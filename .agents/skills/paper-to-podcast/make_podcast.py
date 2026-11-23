"""Render a two-host script into one MP3 with two open-source voice models: Kokoro and Qwen3-TTS (both Apache 2.0).

Usage: python make_podcast.py episodes/<slug>/script.md episodes/<slug>/episode.mp3

Setup (an NVIDIA GPU is required for Qwen3-TTS voices):
    pip install torch --index-url https://download.pytorch.org/whl/cu124
    pip install kokoro-onnx qwen-tts audiotsm lameenc scipy
Then download kokoro-v1.0.onnx and voices-v1.0.bin from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 into the models/ folder next to this file.
The Qwen3-TTS model downloads itself from Hugging Face on the first run.

Only lines of the form "NAME: text" are spoken, with the host's name in capitals. The first host to speak is the
guide, the second is the student. By default the guide is Mei (Kokoro's af_heart voice) and the student is Miguel
(Qwen3-TTS cloning the reference clip assets/voices/miguel.wav). To choose other voices, add a header line such as
"- **Voices:** ANA=af_bella, PEDRO=qwen:pedro". A Kokoro voice is named like af_bella; "qwen:pedro" clones
assets/voices/pedro.wav, whose transcript is in assets/voices/pedro.txt. The guide also reads the tagline and the
closing line. The episode is assembled as: the theme with the tagline, the whole script, and the theme with the
closing line.
"""

import re
import sys
from pathlib import Path

import lameenc
import numpy as np
import soundfile
from kokoro_onnx import Kokoro
from scipy.signal import resample_poly

REPO = Path(__file__).resolve().parents[3]
MODELS = Path(__file__).parent / "models"
THEME = REPO / "assets" / "theme-jasm-heart-madgravitystudio.mp3"
REFERENCE_VOICES = REPO / "assets" / "voices"
DEFAULT_VOICES = ("af_heart", "qwen:miguel")
SAMPLE_RATE = 24000
TURN_LOUDNESS = 0.08
MUSIC_LOUDNESS = 0.10
MUSIC_UNDER_VOICE = 0.38
TURN = re.compile(r"^([A-ZÀ-Ý]+): (.+)$", re.M)
KOKORO_SPEED = 1.1
PAUSE_SECONDS = 0.3
QWEN_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
QWEN_SAMPLING = dict(temperature=0.3, subtalker_temperature=0.3)
QWEN_SEED = 1234
QWEN_SPEED = 1.15
QWEN_LOUDNESS = 1.2
QWEN_PRONUNCIATIONS = {"Miguel": "Mi-GHEL"}
TAGLINE = (
    "The Finance Papers Podcast. A free, open-source educational project in which we discuss and explain classical "
    "papers and current research in finance."
)
CLOSING = (
    "You've been listening to The Finance Papers Podcast. The link to the original paper, the full script, and a "
    "guide to contribute your own episode are on GitHub. Music: JASM HEART, by MadGravityStudio, under a Creative "
    "Commons Attribution license."
)


def voices_for(script):
    """Map each host to a voice: defaults by order of first appearance, overridden by an optional Voices line."""
    hosts = list(dict.fromkeys(name for name, _ in TURN.findall(script)))
    voices = dict(zip(hosts, DEFAULT_VOICES))
    header = re.search(r"^- \*\*Voices:\*\* (.+)$", script, re.M)
    if header:
        voices.update(pair.strip().split("=") for pair in header.group(1).split(","))
    return voices


class Qwen:
    """Qwen3-TTS voice cloning. The model loads on first use, so Kokoro-only scripts run without a GPU."""

    def __init__(self):
        self.model, self.prompts = None, {}

    def say(self, text, name):
        import torch
        from audiotsm import wsola
        from audiotsm.io.array import ArrayReader, ArrayWriter
        from qwen_tts import Qwen3TTSModel

        if self.model is None:
            self.model = Qwen3TTSModel.from_pretrained(QWEN_MODEL, device_map="cuda:0", dtype=torch.bfloat16)
        if name not in self.prompts:
            reference, rate = soundfile.read(REFERENCE_VOICES / f"{name}.wav", dtype="float32")
            transcript = (REFERENCE_VOICES / f"{name}.txt").read_text(encoding="utf-8").strip()
            self.prompts[name] = self.model.create_voice_clone_prompt(ref_audio=(reference, rate), ref_text=transcript)
        for word, spelling in QWEN_PRONUNCIATIONS.items():
            text = text.replace(word, spelling)
        torch.manual_seed(QWEN_SEED)
        wavs, rate = self.model.generate_voice_clone(
            text=text, language="English", voice_clone_prompt=self.prompts[name], **QWEN_SAMPLING
        )
        samples = resample_poly(np.asarray(wavs[0], dtype=np.float32), SAMPLE_RATE, rate)
        writer = ArrayWriter(channels=1)
        wsola(channels=1, speed=QWEN_SPEED).run(ArrayReader(samples.reshape(1, -1)), writer)
        return writer.data.squeeze()


def synthesize(engines, text, voice):
    """Kokoro voices are named like af_heart; Qwen3-TTS cloned voices like qwen:miguel."""
    loudness = TURN_LOUDNESS
    if voice.startswith("qwen:"):
        samples = engines["qwen"].say(text, voice.removeprefix("qwen:"))
        loudness *= QWEN_LOUDNESS
    else:
        samples, _ = engines["kokoro"].create(text, voice=voice, speed=KOKORO_SPEED, lang="en-us")
    return samples.astype(np.float32) * (loudness / np.sqrt(np.mean(samples**2)))


def speak(engines, turns, voices):
    audio = []
    for speaker, text in turns:
        audio += [synthesize(engines, text, voices[speaker]), np.zeros(int(PAUSE_SECONDS * SAMPLE_RATE))]
    return np.concatenate(audio), SAMPLE_RATE


def over_theme(voice, theme, sample_rate, lead=3.0, tail=3.0, duck=MUSIC_UNDER_VOICE):
    """Play the theme alone for `lead` seconds, lower it under the voice, then bring it back and fade it out."""
    voice_start, voice_end = lead, lead + len(voice) / sample_rate
    total = voice_end + tail
    n = int(total * sample_rate)
    bed = np.tile(theme, n // len(theme) + 1)[:n]
    times = [0, voice_start - 0.5, voice_start, voice_end, voice_end + 0.5, total - 2.0, total]
    levels = [1, 1, duck, duck, 1, 1, 0]
    mix = bed * np.interp(np.arange(n) / sample_rate, times, levels)
    start = int(voice_start * sample_rate)
    mix[start:start + len(voice)] += voice
    return mix


def main(script_path, mp3_path):
    text = Path(script_path).read_text(encoding="utf-8")
    voices = voices_for(text)
    guide = next(iter(voices))
    engines = {"kokoro": Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin")), "qwen": Qwen()}

    episode, sample_rate = speak(engines, TURN.findall(text), voices)
    music, music_rate = soundfile.read(THEME)
    theme = resample_poly(music.mean(axis=1), sample_rate, music_rate)
    theme = np.tanh(theme * MUSIC_LOUDNESS / np.sqrt(np.mean(theme**2)))  # soft limiter on the loudest peaks
    intro = over_theme(speak(engines, [(guide, TAGLINE)], voices)[0], theme, sample_rate)
    outro = over_theme(speak(engines, [(guide, CLOSING)], voices)[0], theme, sample_rate)
    audio = np.concatenate([intro, episode, outro])
    pcm = (np.clip(audio, -1, 1) * 32767).astype(np.int16)

    encoder = lameenc.Encoder()
    encoder.set_bit_rate(64)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(1)
    Path(mp3_path).write_bytes(encoder.encode(pcm.tobytes()) + encoder.flush())
    print(f"{len(audio) / sample_rate / 60:.1f} min")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

"""Render a two-host script into one MP3 with two open-source voice models: Kokoro and Qwen3-TTS (both Apache 2.0).

Usage: python make_podcast.py episodes/<slug>/script.md [output.mp3]

Without an output path, the MP3 is written next to the script and named after the APA citation in the script
header, as Surnames_Year_Title.mp3, for example Mehra-Prescott_1985_The-equity-premium-a-puzzle.mp3.

Setup (an NVIDIA GPU is required for Qwen3-TTS voices):
    pip install torch --index-url https://download.pytorch.org/whl/cu124
    pip install kokoro-onnx qwen-tts lameenc scipy
Then download kokoro-v1.0.onnx and voices-v1.0.bin from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 into the models/ folder next to this file.
The Qwen3-TTS models download themselves from Hugging Face on the first run.

Only lines of the form "NAME: text" are spoken, with the host's name in capitals. The first host to speak is the
guide, the second is the student. By default the guide is Mei (Kokoro's af_heart voice) and the student is Miguel
(Qwen3-TTS's built-in Aiden voice). To choose other voices, add a header line such as
"- **Voices:** ANA=af_bella, PEDRO=clone:pedro". A Kokoro voice is named like af_bella; "qwen:Ryan" is one of
Qwen3-TTS's built-in voices; "clone:pedro" makes Qwen3-TTS clone assets/voices/pedro.wav, whose transcript is in
assets/voices/pedro.txt. Built-in and cloned voices use two different Qwen3-TTS models, so an episode should use one
kind or the other unless the GPU has memory for both. The guide also reads the tagline and the closing line. The episode is assembled as: the theme with the tagline, the whole script, and the theme with the
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
DEFAULT_VOICES = ("af_heart", "qwen:Aiden")
SAMPLE_RATE = 24000
TURN_LOUDNESS = 0.08
MUSIC_LOUDNESS = 0.10
MUSIC_UNDER_VOICE = 0.38
TURN = re.compile(r"^([A-ZÀ-Ý]+): (.+)$", re.M)
CITATION = re.compile(r"^- \*\*Paper:\*\* (.+?) \((\d{4})\)\. (.+?)\. \*", re.M)
INITIALS = re.compile(r"^(?:&|and)? ?(?:[A-Z]\.(?: ?[A-Z]\.)*)?$")
KOKORO_SPEED = 1.1
KOKORO_PRONUNCIATIONS = {"is read the original paper": "is reed the original paper"}  # Kokoro says "red" here
PAUSE_SECONDS = 0.3
QWEN_PRESET_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"
QWEN_CLONE_MODEL = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
QWEN_SAMPLING = dict(temperature=0.5, subtalker_temperature=0.5)
QWEN_SEED = 1234
QWEN_MAX_SECONDS_PER_WORD = 1.5  # a longer output is a runaway generation, so cut it off and retry with a new seed
QWEN_TOKENS_PER_SECOND = 12.6  # codec tokens per second of audio, measured on the 12Hz model
QWEN_LOUDNESS = 1.2
QWEN_PRONUNCIATIONS = {"Miguel": "Mi-GHEL"}
TAGLINE = (
    "The Finance and Economics Papers Podcast. A free, open-source educational project in which we discuss and explain "
    "classical papers and current research in finance and economics."
)
CLOSING = (
    "You've been listening to The Finance and Economics Papers Podcast. The link to the original paper, the full "
    "script, and a guide to contribute your own episode are on GitHub. Music: JASM HEART, by MadGravityStudio, under a "
    "Creative Commons Attribution license."
)


def mp3_name(script):
    """Name the audio after the APA citation in the header: Surnames_Year_Title.mp3."""
    authors, year, title = CITATION.search(script).groups()
    surnames = [re.sub(r"^(?:&|and) ", "", part) for part in authors.split(", ") if not INITIALS.match(part)]
    words = lambda text: "-".join(re.sub(r"[^\w\s-]", "", text).split())
    return f"{words(' '.join(surnames))}_{year}_{words(title)}.mp3"


def voices_for(script):
    """Map each host to a voice: defaults by order of first appearance, overridden by an optional Voices line."""
    hosts = list(dict.fromkeys(name for name, _ in TURN.findall(script)))
    voices = dict(zip(hosts, DEFAULT_VOICES))
    header = re.search(r"^- \*\*Voices:\*\* (.+)$", script, re.M)
    if header:
        voices.update(pair.strip().split("=") for pair in header.group(1).split(","))
    return voices


class Qwen:
    """Qwen3-TTS built-in voices ("qwen:Aiden") and cloned voices ("clone:pedro"). Models load on first use."""

    def __init__(self):
        self.models, self.prompts = {}, {}

    def model(self, name):
        import torch
        from qwen_tts import Qwen3TTSModel

        if name not in self.models:
            self.models[name] = Qwen3TTSModel.from_pretrained(name, device_map="cuda:0", dtype=torch.bfloat16)
        return self.models[name]

    def clone_prompt(self, name):
        if name not in self.prompts:
            reference, rate = soundfile.read(REFERENCE_VOICES / f"{name}.wav", dtype="float32")
            transcript = (REFERENCE_VOICES / f"{name}.txt").read_text(encoding="utf-8").strip()
            self.prompts[name] = self.model(QWEN_CLONE_MODEL).create_voice_clone_prompt(
                ref_audio=(reference, rate), ref_text=transcript
            )
        return self.prompts[name]

    def say(self, text, voice):
        import torch

        for word, spelling in QWEN_PRONUNCIATIONS.items():
            text = text.replace(word, spelling)
        kind, name = voice.split(":", 1)
        allowance = QWEN_MAX_SECONDS_PER_WORD * len(text.split()) + 1
        options = dict(text=text, language="English", max_new_tokens=int(QWEN_TOKENS_PER_SECOND * (allowance + 2)),
                       **QWEN_SAMPLING)
        for attempt in range(5):
            torch.manual_seed(QWEN_SEED + attempt)
            if kind == "clone":
                wavs, rate = self.model(QWEN_CLONE_MODEL).generate_voice_clone(
                    voice_clone_prompt=self.clone_prompt(name), **options
                )
            else:
                wavs, rate = self.model(QWEN_PRESET_MODEL).generate_custom_voice(speaker=name, **options)
            if len(wavs[0]) / rate <= allowance:
                break
            print(f"runaway generation ({len(wavs[0]) / rate:.0f} s), retrying: {text[:60]}", flush=True)
        return resample_poly(np.asarray(wavs[0], dtype=np.float32), SAMPLE_RATE, rate)


def synthesize(engines, text, voice):
    """Kokoro voices are named like af_heart; Qwen3-TTS voices like qwen:Aiden (built in) or clone:pedro (cloned)."""
    loudness = TURN_LOUDNESS
    if voice.startswith(("qwen:", "clone:")):
        samples = engines["qwen"].say(text, voice)
        loudness *= QWEN_LOUDNESS
    else:
        for phrase, spelling in KOKORO_PRONUNCIATIONS.items():
            text = text.replace(phrase, spelling)
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


def main(script_path, mp3_path=None):
    text = Path(script_path).read_text(encoding="utf-8")
    mp3_path = mp3_path or Path(script_path).parent / mp3_name(text)
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
    print(f"{mp3_path}: {len(audio) / sample_rate / 60:.1f} min")


if __name__ == "__main__":
    main(*sys.argv[1:3])

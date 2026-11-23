"""Render a two-host script into one MP3 with the open-weight Kokoro voice model (Apache 2.0).

Usage: python make_podcast.py episodes/<slug>/script.md episodes/<slug>/episode.mp3

Setup: pip install kokoro-onnx edge-tts lameenc scipy, then download kokoro-v1.0.onnx and voices-v1.0.bin from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 into the models/ folder next to this file.

Only lines of the form "NAME: text" are spoken, with the host's name in capitals. The first host to speak is the
guide, the second is the student. By default the guide gets Kokoro's af_heart voice and the student Microsoft's
en-US-AndrewNeural voice through edge-tts; to choose
others, add a header line such as "- **Voices:** ANA=af_bella, PEDRO=am_adam". The guide also reads the tagline and
the closing line. The episode is assembled as: the cold open (the first ## section), the theme with the tagline,
the rest of the script, and the theme with the closing line.
"""

import asyncio
import io
import re
import sys
from pathlib import Path

import edge_tts
import lameenc
import numpy as np
import soundfile
from kokoro_onnx import Kokoro
from scipy.signal import resample_poly

REPO = Path(__file__).resolve().parents[3]
MODELS = Path(__file__).parent / "models"
THEME = REPO / "assets" / "theme-jasm-heart-madgravitystudio.mp3"
DEFAULT_VOICES = ("af_heart", "en-US-AndrewNeural")
SAMPLE_RATE = 24000
EDGE_RATE = "+10%"
TURN_LOUDNESS = 0.08
TURN = re.compile(r"^([A-ZÀ-Ý]+): (.+)$", re.M)
SPEED = 1.1
PAUSE_SECONDS = 0.3
TAGLINE = (
    "The Finance Papers Podcast. Research in finance. A free, open-source educational project in which we discuss "
    "and explain classical papers and current research in finance."
)
CLOSING = (
    "You've been listening to The Finance Papers Podcast. The original paper, the full script, and a guide to "
    "contribute your own episode are on GitHub. Music: JASM HEART, by MadGravityStudio, under a Creative Commons "
    "Attribution license."
)


def voices_for(script):
    """Map each host to a voice: defaults by order of first appearance, overridden by an optional Voices line."""
    hosts = list(dict.fromkeys(name for name, _ in TURN.findall(script)))
    voices = dict(zip(hosts, DEFAULT_VOICES))
    header = re.search(r"^- \*\*Voices:\*\* (.+)$", script, re.M)
    if header:
        voices.update(pair.strip().split("=") for pair in header.group(1).split(","))
    return voices


async def edge_mp3(text, voice):
    stream = edge_tts.Communicate(text, voice, rate=EDGE_RATE).stream()
    return b"".join([chunk["data"] async for chunk in stream if chunk["type"] == "audio"])


def synthesize(kokoro, text, voice):
    """Kokoro voices are named like af_heart; Microsoft Edge voices like en-US-AndrewNeural."""
    if voice.endswith("Neural"):
        samples, rate = soundfile.read(io.BytesIO(asyncio.run(edge_mp3(text, voice))), dtype="float32")
        samples = resample_poly(samples, SAMPLE_RATE, rate) if rate != SAMPLE_RATE else samples
    else:
        samples, _ = kokoro.create(text, voice=voice, speed=SPEED, lang="en-us")
    return samples * (TURN_LOUDNESS / np.sqrt(np.mean(samples**2)))


def speak(kokoro, turns, voices):
    audio = []
    for speaker, text in turns:
        audio += [synthesize(kokoro, text, voices[speaker]), np.zeros(int(PAUSE_SECONDS * SAMPLE_RATE))]
    return np.concatenate(audio), SAMPLE_RATE


def over_theme(voice, theme, sample_rate, lead=3.0, tail=3.0, duck=0.2):
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
    cold_open, rest = re.split(r"^## (?!Cold open).*$", text[text.index("## Cold open"):], maxsplit=1, flags=re.M)
    voices = voices_for(text)
    guide = next(iter(voices))
    kokoro = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))

    opening, sample_rate = speak(kokoro, TURN.findall(cold_open), voices)
    body, _ = speak(kokoro, TURN.findall(rest), voices)
    music, music_rate = soundfile.read(THEME)
    theme = 0.5 * resample_poly(music.mean(axis=1), sample_rate, music_rate)
    intro = over_theme(speak(kokoro, [(guide, TAGLINE)], voices)[0], theme, sample_rate)
    outro = over_theme(speak(kokoro, [(guide, CLOSING)], voices)[0], theme, sample_rate)
    audio = np.concatenate([opening, intro, body, outro])
    pcm = (np.clip(audio, -1, 1) * 32767).astype(np.int16)

    encoder = lameenc.Encoder()
    encoder.set_bit_rate(64)
    encoder.set_in_sample_rate(sample_rate)
    encoder.set_channels(1)
    Path(mp3_path).write_bytes(encoder.encode(pcm.tobytes()) + encoder.flush())
    print(f"{len(audio) / sample_rate / 60:.1f} min")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

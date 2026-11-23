"""Render a two-host script into one MP3 with the open-weight Kokoro voice model (Apache 2.0).

Usage: python make_podcast.py episodes/<slug>/script.md episodes/<slug>/episode.mp3

Setup: pip install kokoro-onnx lameenc scipy, then download kokoro-v1.0.onnx and voices-v1.0.bin from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 into the models/ folder next to this file.

Only lines of the form "MEI: text" or "JUAN: text" are spoken. The episode is assembled as: the cold open (the
first ## section), the theme with the tagline, the rest of the script, and the theme with the closing line.
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
VOICES = {"MEI": "af_heart", "JUAN": "am_michael"}
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


def speak(kokoro, turns):
    audio = []
    for speaker, text in turns:
        samples, sample_rate = kokoro.create(text, voice=VOICES[speaker], speed=SPEED, lang="en-us")
        audio += [samples, np.zeros(int(PAUSE_SECONDS * sample_rate), dtype=samples.dtype)]
    return np.concatenate(audio), sample_rate


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
    turn = re.compile(r"^(MEI|JUAN): (.+)$", re.M)
    kokoro = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))

    opening, sample_rate = speak(kokoro, turn.findall(cold_open))
    body, _ = speak(kokoro, turn.findall(rest))
    music, music_rate = soundfile.read(THEME)
    theme = 0.5 * resample_poly(music.mean(axis=1), sample_rate, music_rate)
    intro = over_theme(speak(kokoro, [("MEI", TAGLINE)])[0], theme, sample_rate)
    outro = over_theme(speak(kokoro, [("MEI", CLOSING)])[0], theme, sample_rate)
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

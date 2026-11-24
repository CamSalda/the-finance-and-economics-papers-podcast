---
name: paper-to-podcast
description: Turn an academic finance or economics paper (PDF) into an episode of The Finance and Economics Papers Podcast, a free, open-source, educational show with two hosts who explain the paper in a casual, funny and pedagogical way, and render it to MP3. Use when asked to make a podcast, episode, audio explainer, or script from a paper.
---

# Paper to podcast

The Finance and Economics Papers Podcast is a free, open-source, non-commercial educational project. Its only goal
is to create and spread knowledge about research in finance and economics. Every episode is an independent,
unofficial explanation of one paper, written in our own words for teaching purposes.

This skill produces one episode: a script at `episodes/<slug>/script.md` and audio next to it, which the renderer names
after the APA citation in the script header: `Surnames_Year_Title.mp3`, for example
`Mehra-Prescott_1985_The-equity-premium-A-puzzle.mp3`.
The published episodes in `episodes/` are the reference for tone, pacing and format. Read one before writing.

## Parameters

Ask the user only for what you cannot default.

| Parameter | Default |
|-----------|---------|
| Paper | Required. A PDF path or a citation the user can supply. |
| Length | Set from the paper (see below). Confirm with the user before writing. |
| Tie-in | None. Add a short segment linking the paper to a topic only if the user asks. |
| Slug | Author surnames (up to two, else first author plus `etal`), year, and two or three keywords: `mankiw-1986-equity-premium`. |

Length rule: about 2 minutes per page of main text, between 12 minutes and a hard maximum of 30 minutes. If a paper
needs more, cut to its core results rather than exceed 30 minutes. The voices speak about 150 words per
minute, so target words = minutes x 150. The intro and outro add about one minute, which counts toward the 30.

## The hosts

- **MEI, the guide.** She knows the paper inside out. She introduces every technical term and defines it in plain
  words in the same breath. She drives the structure.
- **MIGUEL, the student.** He is a sharp finance or economics student. He asks the questions a listener would ask
  ("Translate, please"), restates ideas in his own words, pushes back, and brings most of the jokes and analogies.

Keep this dynamic. Mei explains, Miguel checks understanding by paraphrasing, and Mei confirms or corrects.

**Host your own episode.** Mei and Miguel are the default hosts. Contributors are invited to replace them with their
own names in the episodes they add, for example `ANA:` and `PEDRO:`. Keep the two roles: the first host to speak is
the guide and the second is the student. By default the guide has a female voice and the student a male one. To choose
other voices, add a line `- **Voices:** ANA=af_bella, PEDRO=qwen:Ryan` to the header. A plain name is a Kokoro
voice (for example `af_heart`, `af_bella`, `af_nicole`, `am_adam`, `bf_emma`, `bm_george`). `qwen:Ryan` is one of
Qwen3-TTS's built-in voices (Aiden, Ryan, Eric, Dylan, Vivian, Serena and others). `clone:pedro` makes Qwen3-TTS
clone the reference clip `assets/voices/pedro.wav`, with its transcript in `assets/voices/pedro.txt`; never clone a
real person's voice without their permission, and do not mix built-in and cloned Qwen3-TTS voices in one episode,
since they load two different models. Ask the user which
names to use; default to Mei and Miguel.

## Audience and tone

The listener is a finance or economics student with technical training who is still learning.

- Use the real technical terms (pricing kernel, Euler equation, risk aversion) and define each one on first use.
- Never read equations aloud. For each important equation, describe its functional form ("a ratio", "the usual
  kernel times an exponential term"), what it contains, and its intuition.
- Be casual and funny. Use running gags, analogies from daily life, and fun facts from the paper itself:
  the referee, the acknowledgments, footnotes, famous names.
- Repeat the paper's one big idea several times in different words.
- Always include cool and interesting facts around the paper, spread through the episode rather than in one block:
  - **The authors:** where they worked when they wrote it, what else they are known for, prizes, later careers,
    famous textbooks or policy roles.
  - **Academic connections:** advisors and students, co-author networks, the referee or editor, and the people
    thanked in the acknowledgments.
  - **Related papers:** the papers this one answers or builds on, the papers that built on it, famous debates it
    started, and how it is cited or taught today.
  - **The story behind it:** the historical context, the publication history, and surprising footnotes.
- Every episode must stand alone. Never refer to other episodes of the show ("last episode", "welcome back", "as we
  saw before", "in our next episode"), because listeners hear episodes in any order. Mentioning related papers by
  their authors and year is fine; mentioning our episodes of them is not.
- Use no em-dashes. Write short spoken sentences.

## Episode structure

Adapt the segments to the paper, but keep this order:

0. **Intro (automatic).** Every episode starts with the show's theme, with the guide reading the tagline. Do not
   write it into the script: `make_podcast.py` plays it before the first line.
1. **Cold open.** The guide opens with "Welcome to The Finance and Economics Papers Podcast, where we discuss the
   papers that shaped finance and economics, to make reading them easier and more fun." The hosts introduce
   themselves, and the guide reads the spoken educational notice (see below). Then give the paper's citation and
   length, the hook, and the facts about the authors. **The analysis of the paper starts by 3:30 at the latest**,
   and everything about the authors lives here, not later in the episode. Budget, at about 150 words per minute:

   | Block | Time | Words | Content |
   |-------|------|-------|---------|
   | Theme and tagline | 0:18 | automatic | added by the renderer |
   | Welcome and hosts | 0:15 | fixed | the two standard lines |
   | Educational notice | 0:18 | fixed | the standard notice |
   | The paper | 0:20 | 50 | citation, length, one sentence on why it matters |
   | The hook | 0:30 | 75 | the question or the striking number |
   | The authors | 1:15 | 190 | one line per author, one connection, one story from the paper |
   | Bridge | 0:10 | 25 | "Okay, let's start with..." |

   That is about 340 words after the fixed lines and about 3:06 in total, leaving some slack. In the authors block,
   the story comes from the paper itself: a footnote, the acknowledgments, the publication history. Facts that do
   not fit are dropped, not moved. A fact tied to a specific result, such as a prize that result won, may still
   appear where that result is discussed.
2. **The problem.** Explain what puzzle or question the paper answers and why earlier answers fell short.
3. **The setup.** Walk through the model or data step by step, defining every ingredient.
4. **The mechanics.** Go through each main result in turn, with a plain-words punchline for each.
5. **The numbers.** Read the key table or estimates aloud as plain numbers, with what they mean.
6. **Limits.** Cover what the authors concede and what critics or later papers said.
7. **Optional tie-in.** Include this only if the user asked for one.
8. **Wrap-up: the recap.** Every episode must close with a quick recap of the paper, about one minute long. Miguel
   asks and Mei answers, in this order: the research question, the method (model or data, and the empirical or
   theoretical strategy), the main takeaways (two or three results, with the key numbers), and the conclusion
   (what the authors conclude and the main limit). Then Miguel closes with a joke, and both say goodbye. Name the
   segment `## Wrap-up: the recap`.
   - **Outro (automatic).** The theme returns with the closing line and the music credit, which the theme's
     CC BY license requires. `make_podcast.py` adds it after the last line.

## Accuracy

- Every number, quote and proposition about the paper's content must come from the paper. Read the whole paper
  first. If the PDF has no text layer, read the page images.
- Facts about the authors, their connections and related papers may come from outside the paper, but each one must
  be checked against a reliable source: a university or author page, the publisher, Crossref, Wikipedia with a
  cited source, or a prize committee. Drop any fact you cannot verify. Never guess dates, affiliations or
  relationships.
- List every claim from outside the paper, with its source, to the user at the end so they can check it. Hedge any
  claim that is an interpretation rather than a documented fact.
- Never invent a quote.
- Verify the DOI against Crossref (`https://api.crossref.org/works/<doi>`) before putting it in the header.

## Intellectual property

- Explain the paper in your own words. Use only short quotes, and attribute each one to the authors.
- Mention a few key numbers, but never reproduce whole tables, figures or long passages.
- Never upload the paper. Papers are protected by copyright and belong to their authors and publishers. Do not
  commit the paper in any format (PDF, Word, images, screenshots of tables or figures, or long excerpts). Link to it
  by DOI instead.
- Never suggest that the authors or the publisher endorse the episode.

## Script format

Copy the header of an existing script and fill it in. It has, in order:

1. The title line: `# The Finance and Economics Papers Podcast: <episode title>`.
2. The educational notice block quote, copied unchanged from an existing script.
3. A list with the paper's full citation, the DOI link, the topics, the length and the hosts.

Then use `##` headings for segments, starting with `## Cold open`. The generator plays the show's theme and
tagline before the first line, and the theme with the closing credits after the last line. Do not write the
tagline or the music credit into the script. Put each spoken turn on its own line as `NAME: text`, with the host's name in capitals
(`MEI: text`, `MIGUEL: text`). Only those lines are spoken, so headings and notes stay silent.

The spoken notice in the cold open is also copied unchanged from an existing script, spoken by the guide. It starts
with "Quick note before we start. This is an open-source, educational project."

## Render the audio

We use two open-source text-to-speech models, both released under the Apache 2.0 license:

- **[Kokoro](https://huggingface.co/hexgrad/Kokoro-82M)** voices Mei, with its `af_heart` voice. It is a small model
  (82 million parameters) that runs on any computer. We use the
  [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) version.
- **[Qwen3-TTS](https://huggingface.co/collections/Qwen/qwen3-tts)** voices Miguel with the built-in speaker Aiden of its
  [CustomVoice model](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice), at a fixed sampling seed and
  a sampling temperature of 0.5, so Miguel sounds the same in every episode. Its
  [Base model](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) is used only for `clone:` voices.

Both voices are synthetic. Neither imitates a real person.

Always render with `make_podcast.py`: it adds the intro and the outro, including the music credit that the
theme's license requires.

**A GPU is required.** Qwen3-TTS, which voices Miguel, needs an NVIDIA GPU with CUDA and about 8 GB of video
memory. Kokoro, which voices Mei, runs on any computer, so an episode hosted only with Kokoro voices renders without
a GPU.

**Render time.** On a laptop with an NVIDIA RTX 4060 (8 GB), Miguel's lines take about 3 seconds of computing per
second of audio, and Mei's about 0.3 seconds. Rendering therefore takes **about as long as the episode
itself**, 20 to 30 minutes for a full episode. Faster GPUs, or Linux with FlashAttention installed, shorten this. The first run also downloads
the Qwen3-TTS model (about 4.5 GB).

Tell the user about the GPU requirement and the expected render time before starting a render, and run the render
in the background.

```
pip install torch --index-url https://download.pytorch.org/whl/cu124
pip install kokoro-onnx qwen-tts lameenc scipy
python .agents/skills/paper-to-podcast/make_podcast.py episodes/<slug>/script.md
```

The first time, download the two model files listed at the top of `make_podcast.py` into the `models/` folder next
to it. The script prints the episode length when it finishes. If the length misses the target by more than about
10%, or runs past 30 minutes, cut or add dialogue and render again. Then write the length into the script header.

Finally, move the paper from the upcoming list to the library: remove it from `UPCOMING_EPISODES.md`, and add
the episode to `EPISODES.md` (a learning path if one fits, every relevant topic table, and the full list).

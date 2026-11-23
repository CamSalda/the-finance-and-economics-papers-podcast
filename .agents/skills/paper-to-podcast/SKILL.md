---
name: paper-to-podcast
description: Turn an academic finance or economics paper (PDF) into an episode of The Finance Papers Podcast, a free, open-source, educational show with two hosts who explain the paper in a casual, funny and pedagogical way, and render it to MP3. Use when asked to make a podcast, episode, audio explainer, or script from a paper.
---

# Paper to podcast

The Finance Papers Podcast is a free, open-source, non-commercial educational project. Its only goal is to create
and spread knowledge about research in finance. Every episode is an independent, unofficial explanation of one
paper, written in our own words for teaching purposes.

This skill produces one episode: a script at `episodes/<slug>/script.md` and audio at `episodes/<slug>/episode.mp3`.
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
needs more, cut to its core results rather than exceed 30 minutes. The voices speak about 165 words per
minute, so target words = minutes x 165.

## The hosts

- **MEI, the guide.** She knows the paper inside out. She introduces every technical term and defines it in plain
  words in the same breath. She drives the structure.
- **JUAN, the student.** He is a sharp finance student. He asks the questions a listener would ask ("Translate,
  please"), restates ideas in his own words, pushes back, and brings most of the jokes and analogies.

Keep this dynamic. Mei explains, Juan checks understanding by paraphrasing, and Mei confirms or corrects.

## Audience and tone

The listener is a finance student with technical training who is still learning.

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
- Use no em-dashes. Write short spoken sentences.

## Episode structure

Adapt the segments to the paper, but keep this order:

1. **Cold open.** Mei and Juan introduce themselves. Right after, Mei reads the spoken educational notice
   (see below). Then give the paper's citation and length, a fun fact, and a hook question.
2. **The problem.** Explain what puzzle or question the paper answers and why earlier answers fell short.
3. **The setup.** Walk through the model or data step by step, defining every ingredient.
4. **The mechanics.** Go through each main result in turn, with a plain-words punchline for each.
5. **The numbers.** Read the key table or estimates aloud as plain numbers, with what they mean.
6. **Limits.** Cover what the authors concede and what critics or later papers said.
7. **Optional tie-in.** Include this only if the user asked for one.
8. **Wrap-up: the recap.** Every episode must close with a quick recap of the paper, about one minute long. Juan
   asks and Mei answers, in this order: the research question, the method (model or data, and the empirical or
   theoretical strategy), the main takeaways (two or three results, with the key numbers), and the conclusion
   (what the authors conclude and the main limit). Then Juan closes with a joke, and both say goodbye. Name the
   segment `## Wrap-up: the recap`.

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
- Never commit the paper's PDF. Link to it by DOI.
- Never suggest that the authors or the publisher endorse the episode.

## Script format

Copy the header of an existing script and fill it in. It has, in order:

1. The title line: `# The Finance Papers Podcast: <episode title>`.
2. The educational notice block quote, copied unchanged from an existing script.
3. A list with the paper's full citation, the DOI link, the topics, the length and the hosts.

Then use `##` headings for segments. The first segment must be `## Cold open`: the generator plays the show's
theme and tagline right after it, and the theme with the closing credits after the last line. Do not write the
tagline or the music credit into the script. Put each spoken turn on its own line as `MEI: text` or `JUAN: text`. Only
those lines are spoken, so headings and notes stay silent.

The spoken notice in the cold open is also copied unchanged from an existing script. It starts with
"MEI: Quick note before we start. This is an open-source, educational project."

## Render the audio

The voices come from Kokoro, an open-weight model under the Apache 2.0 license. Mei uses `af_heart` and Juan
uses `am_michael`.

```
pip install kokoro-onnx lameenc scipy
python .agents/skills/paper-to-podcast/make_podcast.py episodes/<slug>/script.md episodes/<slug>/episode.mp3
```

The first time, download the two model files listed at the top of `make_podcast.py` into the `models/` folder next
to it. The script prints the episode length when it finishes. If the length misses the target by more than about
10%, or runs past 30 minutes, cut or add dialogue and render again. Then write the length into the script header.

Finally, add the episode to `README.md`: a learning path if one fits, every relevant topic table, and the full list.

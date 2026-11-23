# The Finance Papers Podcast

**The Finance Papers Podcast is a free, open-source, educational project.** Its only goal is to create and
spread knowledge about research in finance. It turns academic papers into casual, pedagogical audio episodes, so
that students, and anyone curious, can learn what the research says and then go read the papers themselves.

The project is non-commercial. It is not affiliated with, sponsored by, or endorsed by any author, journal or
publisher of the papers discussed. Anyone can listen, reuse the material with attribution, and contribute new
episodes.

## How an episode works

Two hosts walk through one paper step by step:

- **Mei, the guide**, knows the paper inside out and explains every technical term as it comes up.
- **Juan, the student**, asks the questions you would ask, restates ideas in his own words, and brings the jokes.

Nobody reads equations aloud: the hosts describe what each equation contains and why it matters. The target
listener is a finance student with some technical training who is still learning. Along the way, the hosts share interesting facts about
the authors, their academic connections and the papers around each one. Every episode comes with its
full script, which doubles as a transcript. Episodes last at most 30 minutes.

Every episode has the same shape: a short cold open, then the show's theme with the tagline "The Finance Papers
Podcast. Research in finance. A free, open-source educational project in which we discuss and explain classical
papers and current research in finance.", then the episode, which always closes with a
one-minute recap of the paper's question, method, main takeaways and conclusions, and the theme again at the end. The generator adds the
theme automatically.

## Learning paths

New to a topic? Start with a path. Each one is a short playlist in the order that builds understanding.

**The equity premium puzzle and heterogeneous consumers**

1. Mehra and Prescott (1985), *The equity premium: A puzzle*. The puzzle itself. *Episode wanted: contribute it!*
2. [Mankiw (1986)](episodes/mankiw-1986-equity-premium/): who bears a recession matters for asset prices.
3. [Constantinides and Duffie (1996)](episodes/constantinides-duffie-1996-heterogeneous-consumers/): the same
   idea in a full dynamic model, where consumption inequality enters the pricing kernel.

## Episodes by topic

A paper can appear under more than one topic.

### Asset pricing

| Paper | Episode | Length |
|-------|---------|--------|
| Mankiw (1986) | [Who pays for the recession?](episodes/mankiw-1986-equity-premium/) | 21 min |
| Constantinides and Duffie (1996) | [The inequality factor](episodes/constantinides-duffie-1996-heterogeneous-consumers/) | 30 min |

### Incomplete markets and heterogeneous agents

| Paper | Episode | Length |
|-------|---------|--------|
| Mankiw (1986) | [Who pays for the recession?](episodes/mankiw-1986-equity-premium/) | 21 min |
| Constantinides and Duffie (1996) | [The inequality factor](episodes/constantinides-duffie-1996-heterogeneous-consumers/) | 30 min |

## All episodes

| Year | Paper | Journal | Length | Listen | Script | Read the paper |
|------|-------|---------|--------|--------|--------|----------------|
| 1986 | Mankiw, *The equity premium and the concentration of aggregate shocks* | Journal of Financial Economics | 21 min | [MP3](episodes/mankiw-1986-equity-premium/episode.mp3) | [Script](episodes/mankiw-1986-equity-premium/script.md) | [DOI](https://doi.org/10.1016/0304-405X(86)90012-7) |
| 1996 | Constantinides and Duffie, *Asset pricing with heterogeneous consumers* | Journal of Political Economy | 30 min | [MP3](episodes/constantinides-duffie-1996-heterogeneous-consumers/episode.mp3) | [Script](episodes/constantinides-duffie-1996-heterogeneous-consumers/script.md) | [DOI](https://doi.org/10.1086/262023) |

To listen, open an MP3 link and use the download button.

## Repository layout

```
AGENTS.md          instructions for AI agents (CLAUDE.md imports it)
episodes/
  <authors>-<year>-<keywords>/
    script.md      full two-host script, with the citation and DOI in its header
    episode.mp3    the rendered audio
assets/
  theme-jasm-heart-madgravitystudio.mp3   the show's theme music (CC BY 4.0, see below)
.agents/skills/paper-to-podcast/
  SKILL.md         instructions for turning a paper into an episode
  make_podcast.py  renders a script into an MP3
```

All episodes sit in one flat folder, named by author surnames, year and two or three keywords, for example
`mankiw-1986-equity-premium`. Folder names never change, so links never break. Topics, journals and years are
handled by the tables above, where one paper can appear in several places.

## Contribute an episode

New episodes are welcome. To make one:

1. Fork this repository.
2. Create `episodes/<authors>-<year>-<keywords>/`.
3. Write `script.md`. The fastest way is the agent skill in
   [.agents/skills/paper-to-podcast](.agents/skills/paper-to-podcast/SKILL.md), which sets out the hosts, tone,
   structure, length rule and accuracy rules. It follows the open [Agent Skills](https://agentskills.io) format, so
   AI coding agents pick it up in this repository: Codex reads `.agents/skills/`, Claude Code reads a pointer in
   `.claude/skills/`, and agents that read `AGENTS.md` are directed to it from there. You can also write the script
   by hand. Copy the header of an existing script, including the educational notice and the spoken notice in the cold open.
4. Render the audio:

   ```
   pip install kokoro-onnx lameenc scipy
   python .agents/skills/paper-to-podcast/make_podcast.py episodes/<slug>/script.md episodes/<slug>/episode.mp3
   ```

   The first time, download the two voice model files listed at the top of
   [make_podcast.py](.agents/skills/paper-to-podcast/make_podcast.py) into the `models/` folder next to it.

5. Add your episode to the learning paths and tables above, then open a pull request.

Before you open the pull request, check these points:

- [ ] The episode lasts 30 minutes or less.
- [ ] The episode closes with the recap: question, method, main takeaways and conclusion.
- [ ] Every number, quote and result in the script comes from the paper.
- [ ] Every fact from outside the paper, such as facts about the authors or related papers, is verified, and its
      source is listed in the pull request.
- [ ] The script explains the paper in your own words. Quotes are short and attributed.
- [ ] No PDF of the paper is committed. Link to it by DOI instead.

## Intellectual property

This project respects the rights of authors and publishers.

- **No papers are hosted here.** Every episode links to the published version through its DOI. The repository
  blocks PDF files so that none is committed by accident.
- **Commentary, not reproduction.** Scripts explain each paper in our own words, for teaching. They use only short,
  attributed quotes, and they mention a few key numbers without reproducing whole tables, figures or passages.
- **Full attribution.** Every script names the authors, the journal and the DOI, in its header and aloud in the
  episode.
- **No endorsement.** Episodes are independent and unofficial. They do not speak for the authors.
- **Takedown requests.** Authors or publishers who want an episode changed or removed can open an issue, and it
  will be handled promptly.

## About the audio

The voices are generated with [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M), an open-weight text-to-speech
model released under the Apache 2.0 license.

The theme music is [JASM HEART](https://freesound.org/people/MadGravityStudio/sounds/834509/) by MadGravityStudio,
licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/). It is used
unchanged, apart from being mixed under the hosts' voices. The credit is also spoken at the end of every episode.

## License

The scripts and audio in this repository are released under the [Creative Commons Attribution 4.0](LICENSE)
license. You can share and adapt them for any purpose, as long as you credit The Finance Papers Podcast. The papers
discussed belong to their authors and publishers and are not covered by this license. The theme music keeps its own
CC BY 4.0 license and credit, given above.

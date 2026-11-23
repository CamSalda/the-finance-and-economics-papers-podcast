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

Coming next: [Upcoming episodes](UPCOMING_EPISODES.md) lists more than fifty landmark papers in finance that we
plan to cover, in APA format. Pick one and contribute it!

## Episodes by topic

A paper can appear under more than one topic.

### Asset pricing

| Paper | Episode | Length |
|-------|---------|--------|
| Mankiw (1986) | [Who pays for the recession?](episodes/mankiw-1986-equity-premium/) | 22 min |
| Constantinides and Duffie (1996) | [The inequality factor](episodes/constantinides-duffie-1996-heterogeneous-consumers/) | 30 min |

### Incomplete markets and heterogeneous agents

| Paper | Episode | Length |
|-------|---------|--------|
| Mankiw (1986) | [Who pays for the recession?](episodes/mankiw-1986-equity-premium/) | 22 min |
| Constantinides and Duffie (1996) | [The inequality factor](episodes/constantinides-duffie-1996-heterogeneous-consumers/) | 30 min |

## All episodes

| Year | Paper | Journal | Length | Listen | Script | Read the paper |
|------|-------|---------|--------|--------|--------|----------------|
| 1986 | Mankiw, *The equity premium and the concentration of aggregate shocks* | Journal of Financial Economics | 22 min | [MP3](episodes/mankiw-1986-equity-premium/episode.mp3) | [Script](episodes/mankiw-1986-equity-premium/script.md) | [DOI](https://doi.org/10.1016/0304-405X(86)90012-7) |
| 1996 | Constantinides and Duffie, *Asset pricing with heterogeneous consumers* | Journal of Political Economy | 30 min | [MP3](episodes/constantinides-duffie-1996-heterogeneous-consumers/episode.mp3) | [Script](episodes/constantinides-duffie-1996-heterogeneous-consumers/script.md) | [DOI](https://doi.org/10.1086/262023) |

To listen, open an MP3 link and use the download button.

## Repository layout

```
AGENTS.md              instructions for AI agents (CLAUDE.md imports it)
UPCOMING_EPISODES.md   landmark papers planned as future episodes
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

## How to contribute

Thank you for being interested in contributing to The Finance Papers Podcast. This is an open-source, collective,
educational effort, and everyone is welcome to contribute: students, researchers, teachers and anyone who loves
finance.

### Ways to contribute

- **Make an episode.** Pick a paper from [Upcoming episodes](UPCOMING_EPISODES.md) and turn it into an episode.
- **Suggest a paper.** Open an issue proposing a paper for the upcoming list, with its full citation and a line on
  why it matters.
- **Review an episode.** Listen to an episode or read a script and report errors, unclear explanations or bad jokes
  by opening an issue.
- **Improve the tools.** Make the skill or the audio generator better.
- **Spread the word.** Share episodes with classmates and use them in your teaching.

### Etiquette

- **Never upload the paper.** Papers are protected by copyright and belong to their authors and publishers. Do
  not commit the paper in any format (PDF, Word, images, screenshots of tables or figures, or long excerpts). Link
  to it by DOI instead.
- **Claim your paper first.** Before you start an episode, open an issue titled `Episode: <authors> (<year>)` so that
  two people don't make the same one. A paper with no open issue is free to take.
- **Open a draft pull request early**, as soon as you have a first version of the script.
- **Say so if you stop.** If you cannot finish, leave a comment on the issue so someone else can take over.
  Inactive claims may be released after a while.

### Make an episode, step by step

1. Claim a paper from [Upcoming episodes](UPCOMING_EPISODES.md) by opening an issue, as above.
2. Fork this repository with the **Fork** button on GitHub.
3. Clone your fork and add this repository as `upstream`:

   ```
   git clone git@github.com:<your-github-handle>/the-finance-papers-podcast.git
   cd the-finance-papers-podcast
   git remote add upstream git@github.com:CamSalda/the-finance-papers-podcast.git
   ```

4. Create a branch for your episode. Never work on `main`.

   ```
   git checkout -b episode-<authors>-<year>
   ```

5. Write `episodes/<authors>-<year>-<keywords>/script.md`. The fastest way is the agent skill in
   [.agents/skills/paper-to-podcast](.agents/skills/paper-to-podcast/SKILL.md), which sets out the hosts, tone,
   structure, length rule and accuracy rules. It follows the open [Agent Skills](https://agentskills.io) format, so
   AI coding agents pick it up in this repository: Codex reads `.agents/skills/`, Claude Code reads a pointer in
   `.claude/skills/`, and agents that read `AGENTS.md` are directed to it from there. You can also write the script
   by hand. Copy the header of an existing script, including the educational notice and the spoken notice in the
   cold open.
6. Render the audio. The first time, download the two voice model files listed at the top of
   [make_podcast.py](.agents/skills/paper-to-podcast/make_podcast.py) into the `models/` folder next to it.

   ```
   pip install kokoro-onnx lameenc scipy
   python .agents/skills/paper-to-podcast/make_podcast.py episodes/<slug>/script.md episodes/<slug>/episode.mp3
   ```

7. Move the paper from the upcoming list to the library:
   - **Remove** the paper from [UPCOMING_EPISODES.md](UPCOMING_EPISODES.md).
   - **Add** the episode to the library in this README: a learning path if one fits, every relevant topic table, and
     the full list of episodes.
8. Commit, sync with the latest version of this repository, and push:

   ```
   git add episodes/<slug> README.md UPCOMING_EPISODES.md
   git commit -m "Add episode on <authors> (<year>)"
   git fetch upstream
   git rebase upstream/main
   git push -u origin episode-<authors>-<year>
   ```

9. Open a pull request from your fork with the **Pull request** button on GitHub, and mention your issue in the
   description (for example, `Closes #12`).

   The `main` branch is protected: nobody commits to it directly, and every pull request needs an approving review
   from a maintainer before it is merged.

### Pull request checklist

Before you submit your pull request, check that your episode meets these guidelines:

- [ ] The issue that claims the paper is referenced in the pull request description.
- [ ] The episode lasts 30 minutes or less.
- [ ] The episode closes with the recap: question, method, main takeaways and conclusion.
- [ ] Every number, quote and result in the script comes from the paper.
- [ ] Every fact from outside the paper, such as facts about the authors or related papers, is verified, and its
      source is listed in the pull request.
- [ ] The script explains the paper in your own words. Quotes are short and attributed.
- [ ] No PDF of the paper is committed. Link to it by DOI instead.
- [ ] The paper is removed from [UPCOMING_EPISODES.md](UPCOMING_EPISODES.md) and added to the library in this README.
- [ ] You have listened to the whole episode at least once.

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

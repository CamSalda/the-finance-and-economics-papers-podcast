# The Finance Papers Podcast: instructions for AI agents

This repository is a free, open-source, educational project. It turns academic papers in finance into two-host
podcast episodes. Each episode lives in `episodes/<authors>-<year>-<keywords>/` as `script.md` plus `episode.mp3`.

To create an episode from a paper, follow the skill in `.agents/skills/paper-to-podcast/SKILL.md`. It defines the
hosts, tone, structure, the 30-minute maximum, the accuracy and intellectual-property rules, and how to render audio.

Rules that always apply:

- Never upload the paper. Papers are protected by copyright and belong to their authors and publishers. Do not
  commit the paper in any format (PDF, Word, images, screenshots of tables or figures, or long excerpts). Link to it
  by DOI instead.
- Every number, quote and result in a script must come from the paper.
- After adding an episode, remove its paper from `UPCOMING_EPISODES.md` and add the episode to the learning paths
  and tables in `README.md`. Contributors follow the "How to contribute" section of the README.

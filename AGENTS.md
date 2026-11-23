# The Finance Papers Podcast: instructions for AI agents

This repository is a free, open-source, educational project. It turns academic papers in finance into two-host
podcast episodes. Each episode lives in `episodes/<authors>-<year>-<keywords>/` as `script.md` plus `episode.mp3`.

To create an episode from a paper, follow the skill in `.agents/skills/paper-to-podcast/SKILL.md`. It defines the
hosts, tone, structure, the 30-minute maximum, the accuracy and intellectual-property rules, and how to render audio.

Rules that always apply:

- Never commit PDFs of papers. Link to them by DOI.
- Every number, quote and result in a script must come from the paper.
- After adding an episode, update the learning paths and tables in `README.md`.

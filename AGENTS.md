# The Finance Papers Podcast: instructions for AI agents

This repository is a free, open-source, educational project. It turns academic papers in finance into two-host
podcast episodes. Each episode lives in `episodes/<authors>-<year>-<keywords>/` as `script.md` plus `episode.mp3`.

To create an episode from a paper, follow the skill in `.agents/skills/paper-to-podcast/SKILL.md`. It defines the
hosts, tone, structure, the 30-minute maximum, the accuracy and intellectual-property rules, and how to render audio.

Rules that always apply:

- Every episode opens and closes with the show's theme, which carries the tagline and the music credit. Always render
  with `.agents/skills/paper-to-podcast/make_podcast.py`, which adds both, and start every script with a
  `## Cold open` section. The theme plays at the very start, before the first line.
- Rendering needs an NVIDIA GPU, because Miguel's voice uses Qwen3-TTS. A full episode takes roughly 25 to 45 minutes
  to render on a laptop GPU, so run it in the background. Mei's voice uses Kokoro. Both models are open source. Never write the tagline or the music credit into a script.
- The default hosts are Mei (the guide) and Miguel (the student). Contributors may host their own episodes under their
  own names; keep the two roles.
- Never upload the paper. Papers are protected by copyright and belong to their authors and publishers. Do not
  commit the paper in any format (PDF, Word, images, screenshots of tables or figures, or long excerpts). Link to it
  by DOI instead.
- Every episode stands alone: never refer to other episodes of the show, because listeners hear them in any order.
  Mentioning related papers by their authors is fine.
- Every number, quote and result in a script must come from the paper.
- After adding an episode, remove its paper from `UPCOMING_EPISODES.md` and add the episode to the learning paths
  and tables in `EPISODES.md`. Contributors follow the "How to contribute" section of the README.

# Lemo-Opuscar ChatGPT Edition 1.0.0-rc.2

Unofficial adaptation of LemoLab's [Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar).

This standalone Agent Skill includes 66 style guides, the original core renderer, a beginner-friendly original 2-second demo, offline preflight, manual dependency installation, approval gates, and rights notices. **No remote render backend is bundled.**

Start here: `references/GETTING_STARTED.md`; run `python3 scripts/doctor.py`; inspect `references/COMPATIBILITY.md`. These are Markdown files, not DOCX: the external multilingual DOCX guides are distributed OUTSIDE the installation ZIP.

To run a video locally, Node >=20, Python >=3.11, FFmpeg and Chromium are required; the user must approve dependency downloads separately. See `ATTRIBUTION.md`.

## UI identity in v1.0.0-rc.2

The ChatGPT skill now includes `agents/openai.yaml` and 128/512 px PNG icon files. The plugin also exposes a composer icon and primary logo. After installing the new ZIP, reload or reopen the ChatGPT Skills/Plugins screen. Display behavior may vary by host; an icon is not proof of video-render availability.

# Quick Start — Lemo-Opuscar ChatGPT Edition

## Choose your path

**No technical experience / no terminal:** Open the skill or plugin in an eligible ChatGPT environment and say: "Help me make a 30-second vertical video about [topic]. First show me style options and a storyboard. Don't render anything before I approve." The assistant can plan with you. It can only render a video if its host also has a suitable execution environment and the required software.

**Local computer / Codex or Work with terminal:** Extract one ZIP archive; preserve folder structure. Run `python3 scripts/doctor.py` from the library root. If dependencies are missing, install them deliberately by following the separate external DOCX instructions or by running `sh scripts/install_deps.sh core`. This installs Node/Python packages, but not operating-system packages such as FFmpeg or Node. Run `python3 scripts/smoke_test.py --render` to test the neutral included clip; test files are saved in `examples/first-film/out/`.

## Six-stage workflow
1. Tell the assistant your topic, goal, target viewer, approximate duration, language and orientation.
2. View recommended styles and choose one; or ask for a custom style.
3. Review and explicitly approve the treatment and storyboard.
4. Review sample frames or each scene as you prefer.
5. Approve a full render and any voice or other online services.
6. Review actual output and request edits; publishing remains a separate approval.

## Prompt examples
- "Use Lemo-Opuscar ChatGPT Edition. Suggest three styles for a 45-second English explainer on reducing repetitive work. I approve only the plan, not rendering."
- "Compare the Whiteboard and Swiss Motion styles for a beginner-friendly vertical promo. Show two motion concepts for each."
- "Check the included smoke test, report exact missing dependencies and do not download anything."
- "I approve the storyboard only. Produce one 640×360 preview frame to review; no voice, no final render."

## Important distinction
Skill: instructions, reference library and local rendering scripts. Plugin: a portable package that exposes the same skill through supported Plugin surfaces. There is **no cloud render service**. ZIP installation, host access, and actual rendering capabilities depend on the ChatGPT/Codex surface and user's permissions.

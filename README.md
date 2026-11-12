# Lemo-Opuscar for ChatGPT

**Unofficial ChatGPT Skill and Agent Plugin adaptation of LemoLab's Lemo-Opuscar.**  
Maintained by **TimNao — AI Skills Lab** · [Website](https://timnao.com)

> **Current release: v1.0.0-rc.2 (pre-release).** This version adds Skill and Plugin icons and metadata. It is not a verified, fully working one-click video-rendering service. Full end-to-end rendering and direct installation in every ChatGPT environment remain unverified.

## What does it do?

Lemo-Opuscar is a code-driven video creation toolkit. This unofficial adaptation helps you:

- Plan original short videos, animated explainers, and promotional content.
- Explore **66 included visual style guides**.
- Write treatments, scripts, storyboards, shot lists, and motion plans before production.
- Inspect a local rendering environment and, when the required execution tools are available, use the bundled renderer to produce video assets.
- Review and approve the creative plan before assets are produced or content is published.

**Important:** In ChatGPT sessions without an authorized local code/browser execution environment, the Skill can help plan and storyboard; it cannot automatically render MP4 files. No hosted rendering backend or MCP server is included.

## Choose a package

Both packages belong to the **same project**. You generally need only one.

| Package | Best for | Contents |
| --- | --- | --- |
| **ChatGPT Skill ZIP** | Installing a standalone Skill | `SKILL.md`, icon metadata, style guides, scripts, local renderer, references |
| **ChatGPT Plugin ZIP** | Installing an Agent Plugin that includes the Skill | `plugin.json`, embedded Skill, icon metadata, style guides, scripts, local renderer |

**Download the two installation packages from [Release v1.0.0-rc.2](https://github.com/timnaocom/lemo-opuscar-chatgpt/releases/tag/v1.0.0-rc.2)** once the release is published. Select the named Skill or Plugin ZIP under **Assets**; GitHub's automatically generated *Source code (zip)* is not the installation package.

The Release also includes separate English and Vietnamese DOCX user guides and changelog TXT files. **DOCX files are not included inside the installation ZIPs.**

## Getting started

1. Download either the **Skill ZIP** or the **Plugin ZIP** from the release assets.
2. Open ChatGPT **Skills** or **Plugins**, depending on which type you want to install, and use the available import/install option. Availability and supported features may depend on your account and interface.
3. After installation, reopen the Skills/Plugins page to check the displayed name and icon.
4. Try this beginner prompt:

   > Help me choose a Lemo-Opuscar style for a 30-second explainer. Propose a storyboard first. Do not render or publish anything until I approve.

For actual local rendering, read the bundled `references/GETTING_STARTED.md` and `references/COMPATIBILITY.md`, then run the read-only preflight from the package's library folder:

```bash
python3 scripts/doctor.py
```

Local production requires **Node.js 20+, Python 3.11+, FFmpeg/ffprobe, and Chromium/Playwright**. Installing dependencies and using any external voice or music service require separate permission. The renderer's dependencies are **not** automatically installed by adding the Skill or Plugin in ChatGPT.

## Testing and known limitations

The `v1.0.0-rc.2` packages passed ZIP integrity, layout/manifest/icon-path, and selected Python/JavaScript checks. All **66 style manifests** were present. An isolated FFmpeg audio/video mux test produced a short H.264/AAC MP4.

**Not yet verified:** complete browser-driven video rendering, real-world functionality of every style, and successful installation/rendering in all ChatGPT execution environments. Treat this release as a preview and report reproducible issues.

## Release details

- **Version:** `v1.0.0-rc.2`
- **Status:** Pre-release / release candidate
- **Main change from `rc.1`:** Added PNG icons and UI identity metadata for both Skill and Plugin; production capabilities and known rendering limitations are unchanged.
- **Feedback:** Open a GitHub Issue with the platform, steps to reproduce, relevant non-sensitive logs, and expected vs. actual results.

## Original author, license, and attribution

**Original project:** [Lemo-Opuscar by LemoLab](https://github.com/lemomo-ai/lemo-opuscar).  
**Upstream code/documentation:** MIT License, copyright © 2026 LemoLab. See [`LICENSE`](LICENSE) and [`ATTRIBUTION.md`](ATTRIBUTION.md).  
**Adaptation:** TimNao — AI Skills Lab (unofficial).

The upstream project has additional terms for media and some voice assets. This adaptation excludes original demo footage and voice tracks; bundled fonts and materials have their own attribution notices. Check the full notices before redistributing assets or publishing media.

This project is **not affiliated with or endorsed by LemoLab, OpenAI, or Anthropic**.

## Useful links

- [TimNao website](https://timnao.com)
- [Original Lemo-Opuscar repository](https://github.com/lemomo-ai/lemo-opuscar)
- [Releases](https://github.com/timnaocom/lemo-opuscar-chatgpt/releases)
- [Report an issue](https://github.com/timnaocom/lemo-opuscar-chatgpt/issues)

# Lemo-Opuscar for ChatGPT

**Unofficial ChatGPT Skill and Agent Plugin adaptation of LemoLab's Lemo-Opuscar.**

Maintained by **TimNao — AI Skills Lab**.

Website: https://timnao.com

> **Current version: v1.0.0-rc.2 — Pre-release**
>
> This release introduces updated Skill and Plugin icons, display metadata, and beginner-friendly workflows. Full end-to-end rendering and compatibility across all ChatGPT environments have not yet been verified.

## Overview

Lemo-Opuscar for ChatGPT adapts the original code-driven video production toolkit by LemoLab.

It provides 66 visual style guides, video planning workflows, storyboarding tools, and a local rendering toolchain for supported execution environments.

### Key Features

- **66 Visual Styles:** Explore distinctive animation and video design approaches.
- **AI-Assisted Storyboarding:** Develop original scripts, scenes, camera movements, and transitions.
- **ChatGPT Skill:** Guide creative planning and use local rendering tools when available.
- **Agent Plugin:** An alternative package that includes the Skill.
- **Human Approval:** Review the creative plan before production or publishing.
- **Beginner-Friendly Guides:** English and Vietnamese installation and usage documentation.
- **Versioned Releases:** Clearly identified installation packages and changelogs.

**Important:** Installing the Skill or Plugin does not automatically provide local rendering capabilities. A compatible execution environment is required to produce MP4 files. No hosted rendering backend is included.

## Download and Installation

### Latest Pre-release — v1.0.0-rc.2

[Download v1.0.0-rc.2 from GitHub Releases](https://github.com/timnaocom/lemo-opuscar-chatgpt/releases/tag/v1.0.0-rc.2)

Choose one installation package:

| Package | Recommended For |
|---|---|
| ChatGPT Skill ZIP | Users who want to install the standalone Skill |
| ChatGPT Plugin ZIP | Users who prefer the Agent Plugin package, which includes the Skill |

You generally do not need to install both.

Additional release downloads include:

- English User Guide (DOCX)
- Vietnamese User Guide (DOCX)
- English Changelog (TXT)
- Vietnamese Changelog (TXT)

**Note:** Choose the specifically named Skill or Plugin ZIP under Release Assets, not GitHub's automatically generated source archive.

## Getting Started

1. Download the appropriate package from GitHub Releases.
2. Open ChatGPT Skills or Plugins, depending on the package.
3. Use the available installation or import option.
4. Reopen the Skills/Plugins page and check the installed package.
5. Start with a simple video planning request.

### Example Prompt

"Help me create a 30-second animated explainer using Lemo-Opuscar. Recommend three visual styles, prepare a storyboard, and explain the production steps. Do not render or publish anything until I approve."

For local video rendering, the bundled toolchain requires Node.js 20+, Python 3.11+, FFmpeg/ffprobe, and Chromium/Playwright.

Read the included GETTING_STARTED and COMPATIBILITY documentation before installing additional dependencies.

## Testing and Compatibility

### Verified

- Installation ZIP structure and integrity
- Skill and Plugin manifest structure
- Icon files and metadata paths
- Presence of all 66 style manifests
- Selected Python and JavaScript checks
- Isolated FFmpeg H.264/AAC mux test

### Not Yet Fully Verified

- Complete browser-driven video rendering
- Real-world rendering of every visual style
- Video production inside every ChatGPT execution environment

**This is a release candidate, not a fully validated stable release.**

## What's New in v1.0.0-rc.2

- Added custom PNG icons for the Skill and Plugin.
- Added Skill interface metadata.
- Added Plugin icon and branding metadata.
- Updated installation documentation.
- Preserved the 66 visual style guides and rendering toolchain.
- Retained the known rendering and environment limitations.

See the included changelog files for more information.

## Credits and Licensing

**Original project:** [Lemo-Opuscar by LemoLab](https://github.com/lemomo-ai/lemo-opuscar)

Original source code and documentation: MIT License.

Copyright © 2026 LemoLab.

This unofficial adaptation is maintained by **TimNao — AI Skills Lab**.

Some upstream media and third-party resources use separate licenses. Original demo footage and voice tracks are not included in the installation packages.

See the LICENSE, ATTRIBUTION.md, and bundled asset notices for details.

This project is not affiliated with or endorsed by LemoLab, OpenAI, or Anthropic.

## Community and Support

Found a bug, installation issue, or compatibility problem?

Please report it through GitHub Issues and include your environment, reproduction steps, and relevant non-sensitive logs.

## Links

- Website: https://timnao.com
- Original project: https://github.com/lemomo-ai/lemo-opuscar
- Releases: https://github.com/timnaocom/lemo-opuscar-chatgpt/releases
- GitHub Issues: https://github.com/timnaocom/lemo-opuscar-chatgpt/issues

---

**TimNao — AI Skills Lab**

*Discover. Adapt. Test. Share.*

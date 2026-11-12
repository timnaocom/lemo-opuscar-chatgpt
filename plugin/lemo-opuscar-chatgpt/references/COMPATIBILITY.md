# Compatibility and limitations — v1.0.0-rc.2

- Portable Agent Skills style: the standalone SKILL.md is available at package root.
- Portable Agent Plugins format: the plugin ZIP has root `plugin.json` and `skills/lemo-opuscar-chatgpt/SKILL.md`.
- ChatGPT Chat without terminal/computer access: planning and help only, not a verified MP4 render path.
- ChatGPT Work or Codex with accessible terminal/files: candidate for end-to-end rendering. An account-specific installation test must be done in that host; no claim of universal installation.
- Node >=20, Python >=3.11, FFmpeg + ffprobe, Chromium and npm/Python dependencies required for local capture; `core/` includes rendering tools but not operating system packages.
- The included original sample uses Canvas 2D; GPU-demanding 3D styles require hardware/drivers and sometimes external licensed media.
- Voice is optional. Online voices/downloads are never enabled silently. Dedicated Whisper/Kokoro models are NOT embedded in the archives.
- Source snapshot is a user-supplied ZIP; exact git commit is unknown. We preserve README/license and use a reproducible ZIP SHA256 in `SOURCE_SNAPSHOT.json`.
- Advanced demo-specific tools and example media were deliberately excluded for safety and size; some complex styles require separately reviewed upstream assets/code.
- Public Plugin Directory acceptance, actual ChatGPT account installation and all 66 film styles remain unverified in this release. Static and small browser-render tests are separate from application-level certification.

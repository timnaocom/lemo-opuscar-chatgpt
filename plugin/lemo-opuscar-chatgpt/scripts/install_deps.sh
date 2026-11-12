#!/bin/sh
# Manual install only. Network download and package installation will occur.
set -eu
HERE=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
TIER=${1:-}
if [ "$TIER" != core ] && [ "$TIER" != voice ] && [ "$TIER" != music ]; then
 echo 'Usage: sh scripts/install_deps.sh core|voice|music' >&2; exit 2
fi
command -v node >/dev/null || { echo 'Node >=20 must be installed separately.' >&2; exit 2; }
command -v npm >/dev/null || { echo 'npm is missing.' >&2; exit 2; }
command -v ffmpeg >/dev/null || { echo 'FFmpeg must be installed separately.' >&2; exit 2; }
cd "$HERE"
echo 'This command downloads packages from npm/PyPI and may download a browser and large voice models.'
echo 'No updates to git repositories are performed; no publishing is performed.'
if [ "${LEMO_INSTALL_APPROVED:-}" != yes ]; then
  printf 'Type YES to continue: '
  read -r ANSWER
  [ "$ANSWER" = YES ] || { echo 'Cancelled.'; exit 1; }
fi
npm ci
if [ -z "${PLAYWRIGHT_CHROME:-}" ]; then
  npx playwright-core install chromium-headless-shell
fi
if command -v python3.12 >/dev/null 2>&1; then PY=python3.12
elif command -v python3.11 >/dev/null 2>&1; then PY=python3.11
elif command -v python3 >/dev/null 2>&1; then PY=python3
else PY=python; fi
"$PY" -m venv .venv
if [ -x .venv/bin/python ]; then V=.venv/bin/python; else V=.venv/Scripts/python.exe; fi
"$V" -m pip install -r requirements.txt
if [ "$TIER" = voice ]; then
  "$V" -m pip install -r requirements-voice.txt
  echo 'Voice models may need a separate download; see references/upstream/TECHNIQUE.md.'
fi
if [ "$TIER" = music ]; then "$V" -m pip install -r requirements-music.txt; fi
"$V" scripts/doctor.py

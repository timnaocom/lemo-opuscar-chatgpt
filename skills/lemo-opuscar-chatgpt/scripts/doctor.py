#!/usr/bin/env python3
"""Read-only diagnostic for Lemo-Opuscar ChatGPT Edition."""
import os, sys, json, shutil, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def cmd(x, arg='--version'):
    path=shutil.which(x)
    if not path:return 'MISSING'
    try:r=subprocess.run([path,arg],capture_output=True,text=True,timeout=10);return (r.stdout or r.stderr).strip().splitlines()[0][:120]
    except Exception as e:return f'ERROR: {e}'
def main():
    print('Lemo-Opuscar ChatGPT Edition — read-only doctor')
    print('Package root:',ROOT)
    print('Python:',sys.version.split()[0], 'OK' if sys.version_info >=(3,11) else 'NEEDS >=3.11')
    for x in ['node','npm','ffmpeg','ffprobe','git']:
        print(f'{x}: {cmd(x)}')
    chrome=os.environ.get('PLAYWRIGHT_CHROME') or next((shutil.which(x) for x in ['chromium','chromium-browser','google-chrome','chrome']),None)
    print('Chromium executable:',chrome or 'not detected; Playwright may install its own headless shell')
    for x in ['core/render/video.mjs','core/render/still.mjs','package.json','package-lock.json','styles/README.md','LICENSE']:
        print('OK' if (ROOT/x).exists() else 'MISSING',x)
    print('Style manifests:',len([p for p in (ROOT/'styles').glob('*/style.json') if p.parent.name!='_template']))
    for x in ['playwright-core','three']:
        print('npm',x, 'INSTALLED' if (ROOT/'node_modules'/x).exists() else 'NOT INSTALLED')
    print('Python venv:', 'present' if (ROOT/'.venv').exists() else 'not installed (optional for core sound and voice)')
    print('No network requests, installs, or mutations were performed.')
if __name__=='__main__':main()

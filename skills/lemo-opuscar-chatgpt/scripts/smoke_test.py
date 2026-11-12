#!/usr/bin/env python3
"""Read-only layout check, optionally render a small ORIGINAL demo."""
from pathlib import Path
import subprocess,sys,shutil,json, argparse
P=argparse.ArgumentParser();P.add_argument('--render',action='store_true',help='render 2-sec silent sample locally');a=P.parse_args()
R=Path(__file__).resolve().parents[1]
p=subprocess.run([sys.executable,str(R/'scripts/verify_package.py')],check=False)
if p.returncode:sys.exit(p.returncode)
if not a.render:
 print('No render requested. Use --render after installing local tools.')
 sys.exit(0)
if not shutil.which('node') or not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
 print('Render unavailable: requires Node, FFmpeg and FFprobe. See doctor.py.');sys.exit(2)
if not (R/'node_modules/playwright-core').exists():
 print('Render unavailable: run the separately approved sh scripts/install_deps.sh core.');sys.exit(2)
sample=R/'examples/first-film';out=sample/'out/smoke.mp4';out.parent.mkdir(parents=True,exist_ok=True)
cmd=['node',str(R/'core/render/video.mjs'),str(sample),'--fps','12','--workers','1','--size','640x360','--out',str(out)]
print('Running:', ' '.join(cmd), flush=True)
r=subprocess.run(cmd,cwd=str(R),check=False)
if r.returncode:sys.exit(r.returncode)
meta=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name,width,height','-of','json',str(out)],capture_output=True,text=True,check=True)
info=json.loads(meta.stdout); duration=float(info['format']['duration'])
if not out.is_file() or out.stat().st_size<5000 or not (1.8<=duration<=2.2):
 print('Output validation failed',info);sys.exit(1)
print('RENDER PASS:',out,'bytes:',out.stat().st_size,'duration:',duration)

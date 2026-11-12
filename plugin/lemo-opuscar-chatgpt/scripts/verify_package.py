#!/usr/bin/env python3
"""Validate static package layout, intended style index and license refs."""
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
errs=[]
for f in ['LICENSE','ATTRIBUTION.md','core/render/video.mjs','core/render/still.mjs','styles/README.md','references/GETTING_STARTED.md','references/QA_AND_APPROVAL.md','examples/first-film/index.html']:
 if not (R/f).is_file():errs.append('missing '+f)
styles=list((R/'styles').glob('*/style.json'))
styles=[p for p in styles if p.parent.name!='_template']
for p in styles:
 try:
  j=json.loads(p.read_text());assert j.get('slug')==p.parent.name
  assert (p.parent/'STYLE.md').is_file()
 except Exception as e:errs.append(str(p)+': '+str(e))
if len(styles)!=66:errs.append('expected 66 styles, found '+str(len(styles)))
if (R/'plugin.json').exists():
 try:
  j=json.loads((R/'plugin.json').read_text());assert j['name']=='lemo-opuscar-chatgpt';assert (R/'skills/lemo-opuscar-chatgpt/SKILL.md').is_file()
 except Exception as e:errs.append('plugin manifest '+str(e))
else:
 if not (R/'SKILL.md').exists():errs.append('standalone skill missing')
print('Static verification:','PASS' if not errs else 'FAIL')
print('styles:',len(styles),'errors:',errs)
sys.exit(1 if errs else 0)

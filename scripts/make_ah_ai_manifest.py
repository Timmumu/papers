# -*- coding: utf-8 -*-
"""Build ah_ai_manifest.json: batches of full-coded papers for AH/AI enrichment."""
import os, re, json, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_data
from screening_data import S

S3 = step3_data.S3
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
SS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss'

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
rid_of, ti_of = {}, {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    m = re.search(r'^ID  - (.*?)$', r, re.M)
    rid_of[n] = m.group(1).strip() if m else ''
    ti = re.search(r'^TI  - (.*?)(?=^[A-Z0-9]{2}  - |\Z)', r, re.M | re.S)
    ti_of[n] = ' '.join(ti.group(1).split()) if ti else ''

full = sorted(n for n, v in S3.items() if v[0] == 'Yes' and v[1] == 'Yes' and v[2] == 'Yes')
items = []
for n in full:
    rid, slug = rid_of[n], S[n][7]
    p = os.path.join(FT, f'{rid}_{slug}.txt')
    items.append(dict(n=n, rid=rid, slug=slug, tier=S3[n][3], z=S3[n][7],
                      title=ti_of[n], txt=os.path.normpath(p) if os.path.exists(p) else '',
                      ag_head=S3[n][14][:200]))

B = 12  # batch size
batches = [items[i:i + B] for i in range(0, len(items), B)]
manifest = dict(batches={i: b for i, b in enumerate(batches)})
json.dump(manifest, open(os.path.join(SS, 'ah_ai_manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('full-coded:', len(items), '| batches:', len(batches))
for i, b in enumerate(batches):
    print(f'  batch {i}: {len(b)} papers, idx {b[0]["n"]}..{b[-1]["n"]}')
print('manifest ->', os.path.join(SS, 'ah_ai_manifest.json'))

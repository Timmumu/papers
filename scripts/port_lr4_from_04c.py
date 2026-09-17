# -*- coding: utf-8 -*-
"""Port 04c Step-3 codes into LR4 for overlapping papers (matched by DOI,
then normalized title). LR4 rows key the stores; codes are copied verbatim
from 04c step3_data / step3_extra / step3_fusion, SRC marked '04c-port'.

Usage: .venv\\Scripts\\python.exe scripts/port_lr4_from_04c.py
"""
import json
import os
import re
import sys
import difflib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
RIS = os.path.join(ROOT, '04c_LR 3round', '429 papers.txt')

sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import step3_data, step3_extra, step3_fusion  # noqa: E402
from screening_data_lr4 import S4, decision  # noqa: E402

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}
INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')


def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


# ---- 04c: index n -> (doi, title) ----
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
meta4 = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''
    meta4[n] = dict(doi=field('DO'), ti=field('TI'))

doi4 = {}
ti4 = {}
for k, v in meta4.items():
    if v['doi']:
        doi4[norm(v['doi'])] = k
    if len(norm(v['ti'])) >= 30:
        ti4[norm(v['ti'])] = k

# ---- load LR4 stores ----
import step3_lr4_data, step3_lr4_extra, step3_lr4_fusion
S3L = step3_lr4_data.S3L
AH = step3_lr4_extra.AH
AI = step3_lr4_extra.AI
FD = step3_lr4_fusion.FD
FDEV = step3_lr4_fusion.FDEV
FDCF = step3_lr4_fusion.FDCF

ported = skipped = 0
for r in INCLUDED:
    if r in S3L:
        continue
    rec = BYROW[r]
    k4 = None
    if rec['doi']:
        k4 = doi4.get(norm(rec['doi']))
    if k4 is None:
        k4 = ti4.get(norm(rec['title']))
    if k4 is None:
        # near-exact title fallback
        ti = norm(rec['title'])
        best = None
        for t, kk in ti4.items():
            ratio = difflib.SequenceMatcher(None, ti, t).ratio()
            if best is None or ratio > best[0]:
                best = (ratio, kk)
        if best and best[0] >= 0.99:
            k4 = best[1]
    if k4 is None or k4 not in step3_data.S3:
        skipped += 1
        continue
    v = list(step3_data.S3[k4])
    # replace SRC with LR4 source marker
    v[15] = '04c-port'
    S3L[r] = tuple(v)
    if k4 in step3_extra.AH:
        AH[r] = step3_extra.AH[k4]
        AI[r] = step3_extra.AI[k4]
    if k4 in step3_fusion.FD:
        FD[r] = step3_fusion.FD[k4]
        FDEV[r] = step3_fusion.FDEV[k4]
        FDCF[r] = step3_fusion.FDCF[k4]
    ported += 1
    print('R%03d %-18s <- 04c#%d [%s]' % (r, rec['slug'], k4, meta4[k4]['doi']))

# write back into the store modules (plain python files)
def dump(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

rows = sorted(S3L)
dump(os.path.join(ROOT, 'scripts', 'step3_lr4_data.py'), [
    '# -*- coding: utf-8 -*-',
    '"""LR4 Step-3 deep-read codes for included papers (Prompt B).',
    'Keyed by corpus row r (1..956). Value tuple:',
    '(P, Q, R, U-Tier, V, W, X, Z-DfX, AA-selfimprove, AB-method, AC-modality,',
    ' AD-validation, AE-QA, AF-cluster, AG-key evidence[, SRC-fulltext-source]).',
    'Only papers with P=Q=R=Yes get full codes. Otherwise P/Q/R recorded, rest blank.',
    '16th element (optional) = full-text source label.',
    '"""',
    'S3L = {',
] + ['%d: %r,' % (r, S3L[r]) for r in rows] + ['}', ''])

dump(os.path.join(ROOT, 'scripts', 'step3_lr4_extra.py'), [
    '# -*- coding: utf-8 -*-',
    '"""LR4 AH (strength & gap filled) and AI (deficiencies & future work) for',
    'the full-coded Step-3 papers. Keyed by corpus row r."""',
    '', 'AH = {',
] + ['%d: %r,' % (r, AH[r]) for r in sorted(AH)] + ['}', '', 'AI = {',
] + ['%d: %r,' % (r, AI[r]) for r in sorted(AI)] + ['}', ''])

dump(os.path.join(ROOT, 'scripts', 'step3_lr4_fusion.py'), [
    '# -*- coding: utf-8 -*-',
    '"""LR4 fusion-depth coding (after AC data modality).',
    'FD: Co-present | Aligned | Fused | SINGLE | Unclear; FDEV: evidence;',
    'FDCF: High | Medium | Low. Keyed by corpus row r."""',
    '', 'FD = {',
] + ['%d: %r,' % (r, FD[r]) for r in sorted(FD)] + ['}', '', 'FDEV = {',
] + ['%d: %r,' % (r, FDEV[r]) for r in sorted(FDEV)] + ['}', '', 'FDCF = {',
] + ['%d: %r,' % (r, FDCF[r]) for r in sorted(FDCF)] + ['}', ''])

print('ported=%d skipped=%d' % (ported, skipped))

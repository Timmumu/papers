# -*- coding: utf-8 -*-
"""Build LR4 Step-3 coding worksheets from staged fulltexts.

For every verified staged fulltext, write a compact extract into
  04d_LR4/5. SLR matrix/ss/coding/batchNN.txt
Each batch holds up to BATCH_N papers; each paper block:
  ===== R{row} {slug} =====
  T: title (from corpus)
  A: abstract (corpus, truncated 900)
  F: fulltext extract (front 16000 + tail 14000 chars from the TXT)

Usage: .venv\\Scripts\\python.exe scripts/make_lr4_code_extracts.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
TXT_DIR = os.path.join(ROOT, '04d_LR4', '3. fulltext L1', 'txt')
COD = os.path.join(SS, 'coding')
os.makedirs(COD, exist_ok=True)

sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from screening_data_lr4 import S4, decision  # noqa: E402

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}
INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')

cov = json.load(open(os.path.join(SS, 'coverage_lr4.json'), encoding='utf-8'))

BATCH_N = 6
FRONT = 16000
TAIL = 14000

blocks = []  # (row, text)
for r in INCLUDED:
    v = cov.get(str(r), {})
    txt = v.get('txt', '')
    if not txt or not os.path.exists(txt):
        txt = os.path.join(TXT_DIR, 'R%03d_%s.txt' % (r, BYROW[r]['slug']))
    if not os.path.exists(txt):
        continue
    t = open(txt, encoding='utf-8', errors='replace').read()
    t = re.sub(r'\s+', ' ', t).strip()
    blocks.append((r, t))

# clear old batches
for f in os.listdir(COD):
    os.remove(os.path.join(COD, f))

n_batches = (len(blocks) + BATCH_N - 1) // BATCH_N
for bi in range(n_batches):
    chunk = blocks[bi * BATCH_N:(bi + 1) * BATCH_N]
    lines = ['LR4 Step-3 coding batch %02d (papers %d-%d of %d)' % (
        bi + 1, bi * BATCH_N + 1, min((bi + 1) * BATCH_N, len(blocks)), len(blocks)), '']
    for r, t in chunk:
        rec = BYROW[r]
        extract = t[:FRONT]
        if len(t) > FRONT:
            extract += ' ... ' + t[-TAIL:]
        lines.append('===== R%03d %s =====' % (r, rec['slug']))
        lines.append('T: ' + rec['title'])
        lines.append('A: ' + rec['abstract'][:900])
        lines.append('DOI: ' + (rec['doi'] or ''))
        lines.append('F: ' + extract)
        lines.append('')
    with open(os.path.join(COD, 'batch%02d.txt' % (bi + 1)), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

print('papers with txt: %d | batches: %d -> %s' % (len(blocks), n_batches, COD))

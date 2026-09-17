# -*- coding: utf-8 -*-
"""Extract TXT companions for all staged LR4 PDFs in 04d_LR4/3. fulltext L1/.
Writes {name}.txt into .../txt/ (skips existing). Usage: python scripts/txt_lr4.py [n]
where n = optional cap on files processed (0 = all).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FT1 = os.path.join(ROOT, '04d_LR4', '3. fulltext L1')
TXT_DIR = os.path.join(FT1, 'txt')
os.makedirs(TXT_DIR, exist_ok=True)

from pypdf import PdfReader

cap = int(sys.argv[1]) if len(sys.argv) > 1 else 0
done = 0
for f in sorted(os.listdir(FT1)):
    if not f.lower().endswith('.pdf'):
        continue
    dst = os.path.join(TXT_DIR, f[:-4] + '.txt')
    if os.path.exists(dst) and os.path.getsize(dst) > 2000:
        continue
    try:
        r = PdfReader(os.path.join(FT1, f))
        parts = []
        for pg in r.pages:
            parts.append(pg.extract_text() or '')
        t = re.sub(r'[ \t]+', ' ', '\n'.join(parts))
        t = re.sub(r'\n{3,}', '\n\n', t)
        with open(dst, 'w', encoding='utf-8') as fh:
            fh.write(t[:60000])
        done += 1
        print('%s -> %d chars' % (f, len(t)))
    except Exception as e:
        print('%s FAIL %s' % (f, e))
    if cap and done >= cap:
        break
print('extracted %d' % done)

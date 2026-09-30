# -*- coding: utf-8 -*-
"""Extract TXT companions for all PDFs in 04d_LR4/4. fulltext L2/
Writes 4. fulltext L2/txt/{name}.txt (60k cap). Idempotent.
"""
import os
import re
import sys

from pypdf import PdfReader

ROOT = r'h:\phd\6.pjt\LR1\papers'
FT = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
TXT = os.path.join(FT, 'txt')
os.makedirs(TXT, exist_ok=True)

done = 0
for f in sorted(os.listdir(FT)):
    if not f.lower().endswith('.pdf'):
        continue
    dst = os.path.join(TXT, f[:-4] + '.txt')
    if os.path.exists(dst) and os.path.getsize(dst) > 2000:
        continue
    try:
        r = PdfReader(os.path.join(FT, f))
        parts = []
        for pg in r.pages:
            parts.append(pg.extract_text() or '')
        t = re.sub(r'[ \t]+', ' ', '\n'.join(parts))
        t = re.sub(r'\n{3,}', '\n\n', t)
        t = t.encode('utf-8', errors='replace').decode('utf-8')
        with open(dst, 'w', encoding='utf-8') as fh:
            fh.write(t[:60000])
        done += 1
    except Exception as e:
        print('%s FAIL %s' % (f, e))
print('extracted %d' % done)

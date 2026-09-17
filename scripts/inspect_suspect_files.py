# -*- coding: utf-8 -*-
"""Inspect the two suspicious staged files + expected metadata."""
import re, sys, os
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from pypdf import PdfReader

DIR = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'

t = open(RIS, encoding='utf-8', errors='replace').read()
for rid in ('3658', '3993', '3756'):
    m = re.search(r'(TY  - .*?ID  - %s.*?)(?=\nER  -|\Z)' % rid, t, re.S)
    print('=' * 90)
    print(m.group(0)[:600] if m else 'NOT FOUND in RIS')

for rid in ('3658', '3993'):
    base = None
    for f in os.listdir(DIR):
        if f.startswith(rid + '_'):
            base = os.path.splitext(f)[0]
    if base:
        txt = open(os.path.join(DIR, base + '.txt'), encoding='utf-8', errors='replace').read()
        print('=' * 90)
        print(rid, '| txt len', len(txt))
        print(txt[:1500].replace('\n', ' '))
        try:
            r = PdfReader(os.path.join(DIR, base + '.pdf'))
            print('--- PDF pages:', len(r.pages))
            p0 = r.pages[0].extract_text() or ''
            print('--- PDF page1:', p0[:900].replace('\n', ' '))
            # print metadata
            md = r.metadata
            print('--- PDF meta:', str(md)[:400])
        except Exception as e:
            print('--- pdf read error:', e)

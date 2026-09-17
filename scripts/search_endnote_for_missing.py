# -*- coding: utf-8 -*-
"""Search the Endnote library (folder + index) for 3756 and 3993 correct PDFs."""
import os, re, json, unicodedata

PDFROOT = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index_v2.json'

def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '', s.lower())

pat3756 = [norm(p) for p in ('work zone safety', 'multisensor fusion', 'proactive work zone', 'ahmad')]
pat3993 = [norm(p) for p in ('underground space', 'intelligent analysis of construction safety', 'large underground')]

# 1) index text search
idx = json.load(open(IDX, encoding='utf-8'))
for label, pats in (('3756', pat3756), ('3993', pat3993)):
    print('=' * 90)
    print(label, 'index hits:')
    hits = 0
    for k, v in idx.items():
        nf = norm(v.get('text', '')[:8000]) + norm(k)
        if all(p in nf for p in pats[:2]) or any(p in nf for p in pats[2:]):
            print('   ', k[:100])
            hits += 1
        if hits >= 15:
            break
    print('   (shown up to 15)')

# 2) filename search on disk
print('=' * 90)
for root, dirs, files in os.walk(PDFROOT):
    for f in files:
        nf = norm(f)
        if any(p in nf for p in pat3756) or any(p in nf for p in pat3993):
            print('FILE:', os.path.join(root, f))

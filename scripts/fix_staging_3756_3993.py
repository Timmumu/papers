# -*- coding: utf-8 -*-
"""Fix staging: add 3756 from Endnote, remove wrong 3993 pair."""
import os, shutil, re, unicodedata
from pypdf import PdfReader

DIR = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
SRC_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF\4127178497\Ahmad-2026-Lessons Learned from the Real-World.pdf'

def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', ' ', s.lower())

# ---- 1) stage 3756 from Endnote ----
out_pdf = os.path.join(DIR, '3756_Ahmad2026.pdf')
shutil.copy2(SRC_PDF, out_pdf)
r = PdfReader(out_pdf)
text = '\n'.join((p.extract_text() or '') for p in r.pages)
open(os.path.join(DIR, '3756_Ahmad2026.txt'), 'w', encoding='utf-8').write(text)
front = norm(text[:6000])
expect_words = ['lessons', 'learned', 'real-world', 'deployment', 'multisensor',
                'fusion', 'proactive', 'work', 'zone', 'safety']
missing_words = [w for w in expect_words if w not in front]
print('3756 pages:', len(r.pages), '| txt len:', len(text))
print('3756 front:', text[:400].replace('\n', ' '))
print('3756 title-word check missing:', missing_words)
print('3756 DOI present:', bool(re.search(r'10\.\d{4,9}/', text[:6000])))

# ---- 2) remove the wrong 3993 pair ----
removed = []
for ext in ('.pdf', '.txt'):
    p = os.path.join(DIR, '3993_Yu2024-underground' + ext)
    if os.path.exists(p):
        os.remove(p)
        removed.append(os.path.basename(p))
print('removed wrong 3993 files:', removed)

print('done.')

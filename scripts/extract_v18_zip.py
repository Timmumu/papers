# -*- coding: utf-8 -*-
"""Extract text + headings from docx without python-docx (zip + XML parse)."""
import re, zipfile
from xml.etree import ElementTree as ET

P = r'h:\phd\6.pjt\LR1\papers\05_article\SLR for CDT (v1.8 260906).docx'
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

z = zipfile.ZipFile(P)
xml = z.read('word/document.xml')
root = ET.fromstring(xml)

paras = []
for p in root.iter('{%s}p' % NS['w']):
    style = ''
    pPr = p.find('w:pPr', NS)
    if pPr is not None:
        ps = pPr.find('w:pStyle', NS)
        if ps is not None:
            style = ps.get('{%s}val' % NS['w']) or ''
    txt = ''.join(t.text or '' for t in p.iter('{%s}t' % NS['w']))
    paras.append((style, txt))

n_words = sum(len(re.findall(r'\w+', t)) for _, t in paras)
print('paragraphs:', len(paras), '| approx words:', n_words)

print('\n=== HEADINGS ===')
for s, t in paras:
    if ('Heading' in s or 'heading' in s or s in ('Title', 'Subtitle')) and t.strip():
        print('  [%s] %s' % (s, t.strip()[:130]))

print('\n=== FRONT (first 45 non-empty) ===')
c = 0
for s, t in paras:
    if t.strip():
        print('<%s> %s' % (s or '-', t.strip()[:280]))
        c += 1
        if c >= 45:
            break

out = r'h:\phd\6.pjt\LR1\papers\scripts\_v18_fulltext.txt'
with open(out, 'w', encoding='utf-8') as f:
    for s, t in paras:
        if t.strip():
            f.write('<%s> %s\n' % (s or '-', t.rstrip()))
print('\nfull text ->', out)

n_tables = 0
rows_per = []
for tbl in root.iter('{%s}tbl' % NS['w']):
    rows = tbl.findall('.//w:tr', NS)
    rows_per.append(len(rows))
    n_tables += 1
print('tables:', n_tables, '| rows each:', rows_per)

full = '\n'.join(t for _, t in paras)
probes = {
    'PRISMA': len(re.findall(r'PRISMA', full)),
    'n= counts': re.findall(r'\bn\s*=\s*[\d,]+', full)[:20],
    'has References heading': bool(re.search(r'(?im)^\s*(References|REFERENCES)\s*$', full)),
    'fusion depth': len(re.findall(r'fusion depth', full, re.I)),
    'Tier 4 / cognitive': len(re.findall(r'Tier 4|cognitive digital twin', full, re.I)),
    'Figure refs': len(re.findall(r'\bFig(?:ure)?\.\s*\d+', full)),
    'Table refs': len(re.findall(r'\bTable\s*\d+', full)),
    'limitations': len(re.findall(r'imitation', full, re.I)),
    'future work': len(re.findall(r'future (work|research)', full, re.I)),
    'placeholders': re.findall(r'(?i)\b(TODO|XXX|TBD|FIXME|placeholder|citation needed)\b', full),
    'word "we" count': len(re.findall(r'\b[Ww]e\b', full)),
}
print('\n=== PROBES ===')
for k, v in probes.items():
    print(' ', k, ':', v)

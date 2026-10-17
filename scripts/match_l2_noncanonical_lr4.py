# -*- coding: utf-8 -*-
"""Match noncanonical LR4 L2 PDFs to corpus rows by DOI/title evidence.

Writes a JSON/CSV report only. It does not rename files or change coding.
"""
import csv
import json
import os
import re
import sys

from pypdf import PdfReader

ROOT = r'h:\phd\6.pjt\LR1\papers'
L2 = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
OUT_JSON = os.path.join(SS, 'l2_noncanonical_matches.json')
OUT_CSV = os.path.join(SS, 'l2_noncanonical_matches.csv')

STOP = set('''a an and are as at based by for from in into is of on or the to using with
digital twin twins construction model models framework system study approach method data technology
management monitoring building buildings analysis simulation dynamic integration'''.split())


def norm(value):
    return re.sub(r'[^a-z0-9]', '', (value or '').lower())


def words(value):
    return [w for w in re.split(r'\W+', (value or '').lower()) if len(w) >= 4 and w not in STOP]


def extract_text(path):
    reader = PdfReader(path)
    parts = []
    for page in reader.pages[:4]:
        parts.append(page.extract_text() or '')
    return re.sub(r'\s+', ' ', ' '.join(parts)).strip()


def canonical_name(row, slug):
    safe = re.sub(r'[^A-Za-z0-9_.-]+', '-', slug).strip('-')[:70]
    return 'R%03d_%s.pdf' % (row, safe)


with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as fh:
    corpus = json.load(fh)

rows = []
for filename in sorted(os.listdir(L2)):
    if not filename.lower().endswith('.pdf'):
        continue
    if re.match(r'R\d{3}_.+\.pdf$', filename):
        continue
    path = os.path.join(L2, filename)
    try:
        text = extract_text(path)
        ntext = norm(text)
    except Exception as exc:
        rows.append({'file': filename, 'status': 'unreadable', 'error': str(exc)[:200]})
        continue

    scored = []
    for rec in corpus:
        doi = (rec.get('doi') or '').strip()
        doi_norm = norm(doi)
        doi_hit = bool(doi_norm and len(doi_norm) >= 10 and doi_norm in ntext)
        title_words = words(rec.get('title'))[:18]
        hits = [w for w in title_words if w in text.lower()]
        title_score = len(hits)
        title_ratio = title_score / float(len(title_words) or 1)
        if doi_hit or title_score >= 5:
            scored.append((doi_hit, title_score, title_ratio, rec, hits))
    scored.sort(key=lambda item: (item[0], item[1], item[2]), reverse=True)
    if not scored:
        rows.append({'file': filename, 'status': 'no-match', 'head': text[:300]})
        continue
    doi_hit, title_score, title_ratio, rec, hits = scored[0]
    status = 'doi-match' if doi_hit else ('title-match' if title_ratio >= 0.60 and title_score >= 5 else 'weak-title-match')
    rows.append({
        'file': filename,
        'status': status,
        'row': rec['row'],
        'slug': rec['slug'],
        'suggested_name': canonical_name(rec['row'], rec['slug']),
        'doi': rec.get('doi', ''),
        'title': rec.get('title', ''),
        'authors': rec.get('authors', ''),
        'year': rec.get('year', ''),
        'title_score': title_score,
        'title_ratio': round(title_ratio, 3),
        'matched_words': '; '.join(hits[:20]),
        'head': text[:300],
    })

with open(OUT_JSON, 'w', encoding='utf-8') as fh:
    json.dump(rows, fh, ensure_ascii=False, indent=1)

fieldnames = ['file', 'status', 'row', 'slug', 'suggested_name', 'doi', 'title', 'authors', 'year', 'title_score', 'title_ratio', 'matched_words', 'error']
with open(OUT_CSV, 'w', encoding='utf-8', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow({key: row.get(key, '') for key in fieldnames})

print('wrote', OUT_JSON)
print('wrote', OUT_CSV)
for row in rows:
    print('%s | %s | %s | %s | %s' % (
        row.get('file'), row.get('status'), row.get('row', ''), row.get('slug', ''), row.get('suggested_name', '')))
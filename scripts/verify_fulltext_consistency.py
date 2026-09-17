# -*- coding: utf-8 -*-
"""Verify fulltext staging consistency with the deep-reading records.

Checks:
  1. orphan staged files (rid not among the 429 screened records)
  2. missing staging (S3 papers with SRC=Endnote but no staged PDF)
  3. identity of every staged PDF (Endnote index front matter OR staged txt
     front matter must contain the paper's DOI or a strong title signature)
  4. PDF/txt pairing gaps
"""
import os, re, sys, json, unicodedata
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_data
from screening_data import S

DIR = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index_v2.json'

S3 = step3_data.S3

def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '', s.lower())

# ---------- RIS metadata ----------
txt_ris = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt_ris)
meta = {}
for n0, r in enumerate(recs, 1):
    if 'TY  -' not in r:
        continue
    m = re.search(r'^ID  - (.*?)$', r, re.M)
    rid = m.group(1).strip() if m else ''
    aus = [a.strip() for a in re.findall(r'^AU  - (.*)$', r, re.M)]
    ti = re.search(r'^TI  - (.*?)(?=^[A-Z0-9]{2}  - |\Z)', r, re.M | re.S)
    title = ' '.join(ti.group(1).split()) if ti else ''
    py = re.search(r'^PY  - (.*?)$', r, re.M)
    doi = re.search(r'^DO  - (.*?)$', r, re.M)
    meta[n0] = dict(rid=rid, title=title,
                    author=(aus[0] if aus else ''),
                    year=py.group(1).strip() if py else '',
                    doi=doi.group(1).strip() if doi else '')
rid2meta = {v['rid']: v for v in meta.values() if v['rid']}

idx = json.load(open(IDX, encoding='utf-8'))

# ---------- staged files ----------
files = os.listdir(DIR)
pdfs = sorted(f for f in files if f.lower().endswith('.pdf'))
txts = sorted(f for f in files if f.lower().endswith('.txt'))
staged = {}
for f in pdfs:
    m = re.match(r'^(\d{4})_', f)
    staged.setdefault(m.group(1) if m else '?', []).append(f)

print('staged PDFs:', len(pdfs), '| staged txts:', len(txts))
dups = {r: v for r, v in staged.items() if len(v) > 1}
print('rids with duplicate PDFs:', dups)

# orphan: rid not among 429
all_rids = set(rid2meta)
orphans = sorted((r, staged[r]) for r in staged if r not in all_rids)
print('ORPHANS (not among 429):', orphans)

# pairing
pdf_stems = {os.path.splitext(f)[0] for f in pdfs}
txt_stems = {os.path.splitext(f)[0] for f in txts}
print('txt without pdf:', sorted(txt_stems - pdf_stems))
print('pdf without txt:', sorted(pdf_stems - txt_stems))

# ---------- missing staging ----------
missing = []
for n in sorted(S3):
    rid = meta[n]['rid']
    src = S3[n][15] if len(S3[n]) > 15 else ''
    if rid not in staged:
        missing.append((n, rid, S[n][7], src, meta[n]['title'][:60]))
print('\nS3 papers without staged PDF:')
for t in missing:
    print('  ', t)

# ---------- identity check ----------
def sig(title):
    t = norm(title)
    return t[:60] if t else ''

bad = []
STOP = set('with and for the from based using into within their its this that under over across during digital twin twins twin twinning structural health safety construction of on in a an to by data models model modeling'.split())
def title_words(t):
    s = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return [w for w in re.findall(r'[a-z0-9]+', s.lower()) if len(w) >= 4 and w not in STOP]
for f in pdfs:
    rid = re.match(r'^(\d{4})_', f).group(1)
    exp = rid2meta.get(rid)
    if not exp:
        continue
    doi_n = norm(exp['doi']) if exp['doi'] else ''
    title_sig = sig(exp['title'])
    # source of front matter
    front = ''
    if f in idx:
        front = idx[f].get('text', '')
    elif os.path.splitext(f)[0] in txt_stems:
        tpath = os.path.join(DIR, os.path.splitext(f)[0] + '.txt')
        front = open(tpath, encoding='utf-8', errors='replace').read()[:8000]
    nf = norm(front)
    ok_doi = bool(doi_n and doi_n in nf)
    ok_title = bool(title_sig and title_sig in nf)
    tw = title_words(exp['title'])
    ok_words = bool(tw) and all(w in nf for w in tw)
    status = 'OK' if (ok_doi or ok_title or ok_words) else 'MISMATCH'
    why = 'doi' if ok_doi else ('title' if ok_title else ('title-words' if ok_words else 'neither'))
    if status == 'MISMATCH':
        bad.append((rid, f, exp['title'][:50], 'in_index=' + str(f in idx)))
    print('%-8s %-6s %s (%s)' % (rid, status, f[:60], why))
print('\nIDENTITY MISMATCHES:', len(bad))
for b in bad:
    print('  ', b)

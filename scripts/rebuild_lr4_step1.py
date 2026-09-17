# -*- coding: utf-8 -*-
"""LR4 Step-1 rebuild:
  - 04d_LR4/SLR summary matrix step 1.md  (04c column order, header with counts)
  - 01_source_4th_SLR/{slug}.md            (per-paper derivative notes, all 956)
Authoritative stores: corpus_lr4.json + screening_data_lr4.S4.
Run from repo root; idempotent.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
OUT_MD = os.path.join(ROOT, '04d_LR4', 'SLR summary matrix step 1.md')
SRC_NOTES = os.path.join(ROOT, '01_source_4th_SLR')
os.makedirs(SRC_NOTES, exist_ok=True)

import sys
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from screening_data_lr4 import S4, decision  # noqa: E402

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}
assert len(BYROW) == 956


def authors_disp(aus):
    parts = [p.strip() for p in (aus or '').split(';') if p.strip()]
    if not parts:
        return 'Anon.'
    first = parts[0]
    if ',' in first:
        seg = first.split(',')[0].strip()
        ini = first.split(',', 1)[1].strip()
        nm = seg + (', ' + ini if ini else '')
    else:
        toks = [t for t in re.split(r'[\s,]+', first) if t]
        last = toks[-1] if toks else ''
        last_core = last.rstrip('.')
        if last != last_core or INITIAL_RE.match(last_core):
            nm = (toks[-2] if len(toks) >= 2 else last_core) + ', ' + last_core
        else:
            nm = last.rstrip('.')
    if len(parts) > 1:
        nm += ' et al.'
    return nm


def md_escape(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ')


INITIAL_RE = re.compile(r'^[A-Za-z][A-Za-z]?\.?$')


def clean(s):
    return re.sub(r'\s+', ' ', s or '').strip()


# ---------------- Step-1 matrix ----------------
inc_rows = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')
exc_rows = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Exclude')
flags = {r: t[:5] for r, t in S4.items()}
notes = {r: t[5] for r, t in S4.items()}

L = []
L.append('# SLR Summary Matrix — Step 1 Screening (956 papers)')
L.append('')
L.append('Review: *A Self-Improving Cognitive Digital Twin for Design-for-Safety and '
         'Design-for-Quality in the Built Environment.*')
L.append('Screening follows Prompt A (title/abstract screening, columns G–K) of the 04c '
         '`2 stage PRISMA guideline.md`, reused for 04d_LR4.')
L.append('**Step-1 decision rule:** Include only if G–K are all "Yes". Conservative: unsure → "No".')
L.append('**Result: %d Include / %d Exclude** (out of 956; corpus '
         '`0.1a.Corpus_Merged-956 nos. v2.csv`).' % (len(inc_rows), len(exc_rows)))
L.append('')
L.append('| ID | Author | Title | Year | Source | G | H | I | J | K | Decision | Note | DOI |')
L.append('| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
for r in sorted(BYROW):
    rec = BYROW[r]
    f = flags[r]
    d = decision(f)
    L.append('| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        r,
        md_escape(authors_disp(rec['authors'])),
        md_escape(rec['title']),
        rec['year'],
        'Scopus' if rec['db'].lower().startswith('scopus') else 'Web of Science',
        f[0], f[1], f[2], f[3], f[4],
        '**Include**' if d == 'Include' else 'Exclude',
        md_escape(notes[r]),
        rec['doi'] or ''))
L.append('')
L.append('---')
L.append('')
L.append('## Include list (%d)' % len(inc_rows))
L.append('')
for r in inc_rows:
    rec = BYROW[r]
    L.append('- R%03d | %s | %s (%s) | DOI: %s' % (
        r, rec['slug'], md_escape(rec['title']), rec['year'], rec['doi'] or '-'))
L.append('')
with open(OUT_MD, 'w', encoding='utf-8') as f:
    f.write('\n'.join(L))
print('matrix written: %s' % OUT_MD)
print('includes=%d excludes=%d' % (len(inc_rows), len(exc_rows)))

# ---------------- per-paper notes ----------------
# clean stale notes (slug set may have changed)
valid = {rec['slug'] + '.md' for rec in CORPUS}
removed = 0
for fp in os.listdir(SRC_NOTES):
    if fp.endswith('.md') and fp not in valid:
        os.remove(os.path.join(SRC_NOTES, fp))
        removed += 1
if removed:
    print('removed stale notes: %d' % removed)

for r in sorted(BYROW):
    rec = BYROW[r]
    f = flags[r]
    d = decision(f)
    ab = clean(rec['abstract'])
    ab_sum = (ab[:900] + '…') if len(ab) > 900 else ab
    au = authors_disp(rec['authors'])
    N = []
    N.append('# %s (%s) — %s' % (au, rec['year'], rec['title']))
    N.append('')
    N.append('- **ID:** R%03d | **Source:** %s | **DOI:** %s' % (
        r, 'Scopus' if rec['db'].lower().startswith('scopus') else 'Web of Science',
        rec['doi'] or 'N/A'))
    N.append('- **Journal:** %s' % rec['journal'])
    N.append('- **Authors:** %s' % clean(rec['authors']))
    N.append('')
    N.append('## Abstract summary')
    N.append(ab_sum if ab_sum else '(no abstract)')
    N.append('')
    N.append('## Step-1 Screening (Prompt A)')
    N.append('| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |')
    N.append('|---|---|---|---|---|---|')
    N.append('| %s | %s | %s | %s | %s | **%s** |' % (f[0], f[1], f[2], f[3], f[4], d))
    N.append('')
    N.append('**Note:** %s' % notes[r])
    N.append('')
    with open(os.path.join(SRC_NOTES, rec['slug'] + '.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(N))

print('notes written: %d -> %s' % (len(BYROW), SRC_NOTES))

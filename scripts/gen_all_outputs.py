"""Rebuild SLR summary matrix + all 429 atomic notes from screening_data.py."""
import re, os, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

SRC = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
OUTDIR = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'
MATRIX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md'
os.makedirs(OUTDIR, exist_ok=True)

txt = open(SRC, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)

papers = {}  # n -> dict
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''
    aus = re.findall(r'^AU  - (.*)$', r, re.M)
    db = field('DB')
    papers[n] = dict(
        rid=field('ID'), ti=field('TI'), ab=field('AB'),
        src=db if db else ('Web of Science' if 'WOS:' in r else 'Lens.org'),
        aus=aus, py=field('PY'), do=field('DO'), t2=field('T2'))

assert len(papers) == 429, f'expected 429, got {len(papers)}'
assert set(S.keys()) == set(range(1, 430)), 'screening data keys mismatch'

# ---- atomic notes ----
for n, p in papers.items():
    g, h, i, j, k, dec, note, slug = S[n]
    au_str = '; '.join(p['aus'])
    first_au = p['aus'][0].split(',')[0] if p['aus'] else 'Unknown'
    ab = p['ab']
    ab_short = ab[:900] + ('…' if len(ab) > 900 else '')
    md = f"""# {first_au} et al. ({p['py']}) — {p['ti']}

- **ID:** {p['rid']} | **Source:** {p['src']} | **DOI:** {p['do'] or 'n/a'}
- **Journal:** {p['t2']}
- **Authors:** {au_str}

## Abstract summary
{ab_short}

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| {g} | {h} | {i} | {j} | {k} | **{dec}** |

**Note:** {note}
"""
    with open(os.path.join(OUTDIR, slug + '.md'), 'w', encoding='utf-8') as f:
        f.write(md)

# ---- summary matrix ----
inc = [n for n in range(1, 430) if S[n][5] == 'Include']
lines = []
lines.append('# SLR Summary Matrix — 3rd Round (429 papers)\n')
lines.append('Review: *A Self-Improving Cognitive Digital Twin for Design-for-Safety and Design-for-Quality in the Built Environment.*')
lines.append('Screening follows `2 stage PRISMA guideline.md` — Prompt A (Step 1, title/abstract screening, columns G–K).')
lines.append('Data source: `429 papers.txt` (Endnote RIS export; Scopus / Web of Science / Lens.org).\n')
lines.append('**Step-1 decision rule:** Include only if G–K are all "Yes". Conservative: unsure → "No".\n')
lines.append(f'**Result: {len(inc)} Include / {429-len(inc)} Exclude** (incl. 6 cross-database duplicates excluded)\n')
lines.append('## Step 1 Screening — all 429 papers\n')
lines.append('| # | ID | Source | Title (short) | G | H | I | J | K | Decision | Note |')
lines.append('|---|---|---|---|---|---|---|---|---|---|---|')
for n in range(1, 430):
    p = papers[n]
    g, h, i, j, k, dec, note, slug = S[n]
    ti = p['ti']
    ti_short = ti[:70] + ('…' if len(ti) > 70 else '')
    ti_short = ti_short.replace('|', '\\|')
    note_md = note.replace('|', '\\|')
    dec_md = f'**{dec}**' if dec == 'Include' else dec
    lines.append(f'| {n} | {p["rid"]} | {p["src"]} | {ti_short} | {g} | {h} | {i} | {j} | {k} | {dec_md} | {note_md} |')

lines.append('\n## Included papers (proceed to Step 3 full-text coding)\n')
lines.append('| # | ID | Slug (atomic note) |')
lines.append('|---|---|---|')
for n in inc:
    lines.append(f'| {n} | {papers[n]["rid"]} | `{S[n][7]}.md` |')

lines.append('\n## Step 3 Deep-Read Coding (pending full text)\n')
lines.append('| ID | P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF | AG |')
lines.append('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for n in inc:
    lines.append(f'| {papers[n]["rid"]} | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Awaiting full text |')

open(MATRIX, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print(f'notes written: 429 | matrix rows: 429 | included: {len(inc)}')

"""Map the 165 included papers to Endnote-attached PDFs.

Strategy: for each included paper (from screening_data.S), search Endnote PDF folder
for a file whose name contains first-author surname + year. Copy matches to the
fulltext staging folder named '{ID}_{slug}.pdf'. Report found / not-found / ambiguous.
"""
import os, re, sys, shutil
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'

# --- parse RIS for per-index metadata ---
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
meta = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''
    aus = re.findall(r'^AU  - (.*)$', r, re.M)
    first = aus[0].split(',')[0].strip() if aus else ''
    meta[n] = dict(rid=field('ID'), first=first, py=field('PY'), ti=field('TI'))

# --- build Endnote index (filename lower) ---
en_files = []
for root, _, files in os.walk(EN_PDF):
    for f in files:
        if f.lower().endswith('.pdf'):
            en_files.append((os.path.join(root, f), os.path.basename(f)))

def en_lookup(first, py, ti):
    """Return (path, certainty). certainty: 'exact' | 'guess' | None"""
    base = first.lower()
    cands = []
    for path, fname in en_files:
        low = fname.lower()
        # surname at start of filename (Endnote format: Author-Year-Title)
        if not low.startswith(base):
            # allow 'van ' prefixes etc. by 'in'
            if base not in low.split('-')[0]:
                continue
        if py and py not in fname:
            continue
        cands.append((path, fname))
    if not cands:
        return None
    # prefer strongest title keyword overlap
    words = [w for w in re.split(r'\W+', ti.lower()) if len(w) > 4 and w not in ('digital', 'twin', 'twins', 'construction', 'based', 'using', 'model', 'models', 'framework', 'system', 'review', 'study', 'analysis', 'applications', 'application', 'management', 'monitoring')]
    best = cands[0]
    best_score = -1
    for path, fname in cands:
        low = fname.lower()
        score = sum(1 for w in words if w in low)
        if score > best_score:
            best_score, best = score, (path, fname)
    return (best, 'exact' if best_score > 0 or len(cands) == 1 else 'guess')

included = [n for n in range(1, 430) if S[n][5] == 'Include']
found, missing = [], []
for n in included:
    slug = S[n][7]
    m = meta[n]
    out = os.path.join(FT, f"{m['rid']}_{slug}.pdf")
    if os.path.exists(out):  # already have full text
        found.append((n, m['rid'], slug, out, 'have'))
        continue
    res = en_lookup(m['first'], m['py'], m['ti'])
    if res:
        path, cert = res
        shutil.copy2(path[0] if isinstance(path, tuple) else path, out)
        found.append((n, m['rid'], slug, out, cert))
    else:
        missing.append((n, m['rid'], slug, m['first'], m['py'], m['ti']))

print('=== FOUND (copied from Endnote) ===')
for n, rid, slug, out, cert in found:
    print(f'#{n} [{rid}] {slug} [{cert}]')
print(f'\nfound total: {len(found)}')
print('\n=== MISSING in Endnote ===')
for n, rid, slug, first, py, ti in missing:
    print(f'#{n} [{rid}] {slug} | {first} {py} | {ti[:60]}')
print(f'\nmissing total: {len(missing)}')

"""Build the FINAL honest coverage report.

Reconciles:
  A. definitive verified list from verify_fulltext_final.py logic (34 incl. 3924 corrigendum)
  B. new found_verified from coverage re-match (first pass, 23)
  C. new found_verified from strict resolution (second pass, 17)

Checks for overlaps/double-counting and produces a clean per-paper status table:
  FOUND-ENDNOTE   = full text confirmed in Endnote (verified by DOI/title)
  UNVERIFIED-CAND = a candidate file exists but could not be positively verified
  ABSENT          = no reliable full text in Endnote

Output: ss/final_coverage_report.txt
"""
import os, re, sys, json
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
MATCH = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\coverage_match.json'
FINAL = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\coverage_final.json'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\final_coverage_report.txt'

# --- parse RIS ---
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
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=field('DO').lower())

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

# --- A: definitive verified (recompute verify_fulltext_final logic) ---
CORRIGENDA = {'3924'}
def verify(path, doi, ti_full):
    try:
        c = open(path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False
    if len(c) < 4000:
        return False
    cn = norm(c)
    if doi.startswith('10.') and doi in c[:4500]:
        return True
    if len(ti_full) >= 40 and ti_full in cn[:4000]:
        return True
    return False

included = [n for n in range(1, 430) if S[n][5] == 'Include']
definitive_found = {}   # rid -> file
for n in included:
    rid = meta[n]['rid']
    if rid in CORRIGENDA:
        continue
    slug = S[n][7]
    f = os.path.join(FT, rid + '_' + slug + '.txt')
    if os.path.exists(f) and verify(f, meta[n]['doi'], norm(meta[n]['ti'])):
        definitive_found[rid] = rid + '_' + slug + '.txt'

# --- B/C: new finds from the two passes ---
match = json.load(open(MATCH, encoding='utf-8'))
final = json.load(open(FINAL, encoding='utf-8'))
new_found = {}
for rid, v in match.items():
    if v['status'] == 'found_verified':
        new_found[rid] = v['file']
for rid, v in final.items():
    if v['status'] == 'found_verified':
        new_found[rid] = v['file']

# remove overlaps with definitive
new_found = {r: f for r, f in new_found.items() if r not in definitive_found}

# --- unresolved from final pass ---
unverified = {}
for rid, v in final.items():
    if v['status'] == 'unverified':
        unverified[rid] = v.get('endnote_file', '?')

# --- build final status per paper ---
status = {}
for n in included:
    rid = meta[n]['rid']
    if rid in definitive_found:
        status[rid] = ('FOUND-ENDNOTE', definitive_found[rid], 'definitive')
    elif rid in new_found:
        status[rid] = ('FOUND-ENDNOTE', new_found[rid], 'new')
    elif rid in unverified:
        status[rid] = ('UNVERIFIED-CAND', unverified[rid], 'candidate')
    else:
        status[rid] = ('ABSENT', '', '')

lines = []
lines.append('=== FINAL ENDNOTE COVERAGE (165 included papers) ===')
lines.append('')
counts = {}
for rid, (st, fn, src) in sorted(status.items()):
    counts[st] = counts.get(st, 0) + 1
lines.append('FOUND-ENDNOTE: %d | UNVERIFIED-CAND: %d | ABSENT: %d' % (
    counts.get('FOUND-ENDNOTE', 0), counts.get('UNVERIFIED-CAND', 0), counts.get('ABSENT', 0)))
lines.append('')
lines.append('=== FOUND IN ENDNOTE (full text verified) ===')
for n in included:
    rid = meta[n]['rid']
    if status[rid][0] == 'FOUND-ENDNOTE':
        lines.append('FOUND  [%s] %-40s <- %s  (%s)' % (rid, S[n][7], status[rid][1], status[rid][2]))
lines.append('')
lines.append('=== UNVERIFIED CANDIDATE (file exists, identity not confirmed) ===')
for n in included:
    rid = meta[n]['rid']
    if status[rid][0] == 'UNVERIFIED-CAND':
        lines.append('UNVER  [%s] %-40s <- %s' % (rid, S[n][7], status[rid][1]))
lines.append('')
lines.append('=== ABSENT (no reliable full text in Endnote) ===')
for n in included:
    rid = meta[n]['rid']
    if status[rid][0] == 'ABSENT':
        lines.append('ABSENT [%s] %s' % (rid, S[n][7]))

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines[:15]))
print('...')
print('full report at', OUT)

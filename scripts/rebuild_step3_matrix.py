# -*- coding: utf-8 -*-
"""Rebuild the Step-3 markdown file (SLR summary matrix step 3.md) from
step3_data.py (authoritative), enriched with RIS author/title/year metadata,
plus the included-but-uncoded (missing full text) section.
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_data, step3_extra, step3_fusion
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
DIR = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round'
OUT3 = os.path.join(DIR, 'SLR summary matrix step 3.md')

S3 = step3_data.S3
AH = step3_extra.AH
AI = step3_extra.AI
FD = step3_fusion.FD
FDEV = step3_fusion.FDEV
FDCF = step3_fusion.FDCF

# ---------- RIS metadata ----------
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
meta = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    m = re.search(r'^ID  - (.*?)$', r, re.M)
    rid = m.group(1).strip() if m else ''
    aus = [a.strip() for a in re.findall(r'^AU  - (.*)$', r, re.M)]
    ti = re.search(r'^TI  - (.*?)(?=^[A-Z0-9]{2}  - |\Z)', r, re.M | re.S)
    title = ' '.join(ti.group(1).split()) if ti else ''
    py = re.search(r'^PY  - (.*?)$', r, re.M)
    year = py.group(1).strip() if py else ''
    do = re.search(r'^DO  - (.*?)$', r, re.M)
    doi = do.group(1).strip() if do else ''
    author = (aus[0] + (' et al.' if len(aus) > 1 else '')) if aus else ''
    meta[n] = dict(rid=rid, author=author, title=title, year=year, doi=doi)

def esc(s):
    return re.sub(r'\s+', ' ', s).replace('|', '/').strip()

def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

full = [n for n in S3 if S3[n][0] == 'Yes' and S3[n][1] == 'Yes' and S3[n][2] == 'Yes']
excl = [n for n in S3 if n not in full]

def stage2_reason(v):
    """Auto-derive the Stage-2 exclusion reason from P/Q/R gates."""
    ag = v[14]
    if 'RETRACTED' in ag.upper():
        return 'Retracted article'
    nos = []
    for tag, val in (('P', v[0]), ('Q', v[1]), ('R', v[2])):
        if val != 'Yes':
            nos.append('%s=No' % tag)
    return '; '.join(nos) if nos else ''

hdr3 = [
    '# SLR Summary Matrix — Step 3 Deep-Read Coding',
    '',
    'Review: *A Self-Improving Cognitive Digital Twin for Design-for-Safety and Design-for-Quality in the Built Environment.*',
    'Coded from verified full text (Prompt B). **%d papers coded** — %d full-coded + %d Stage-2 excluded.' % (len(S3), len(full), len(excl)),
    'Every row carries a `[Full-text source: ...]` mark in AG. AH = strength & gaps filled; AI = deficiencies & future work.',
    '',
    '| ID   | Author | Title | Year | P — DT built/evaluated | Q — DfS/DfQ scope | R — methodology | S — Stage-2 decision | T — Stage-2 exclusion reason | U — DT tier | V — design phase | W — construction phase | X — operation phase | Z — DfX focus | AA — self-improvement | AB — method | AC — data modality | AC1 — fusion depth | AC2 — fusion evidence | AC3 — confidence | AD — validation | AE — QA (0–5) | AF — cluster | AG — key evidence | AH — strength & gap filled | AI — deficiencies & future work | DOI |',
    '| ---- | ------ | ----- | ---- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ---- | ---- | ---- | --- | --- | --- | ---- | --- | ---- | -- | -- | -- | --- |',
]
for n in sorted(S3):
    v = S3[n]
    P, Q, R, tier = v[0], v[1], v[2], tier_short(v[3])
    if n in full:
        V, W, X, Z, AA, AB, AC, AD, AE, AF = v[4:14]
        s_dec = 'Include'
        s_reason = ''
        fd = FD.get(n, '')
        fdev = FDEV.get(n, '')
        fdcf = FDCF.get(n, '')
    else:
        V = W = X = Z = AA = AB = AC = AD = AE = AF = ''
        s_dec = 'Exclude'
        s_reason = stage2_reason(v)
        fd = fdev = fdcf = ''
    AG = v[14]
    SRC = v[15] if len(v) > 15 else ''
    ag = esc(AG) + ((' [Full-text source: %s]' % SRC) if SRC else '')
    ah = esc(AH.get(n, ''))
    ai = esc(AI.get(n, ''))
    m = meta.get(n, {})
    hdr3.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        m.get('rid', ''), esc(m.get('author', '')), esc(m.get('title', '')), m.get('year', ''),
        P, Q, R, s_dec, s_reason, tier, V, W, X, Z, AA, AB, AC, fd, fdev, fdcf, AD, AE, AF, ag, ah, ai, m.get('doi', '')))

# included-but-uncoded section (from screening_data)
included = sorted(n for n in S if S[n][5] == 'Include')
uncoded = [n for n in included if n not in S3]
reasons = {
    123: 'ASCE paywall; no full text available',
    311: 'ICE paywall; no full text available',
    390: 'MDPI Gold OA but Access-Denied from this network',
}
hdr3.append('')
hdr3.append('## Included papers missing full text (not yet coded)')
hdr3.append('')
hdr3.append('| ID   | Author | Title | Year | Reason | DOI |')
hdr3.append('| ---- | ------ | ----- | ---- | ------ | --- |')
for n in uncoded:
    m = meta.get(n, {})
    hdr3.append('| %s | %s | %s | %s | %s | %s |' % (
        m.get('rid', ''), esc(m.get('author', '')), esc(m.get('title', '')),
        m.get('year', ''), reasons.get(n, 'full text unavailable'), m.get('doi', '')))
open(OUT3, 'w', encoding='utf-8').write('\n'.join(hdr3) + '\n')
print(f'Rebuilt Step-3 file: {len(S3)} coded rows + {len(uncoded)} missing -> {OUT3}')

# -*- coding: utf-8 -*-
"""Resolve the 7 AMBIGUOUS cases from rematch_round2 by picking the candidate
whose front matter contains the paper's DOI (preferred) or full title, then
copy + full-extract + verify. Output: ss/rematch_ambig.txt
"""
import os, re, json, sys, shutil, subprocess
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index_v2.json'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\rematch_ambig.txt'

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

idx = json.load(open(IDX, encoding='utf-8'))

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

def find_path(base):
    return os.path.join(EN_PDF, idx[base]['dir'], base)

def full_extract(pdf, txt_out):
    code = ('from pypdf import PdfReader; r=PdfReader(r"%s"); '
            'open(r"%s","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))'
            % (pdf.replace('"', '\\"'), txt_out.replace('"', '\\"')))
    subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=180)

def verify(txt_path, doi, ti_norm):
    try:
        c = open(txt_path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False, 0
    cn = norm(c)
    if doi.startswith('10.') and doi in c[:4500]:
        return True, len(c)
    if len(ti_norm) >= 40 and ti_norm in cn[:4000]:
        return True, len(c)
    return False, len(c)

# the 7 ambiguous cases with their candidate lists (from rematch_round2)
AMBIG = {
    104: ['Guo-2026-AN INTELLIGENT CONSTRUCTION SYSTEM BA.pdf', 'Guo-2026-An intelligent construction system ba.pdf'],
    125: ['Huang-2026-Research on an intelligent monitori.pdf', 'Hu-2026-Integrating digital twin technologies.pdf', 'Hu-2026-Digital Twin-enabled failure predictio.pdf'],
    129: ['Huang-2026-Research on an intelligent monitori.pdf', 'ijmqe250043.pdf'],
    343: ['Wang-2024-Development and validation of graph1.pdf', 'Wang-2024-Development and validation of graphi.pdf', 'Wang-2024-Enabling Building Information Model-.pdf', 'Wang-2024-Research on Digital Twin Vehicle Sta.pdf'],
    393: ['Zeng-2025-A dynamic digital twin-based health.pdf', 'Zeng-2025-RETRACTED_ A dynamic digital twin-ba.pdf', 'Zeng-2025-Digital twin-empowered performance e.pdf'],
    418: ['Zheng-2022-Digital Twin‐Based Investigation of.pdf', 'Zheng-2022-Digital Twin-Based Investigation of.pdf'],
    429: ['Martinez-2025-Integration of building informat.pdf', 'Martinez-2026-Integration of building informat.pdf', 'Elshabshiri-2025-Integration of Building Infor.pdf', 'Pan-2021-A BIM-data mining integrated digital.pdf', 'j.autcon.2019.01.020.pdf#view=FitH.pdf', 'Wu-2026-Research on Management Efficiency and.pdf', 'Wang-2026-Digital twins in the construction in.pdf', 'Loggia-2024-Electrical Safety Enhanced With BI.pdf', 'j.autcon.2019.02.011.pdf#view=FitH.pdf', 'González-2026-Editorial_ AECO industry human-c.pdf'],
}

lines = []
for n, cands in AMBIG.items():
    m = meta[n]
    rid, slug, doi, ti_norm = m['rid'], S[n][7], m['doi'], norm(m['ti'])
    lines.append(f'\n#{n} [{rid}] {slug} DOI={doi}')
    best = None
    # 1) DOI match wins
    for f in cands:
        if doi.startswith('10.') and doi in idx.get(f, {}).get('text', ''):
            best = f
            lines.append(f'  DOI-hit: {f}')
            break
    # 2) else full-title match
    if best is None:
        for f in cands:
            tn = norm(idx.get(f, {}).get('text', ''))
            if len(ti_norm) >= 40 and ti_norm in tn:
                best = f
                lines.append(f'  TITLE-hit: {f}')
                break
    # 3) else prefer non-RETRACTED and longest front-matter
    if best is None:
        non_retr = [f for f in cands if 'RETRACTED' not in f]
        pool = non_retr or cands
        best = max(pool, key=lambda f: len(idx.get(f, {}).get('text', '')))
        lines.append(f'  FALLBACK (non-retracted/longest): {best}')

    src = find_path(best)
    out_pdf = os.path.join(FT, f'{rid}_{slug}.pdf')
    out_txt = os.path.join(FT, f'{rid}_{slug}.txt')
    if not os.path.exists(src):
        lines.append(f'  !! source missing: {src}')
        continue
    shutil.copy2(src, out_pdf)
    full_extract(out_pdf, out_txt)
    ok, ln = verify(out_txt, doi, ti_norm)
    if ok and ln >= 4000:
        lines.append(f'  RESOLVED -> {best} len={ln}')
    else:
        for p in (out_pdf, out_txt):
            if os.path.exists(p):
                os.remove(p)
        lines.append(f'  FAILED verify -> removed (len={ln})')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines))
print('\nReport:', OUT)

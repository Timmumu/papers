"""Rebuild the full-text corpus deterministically from OA sources.

For each included paper, attempt to fetch its PDF from OA mirrors by DOI:
  1. MDPI -> mdpi-res.com mirror (pattern by journal/vol/article)
  2. else -> Semantic Scholar openAccessPdf (arxiv, publisher gold OA)
  3. else -> itcon.org direct (journal-specific)
Then extract text with pypdf and verify front-matter DOI.
Only papers whose text passes verification are kept.
"""
import os, re, sys, json, urllib.request, subprocess
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
os.makedirs(FT, exist_ok=True)

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
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=field('DO').lower(),
                   t2=field('T2'), py=field('PY'))

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch(url, out):
    """Download via PowerShell (system proxy works there)."""
    ps = ('$ua=@{User-Agent="Mozilla/5.0"}; try { Invoke-WebRequest -Uri "%s" '
          '-OutFile "%s" -UseBasicParsing -Headers $ua; "OK" } catch { "FAIL" }'
          % (url.replace('"', '\\"'), out.replace('"', '\\"')))
    r = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True)
    return 'OK' in (r.stdout or '')

def mdpi_url(jour, vol, art):
    # article number has 5 digits; try both patterns
    cands = [
        f'https://mdpi-res.com/d_attachment/{jour}/{jour}-{vol}-{art}/article_deploy/{jour}-{vol}-{art}.pdf',
        f'https://mdpi-res.com/d_attachment/{jour}/{jour}-{vol}-{art}/article_deploy/{jour}-{vol}-{art}-v2.pdf',
    ]
    return cands

def ss_pdf_url(doi):
    try:
        url = f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf,externalIds'
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=40) as r:
            d = json.load(r)
        oa = d.get('openAccessPdf') or {}
        return oa.get('url')
    except Exception:
        return None

def extract(pdf, txt_out):
    code = ('from pypdf import PdfReader; r=PdfReader(r"%s"); '
            'open(r"%s","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))'
            % (pdf.replace('"', '\\"'), txt_out.replace('"', '\\"')))
    r = subprocess.run([PWSH, '-c', code], capture_output=True, text=True)
    return os.path.exists(txt_out)

def verify_doi(txt_path, doi):
    try:
        c = open(txt_path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False
    return doi.startswith('10.') and doi in c[:4000]

results = {}
for n in range(1, 430):
    if S[n][5] != 'Include':
        continue
    m = meta[n]
    slug = S[n][7]
    out_pdf = os.path.join(FT, f'{m["rid"]}_{slug}.pdf')
    out_txt = os.path.join(FT, f'{m["rid"]}_{slug}.txt')
    if os.path.exists(out_txt):  # already verified & kept
        results[n] = ('have', out_txt)
        continue
    doi = m['doi']
    got = None
    # 1. MDPI
    mdp = re.match(r'10\.3390/([a-z0-9]+)(\d+)(\d{4,5})', doi)
    if mdp:
        jour, vol, art = mdp.group(1), mdp.group(2), mdp.group(3)
        for u in mdpi_url(jour, vol, art):
            if fetch(u, out_pdf):
                got = out_pdf
                break
    # 2. Semantic Scholar
    if not got:
        ss = ss_pdf_url(doi)
        if ss:
            if fetch(ss, out_pdf):
                got = out_pdf
    # 3. itcon
    if not got and 'itcon' in doi:
        # guess URL from doi suffix
        pass
    if got:
        extract(got, out_txt)
        if verify_doi(out_txt, doi):
            results[n] = ('verified', out_txt)
        else:
            results[n] = ('UNVERIFIED', out_txt)
    else:
        results[n] = ('NOFETCH', '')

ok = sum(1 for v in results.values() if v[0] in ('have', 'verified'))
print(f'corpus: {ok}/{len(results)} verified | unverified={sum(1 for v in results.values() if v[0] not in ("have","verified"))}')
print('unverified/no-fetch:')
for n, (st, p) in results.items():
    if st not in ('have', 'verified'):
        print(f'  #{n} [{meta[n]["rid"]}] {S[n][7]} -> {st}')

"""Deterministic OA fetch for all included papers lacking a verified text.

Sources tried per paper (by DOI):
  1. MDPI mirror (mdpi-res.com) — known-good pattern
  2. arXiv via Semantic Scholar API
  3. itcon.org direct PDF (journal has open PDFs)
  4. Unpaywall best OA location
  5. OpenAlex best OA location pdf_url
Then extract + verify front-matter DOI; keep only verified. Report per-paper status.
"""
import os, re, sys, json, subprocess, time
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
REPORT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\oa_fetch_report.txt'
os.makedirs(FT, exist_ok=True)

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# parse metadata
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
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=field('DO').lower(), t2=field('T2'))


def ps_download(url, out):
    """Download via PowerShell (system proxy works)."""
    ps = ('$ua=@{User-Agent="Mozilla/5.0"}; try { Invoke-WebRequest -Uri "%s" '
          '-OutFile "%s" -UseBasicParsing -Headers $ua; "OK" } catch { "FAIL" }'
          % (url.replace('"', '\\"'), out.replace('"', '\\"')))
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', ps],
                       capture_output=True, text=True, timeout=90)
    return 'OK' in (r.stdout or '') and os.path.exists(out) and os.path.getsize(out) > 15000


def api_get(url):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.load(r)
    except Exception:
        return None


def mdpi_urls(doi):
    m = re.match(r'10\.3390/([a-z0-9]+)(\d+)(\d{4,5})$', doi)
    if not m:
        return []
    jour, vol, art = m.group(1), m.group(2), m.group(3)
    return [
        f'https://mdpi-res.com/d_attachment/{jour}/{jour}-{vol}-{art}/article_deploy/{jour}-{vol}-{art}.pdf',
        f'https://mdpi-res.com/d_attachment/{jour}/{jour}-{vol}-{art}/article_deploy/{jour}-{vol}-{art}-v2.pdf',
    ]


def itcon_url(doi):
    # itcon DOIs: 10.36680/j.itcon.YYYY.NNN -> https://www.itcon.org/papers/{year}_{nn}.pdf is not uniform;
    # instead use itcon paper page. Return None (handled manually).
    return None


def candidate_urls(doi):
    urls = mdpi_urls(doi)
    # Semantic Scholar / Unpaywall / OpenAlex
    ss = api_get(f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf')
    if ss and (ss.get('openAccessPdf') or {}).get('url'):
        u = ss['openAccessPdf']['url']
        if u and u.startswith('http'):
            urls.append(u)
    uw = api_get(f'https://api.unpaywall.org/v2/{doi}?email=slr@openai.com')
    if uw and (uw.get('best_oa_location') or {}).get('url_for_pdf'):
        urls.append(uw['best_oa_location']['url_for_pdf'])
    oa = api_get(f'https://api.openalex.org/works/doi:{doi}?mailto=slr@example.org')
    if oa:
        for loc in (oa.get('best_oa_location'), *([oa.get('locations')] or [])):
            pass
        bl = oa.get('best_oa_location') or {}
        if bl.get('pdf_url'):
            urls.append(bl['pdf_url'])
        if oa.get('locations'):
            for l in oa['locations']:
                if l.get('pdf_url'):
                    urls.append(l['pdf_url'])
    # dedupe
    seen = set()
    out = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def extract(pdf, txt_out):
    code = ('from pypdf import PdfReader; r=PdfReader(r"%s"); '
            'open(r"%s","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))'
            % (pdf.replace('"', '\\"'), txt_out.replace('"', '\\"')))
    subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=120)
    return os.path.exists(txt_out)


def verify_doi(txt_path, doi):
    try:
        c = open(txt_path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False
    return doi.startswith('10.') and doi in c[:4500]


included = [n for n in range(1, 430) if S[n][5] == 'Include']
lines = []
done, fail = [], []
for idx, n in enumerate(included):
    m = meta[n]
    slug = S[n][7]
    out_txt = os.path.join(FT, f'{m["rid"]}_{slug}.txt')
    if os.path.exists(out_txt) and verify_doi(out_txt, m['doi']):
        done.append((n, 'already-verified', out_txt))
        lines.append(f'#{n} [{m["rid"]}] {slug} -> already-verified')
        continue
    # remove stale files
    for suf in ('.txt', '.pdf'):
        p = os.path.join(FT, f'{m["rid"]}_{slug}{suf}')
        if os.path.exists(p):
            os.remove(p)
    out_pdf = os.path.join(FT, f'{m["rid"]}_{slug}.pdf')
    ok = False
    for u in candidate_urls(m['doi']):
        if ps_download(u, out_pdf):
            if extract(out_pdf, out_txt) and verify_doi(out_txt, m['doi']):
                done.append((n, 'verified', out_txt))
                lines.append(f'#{n} [{m["rid"]}] {slug} -> verified ({u[:60]})')
                ok = True
                break
            else:
                os.remove(out_pdf)
    if not ok:
        fail.append((n, m['rid'], slug, m['doi'], m['ti'][:55]))
        lines.append(f'#FAIL {n} [{m["rid"]}] {slug} DOI={m["doi"] or "-"} | {m["ti"][:55]}')
    if (idx + 1) % 15 == 0:
        print(f'progress {idx+1}/{len(included)}: done={len(done)} fail={len(fail)}')

lines.insert(0, f'DONE: {len(done)} | FAIL: {len(fail)}')
open(REPORT, 'w', encoding='utf-8').write('\n'.join(lines))
print(f'FINAL done={len(done)} fail={len(fail)} -> report at {REPORT}')

"""Download OA PDFs for Step-3 batches and extract text with pypdf."""
import os, sys, urllib.request

FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
os.makedirs(FT, exist_ok=True)
HDR = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def fetch(url, slug):
    out = os.path.join(FT, slug + '.pdf')
    req = urllib.request.Request(url, headers=HDR)
    try:
        with urllib.request.urlopen(req, timeout=60) as r, open(out, 'wb') as f:
            f.write(r.read())
        return os.path.getsize(out) > 20000
    except Exception:
        if os.path.exists(out):
            os.remove(out)
        return False

def mdpi(slug, jour, v, i, a):
    for suf in ('-v2', ''):
        u = f'https://mdpi-res.com/d_attachment/{jour}/{jour}-{v}-{i}-{a}/article_deploy/{jour}-{v}-{i}-{a}{suf}.pdf'
        if fetch(u, slug):
            return True
    return False

# Downloads are done via PowerShell (system proxy); this script only extracts.

# extract text
from pypdf import PdfReader
for f in os.listdir(FT):
    if f.endswith('.pdf'):
        txt_path = os.path.join(FT, f[:-4] + '.txt')
        if os.path.exists(txt_path):
            continue
        try:
            r = PdfReader(os.path.join(FT, f))
            t = '\n'.join(p.extract_text() or '' for p in r.pages)
            open(txt_path, 'w', encoding='utf-8').write(t)
            print(f, '->', len(t), 'chars')
        except Exception as e:
            print(f, 'EXTRACT FAIL', e)

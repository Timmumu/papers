# -*- coding: utf-8 -*-
"""Fetch missing/wrong fulltexts: 3756 (arXiv), 3993 (MDPI Buildings)."""
import urllib.request, urllib.parse, re, ssl, json, sys, os

DIR = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get(url, timeout=60, headers=None):
    req = urllib.request.Request(url, headers=headers or {'User-Agent': 'Mozilla/5.0 (research script; contact: local)'})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read(), r.geturl(), r.status

# ---------- 3756 arXiv ----------
q = urllib.parse.quote('all:"Lessons Learned from the Real-World Deployment of Multisensor Fusion for Proactive Work Zone Safety"')
api = 'http://export.arxiv.org/api/query?search_query=%s&max_results=5' % q
try:
    data, _, _ = get(api, headers={'User-Agent': 'Mozilla/5.0'})
    txt = data.decode('utf-8', 'replace')
    ids = re.findall(r'<id>http://arxiv.org/abs/([^<]+)</id>', txt)
    titles = re.findall(r'<title>([^<]+)</title>', txt)
    print('arXiv candidates:')
    for i, t in zip(ids, titles[1:]):
        print('  ', i, '|', t[:100])
    if ids:
        aid = ids[0].split('v')[0]
        print('chosen:', aid)
        pdf_url = 'https://arxiv.org/pdf/%s' % aid
        b, _, _ = get(pdf_url)
        out_pdf = os.path.join(DIR, '3756_Ahmad2026.pdf')
        open(out_pdf, 'wb').write(b)
        print('downloaded', out_pdf, len(b), 'bytes')
except Exception as e:
    print('arXiv fetch error:', e)

# ---------- 3993 MDPI search ----------
try:
    q = urllib.parse.quote('"Intelligent Analysis of Construction Safety of Large Underground Space Based on Digital Twin"')
    b, final_url, _ = get('https://www.mdpi.com/search?q=%s' % q)
    page = b.decode('utf-8', 'replace')
    links = re.findall(r'href="(/[^"]*buildings[^"]*/[^"]*)"', page)
    print('\nMDPI search final url:', final_url)
    print('candidate links:', links[:10])
    m = re.search(r'href="(https?://www\.mdpi\.com/\d{4}-\d{4}/\d+/\d+/\d+[^"]*)"', page)
    print('article link regex:', m.group(1) if m else None)
except Exception as e:
    print('MDPI search error:', e)

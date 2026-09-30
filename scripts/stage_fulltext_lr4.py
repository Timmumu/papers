# -*- coding: utf-8 -*-
"""LR4 fulltext staging: match the 244 Step-1 includes to Endnote PDFs,
copy to 04d_LR4/3. fulltext L1/{R%03d}_{slug}.pdf, verify identity via
DOI/title-signature (Endnote index text or fresh pypdf extraction), and
optionally extract full TXT for Step-3 coding.

Usage (from repo root):
  .venv\\Scripts\\python.exe scripts/stage_fulltext_lr4.py stage [a b]   # copy + verify
  .venv\\Scripts\\python.exe scripts/stage_fulltext_lr4.py txt [a b]     # extract txt
where a..b are 1-based ranks over the sorted include list (default: all).
"""
import json
import os
import re
import shutil
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
FT1 = os.path.join(ROOT, '04d_LR4', '3. fulltext L1')
TXT_DIR = os.path.join(FT1, 'txt')
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
EN_IDX = os.path.join(ROOT, '04c_LR 3round', 'ss', 'endnote_index_v2.json')
COV = os.path.join(SS, 'coverage_lr4.json')
COV_TXT = os.path.join(SS, 'coverage_lr4.txt')
os.makedirs(TXT_DIR, exist_ok=True)

sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from screening_data_lr4 import S4, decision  # noqa: E402

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}
INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')

INITIAL_RE = re.compile(r'^[A-Za-z][A-Za-z]?\.?$')

def surname(aus):
    a = (aus.split(';')[0] if aus else '').strip()
    a = re.sub(r'[^A-Za-z\u00c0-\u024f\- ,.]', '', a).strip()
    if not a:
        return ''
    if ',' in a:
        a = a.split(',')[0].strip()
    toks = [t for t in a.split() if t]
    if not toks:
        return ''
    last = toks[-1]
    last_core = last.rstrip('.')
    if last != last_core or INITIAL_RE.match(last_core):
        return toks[-2].rstrip('.') if len(toks) >= 2 else last_core
    return last.rstrip('.')

STOP = set('''digital twin twins construction based using model models framework
system review study analysis approach method case data technology technologies
application applications management monitoring building buildings'''.split())

def title_words(ti):
    ws = [w for w in re.split(r'\W+', ti.lower()) if len(w) > 4 and w not in STOP]
    return ws[:14]

def title_full(ti):
    """All significant title words incl. stopwords, for filename/text matching."""
    ws = [w for w in re.split(r'\W+', ti.lower()) if len(w) >= 3]
    return ws[:20]

def hits_in(ws, text):
    return [w for w in ws if w in text]

def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())

def strip_accents(s):
    import unicodedata
    return ''.join(c for c in unicodedata.normalize('NFKD', s or '')
                   if not unicodedata.combining(c)).lower()

def get_index():
    try:
        with open(EN_IDX, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def walk_pdfs():
    out = []
    for root, _, files in os.walk(EN_PDF):
        for f in files:
            if f.lower().endswith('.pdf'):
                out.append((os.path.join(root, f), f))
    return out

def surnames_all(aus):
    """All author surnames (accent-stripped, lower)."""
    out = []
    for a in (aus or '').split(';'):
        a = a.strip()
        if not a:
            continue
        if ',' in a:
            a = a.split(',')[0].strip()
        a = re.sub(r'[^A-Za-z\u00c0-\u024f\- .]', '', a).strip()
        toks = [t for t in a.split() if t]
        if not toks:
            continue
        last = toks[-1]
        core = last.rstrip('.')
        is_init = bool(re.match(r'^(?:[A-Za-z]\.)+$', last)) or \
            (len(core) == 1 and last.isupper())
        sn = toks[-2] if is_init and len(toks) >= 2 else core
        sn = sn.rstrip('.')
        if sn and strip_accents(sn) not in out:
            out.append(strip_accents(sn))
    return out

def match_candidates(sur, year, files, authors=''):
    cands = []
    s = strip_accents(sur)
    sset = set(surnames_all(authors)) if authors else {s}
    for path, base in files:
        low = base.lower()
        if not low.endswith('.pdf'):
            continue
        head = low[:-4]
        seg = head.split('-')[0].strip()
        hacc = strip_accents(head)
        sacc = strip_accents(seg)
        ok = False
        for sn in sset:
            if not sn:
                continue
            if (hacc.startswith(sn + '-') or hacc.startswith(sn + ',') or
                    hacc.startswith(sn + ' ') or hacc.startswith(sn + ' et') or
                    sn in sacc.split() or sacc.replace(',', ' ').rstrip('.').split()[-1:] == [sn]):
                ok = True
                break
        if not ok:
            continue
        yr = 1 if (year and year in head) else 0
        cands.append((path, base, yr))
    return cands

def score(fname, words):
    low = strip_accents(fname)
    return sum(1 for w in words if w in low)

def verify_text(text, doi, ti):
    """Return (ok, method)."""
    if not text:
        return (False, '')
    nt = norm(text)
    if doi:
        dn = norm(doi)
        dn = dn[2:] if dn.startswith('10') and len(dn) > 10 else dn
        if len(dn) >= 12 and dn in nt:
            return (True, 'doi')
    ws = title_full(ti)
    n = len(hits_in(ws, text))
    strong = n >= max(4, round(0.6 * len(ws)))
    return (strong, 'title+%d/%d' % (n, len(ws)))

def verify_full(pdf_path, doi, ti):
    """Deep verification: DOI anywhere in full text; else title front check."""
    try:
        from pypdf import PdfReader
        r = PdfReader(pdf_path)
        parts = []
        for pg in r.pages:
            parts.append(pg.extract_text() or '')
        t = re.sub(r'\s+', ' ', ' '.join(parts)).strip().lower()
        nt = norm(t)
    except Exception:
        return (False, '')
    if doi:
        dn = norm(doi)
        dn = dn[2:] if dn.startswith('10') and len(dn) > 10 else dn
        if len(dn) >= 12 and dn in nt:
            return (True, 'doi-full')
    ws = title_full(ti)
    n = len(hits_in(ws, t[:4000]))
    strong = n >= max(4, round(0.6 * len(ws)))
    return (strong, 'title+%d/%d' % (n, len(ws)))

def verify_fname(base, ti, year):
    """Filename title-overlap check (year-gated ±1, prefix-tolerant)."""
    low = strip_accents(base[:-4] if base.lower().endswith('.pdf') else base)
    ws = title_full(ti)
    n = len([w for w in ws if w in low or w[:5] in low])
    yr_ok = year in base
    if not yr_ok and year.isdigit():
        yr_ok = any(str(int(year) + d) in base for d in (-1, 1))
    strong = n >= max(4, round(0.6 * len(ws))) and yr_ok
    return (strong, 'fname+%d/%d' % (n, len(ws)))

def extract_front(pdf_path, pages=4, cap=8000):
    try:
        from pypdf import PdfReader
        r = PdfReader(pdf_path)
        parts = []
        for pg in r.pages[:pages]:
            parts.append(pg.extract_text() or '')
        t = re.sub(r'\s+', ' ', ' '.join(parts)).strip().lower()
        return t[:cap]
    except Exception as e:
        print('  ! extract failed:', e)
        return ''

def stage(ranks):
    files = walk_pdfs()
    idx = get_index()
    cov = {}
    if os.path.exists(COV):
        try:
            cov = json.load(open(COV, encoding='utf-8'))
        except Exception:
            cov = {}
    n_ok = n_fail = 0
    for r in INCLUDED[ranks[0] - 1:ranks[1]]:
        rec = BYROW[r]
        key = str(r)
        if key in cov and cov[key].get('status') == 'verified' and \
                os.path.exists(cov[key].get('pdf', '')):
            continue
        sur = surname(rec['authors'])
        cands = match_candidates(sur, rec['year'], files, rec['authors'])
        if not cands:
            cov[key] = {'slug': rec['slug'], 'status': 'no-candidate',
                        'surname': sur, 'year': rec['year'], 'title': rec['title'][:90]}
            n_fail += 1
            print('R%03d %-18s NO CANDIDATE (sur=%s %s)' % (r, rec['slug'], sur, rec['year']))
            continue
        words = title_words(rec['title'])
        ws = title_full(rec['title'])
        chosen = None
        method = ''
        # filename hits over ALL candidates (cheap, discriminative)
        fhits = []
        for path, base, yr in cands:
            low = strip_accents(base[:-4] if base.lower().endswith('.pdf') else base)
            n = len([w for w in ws if w in low or w[:5] in low])
            yr_ok = rec['year'] in base
            if not yr_ok and rec['year'].isdigit():
                yr_ok = any(str(int(rec['year']) + d) in base for d in (-1, 1))
            fhits.append((n, yr_ok, path, base))
        by_hits = sorted(fhits, key=lambda x: -x[0])
        top = by_hits[:4]
        # pass 1: DOI in front text (top 12 by filename hits, index text)
        for n, yr_ok, path, base in by_hits[:12]:
            text = idx.get(base, {}).get('text', '')
            if not text:
                text = extract_front(path)
            ok, m = verify_text(text, rec['doi'], rec['title'])
            if ok and m.startswith('doi'):
                chosen, method = (path, base), m
                break
        # pass 2: filename title overlap (year-gated)
        if chosen is None:
            strong = [x for x in by_hits if x[1] and x[0] >= max(4, round(0.6 * len(ws)))]
            weak = [x for x in by_hits if x[1] and x[0] >= 3]
            if strong:
                n, yr_ok, path, base = strong[0]
                chosen, method = (path, base), 'fname+%d/%d' % (n, len(ws))
            elif len(by_hits) == 1 and weak:
                n, yr_ok, path, base = weak[0]
                chosen, method = (path, base), 'fname+%d/%d' % (n, len(ws))
            elif len(by_hits) >= 2:
                b1 = by_hits[0][0]
                b2 = by_hits[1][0]
                if b1 >= 3 and b1 - b2 >= 2 and by_hits[0][1]:
                    n, yr_ok, path, base = by_hits[0]
                    chosen, method = (path, base), 'fname+%d/%d' % (n, len(ws))
        if chosen is None:
            # deep pass: DOI anywhere in full text of top filename hits
            for n, yr_ok, path, base in top:
                ok, m = verify_full(path, rec['doi'], rec['title'])
                if ok and m.startswith('doi'):
                    chosen, method = (path, base), m
                    break
        if chosen is None:
            cov[key] = {'slug': rec['slug'], 'status': 'unverified',
                        'method': 'no-verification',
                        'candidates': [c[3] for c in top],
                        'doi': rec['doi'], 'title': rec['title'][:90]}
            n_fail += 1
            print('R%03d %-18s UNVERIFIED candidates=%d' % (r, rec['slug'], len(cands)))
            continue
        path, base = chosen
        dst = os.path.join(FT1, 'R%03d_%s.pdf' % (r, rec['slug']))
        shutil.copy2(path, dst)
        status = 'verified' if method.startswith(('doi', 'title', 'fname')) else 'unverified'
        cov[key] = {'slug': rec['slug'], 'pdf': dst, 'en_file': base,
                    'status': status, 'method': method,
                    'doi': rec['doi'], 'title': rec['title'][:90]}
        if status == 'verified':
            n_ok += 1
        else:
            n_fail += 1
        print('R%03d %-18s %-9s %s' % (r, rec['slug'], status, base[:70]))
    json.dump(cov, open(COV, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('this pass: verified=%d unverified/missing=%d' % (n_ok, n_fail))
    report(cov)

def extract_txt(ranks):
    cov = json.load(open(COV, encoding='utf-8'))
    from pypdf import PdfReader
    for r in INCLUDED[ranks[0] - 1:ranks[1]]:
        e = cov.get(str(r))
        if not e or not os.path.exists(e.get('pdf', '')):
            continue
        dst = os.path.join(TXT_DIR, 'R%03d_%s.txt' % (r, e['slug']))
        if os.path.exists(dst) and os.path.getsize(dst) > 2000:
            continue
        try:
            rd = PdfReader(e['pdf'])
            parts = []
            for pg in rd.pages:
                parts.append(pg.extract_text() or '')
            t = re.sub(r'[ \t]+', ' ', '\n'.join(parts))
            t = re.sub(r'\n{3,}', '\n\n', t)
            with open(dst, 'w', encoding='utf-8') as f:
                f.write(t[:60000])
            e['txt'] = dst
            print('R%03d txt %d chars' % (r, len(t)))
        except Exception as ex:
            print('R%03d txt FAIL %s' % (r, ex))
    json.dump(cov, open(COV, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def report(cov):
    lines = ['LR4 fulltext coverage (Step-1 includes = %d)' % len(INCLUDED),
             'verified=%d unverified=%d missing=%d' % (
                 sum(1 for v in cov.values() if v.get('status') == 'verified'),
                 sum(1 for v in cov.values() if v.get('status') in ('unverified', 'no-candidate')),
                 sum(1 for r in INCLUDED if str(r) not in cov)), '']
    for r in INCLUDED:
        v = cov.get(str(r))
        if not v:
            lines.append('R%03d MISSING-not-staged' % r)
        elif v.get('status') == 'verified':
            lines.append('R%03d OK       %s | %s' % (r, v['slug'], v['method']))
        else:
            lines.append('R%03d PROBLEM  %s | %s | %s' % (r, v['slug'], v.get('status'), v.get('en_file', '')))
    open(COV_TXT, 'w', encoding='utf-8').write('\n'.join(lines))

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'stage'
    a = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    b = int(sys.argv[3]) if len(sys.argv) > 3 else len(INCLUDED)
    ranks = (a, b)
    print('included=%d processing ranks %d..%d' % (len(INCLUDED), a, b), flush=True)
    if cmd == 'stage':
        stage(ranks)
    elif cmd == 'txt':
        extract_txt(ranks)
    else:
        print('unknown command')

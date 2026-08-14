"""Rebuild the Endnote front-matter index with RICHER coverage.

Fixes the flaws of the original endnote_index.json:
1. STALE: original indexed 1655 of ~1803 PDFs (library grew). We re-walk ALL PDFs.
2. TOO SHALLOW: original took only first 2 pages, truncated to 2000 chars. RG-export
   PDFs put the DOI in the citation block at the BOTTOM of the abstract page, so the
   DOI frequently landed beyond 2000 chars. We now take first 4 pages, cap ~8000 chars.
3. Also records filename AND the numeric subfolder so downstream can locate the file
   without a full os.walk every time.

Output: 04c_LR 3round/ss/endnote_index_v2.json
  { basename: {"text": <lowercased, ws-collapsed, first 4 pages, [:8000]>, "dir": <numeric subfolder>} }
"""
import os, re, json, time

EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index_v2.json'

from pypdf import PdfReader

def extract_front(pdf_path, pages=4, cap=8000):
    """Return normalized front-matter text (lowercased, whitespace-collapsed)."""
    try:
        r = PdfReader(pdf_path)
        parts = []
        for pg in r.pages[:pages]:
            parts.append(pg.extract_text() or '')
        t = ' '.join(parts)
        t = re.sub(r'\s+', ' ', t).strip().lower()
        return t[:cap]
    except Exception:
        return ''

def main():
    # collect all PDFs with their numeric subfolder
    files = []  # (abs_path, basename, subdir)
    for root, _, fs in os.walk(EN_PDF):
        sub = os.path.basename(root)
        for f in fs:
            if f.lower().endswith('.pdf'):
                files.append((os.path.join(root, f), f, sub))

    print(f'Found {len(files)} PDFs in Endnote library', flush=True)

    idx = {}
    empty = 0
    short = 0
    t0 = time.time()
    for i, (abs_path, base, sub) in enumerate(files):
        t = extract_front(abs_path)
        if not t.strip():
            empty += 1
        elif len(t) < 1000:
            short += 1
        idx[base] = {'text': t, 'dir': sub}
        if (i + 1) % 400 == 0:
            el = time.time() - t0
            print(f'  ...{i+1} ({el:.0f}s)', flush=True)

    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(idx, f, ensure_ascii=False)

    print(f'\nDone. Indexed {len(idx)} PDFs -> {OUT}')
    print(f'  empty extraction: {empty}')
    print(f'  short (<1000 chars): {short}')

if __name__ == '__main__':
    main()

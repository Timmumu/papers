"""Find an Endnote-attached PDF for a paper by (first-author, year, title-keyword).

Usage:
  python find_endnote_pdf.py "Chan" "2025" "bridge"
  python find_endnote_pdf.py --list-all
"""
import sys, os, re

EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'


def all_pdfs():
    out = []
    for root, _, files in os.walk(EN_PDF):
        for f in files:
            if f.lower().endswith('.pdf'):
                out.append(os.path.join(root, f))
    return out


def find(author=None, year=None, keyword=None, limit=5):
    hits = []
    for p in all_pdfs():
        name = os.path.basename(p)
        if author and author.lower() not in name.lower():
            continue
        if year and year not in name:
            continue
        if keyword and keyword.lower() not in name.lower():
            continue
        hits.append(p)
        if len(hits) >= limit:
            break
    return hits


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == '--list-all':
        print('total PDFs:', len(all_pdfs()))
    else:
        a = sys.argv[1] if len(sys.argv) > 1 else None
        y = sys.argv[2] if len(sys.argv) > 2 else None
        k = sys.argv[3] if len(sys.argv) > 3 else None
        for h in find(a, y, k):
            print(h)
        if not find(a, y, k):
            print('(no match)')

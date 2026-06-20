"""Bridge: match EndNote PDFs to PRISMA notes via DOI, extract full text.
Usage: python enl_bridge.py [--extract] [--limit N]
  --extract : actually extract full text (default: stats only)
  --limit N  : limit to N matches (default: all)
"""
import sqlite3, csv, os, sys
from pathlib import Path
from pypdf import PdfReader

ENL = r"H:\phd\paper\Endnote\My EndNote Library.enl.backup"
DATA = r"H:\phd\paper\Endnote\My EndNote Library.Data"
HERE = Path(__file__).resolve().parent
KEYMAP = HERE / "csv" / "zotero_keymap.csv"
NOTES = HERE.parent / "01_source"

do_extract = "--extract" in sys.argv
limit = None
for i, a in enumerate(sys.argv):
    if a == "--limit" and i+1 < len(sys.argv):
        limit = int(sys.argv[i+1])

# ---- 1. Load PRISMA keymap (DOI -> note_file)
print("Loading keymap...")
prisma = {}
with open(KEYMAP, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        doi = (r.get("doi") or "").strip().lower()
        if doi:
            prisma[doi] = {
                "note_file": r["note_file"],
                "zotero_key": r["zotero_key"],
                "batch": r.get("batch", ""),
                "order": r.get("order", ""),
            }
print(f"  {len(prisma)} PRISMA notes with DOIs")

# ---- 2. Load EndNote refs (DOI -> pdf_path, abstract)
print("Loading EndNote refs...")
conn = sqlite3.connect(ENL)
cursor = conn.cursor()
cursor.execute("""
    SELECT r.id, r.title, r.electronic_resource_number, r.abstract,
           f.file_path
    FROM refs r LEFT JOIN file_res f ON r.id = f.refs_id
    WHERE r.trash_state = 0
""")
enl = {}
no_doi = 0
has_pdf = 0
for r in cursor.fetchall():
    doi = (r[2] or "").strip().lower()
    pdf = (r[4] or "").replace("internal-pdf://", "").strip()
    if doi:
        enl[doi] = {
            "enl_id": r[0],
            "title": r[1] or "",
            "abstract": r[3] or "",
            "pdf_path": pdf if pdf else None,
        }
    else:
        no_doi += 1
    if pdf:
        has_pdf += 1
conn.close()
print(f"  {len(enl)} EndNote refs with DOIs ({no_doi} without)")
print(f"  {has_pdf} refs with PDF attachments")

# ---- 3. Match by DOI
print("\nMatching...")
matched = []
for doi, edata in enl.items():
    if doi in prisma:
        matched.append((doi, edata, prisma[doi]))

print(f"  {len(matched)} matches (EndNote DOI ∩ PRISMA DOI)")

with_pdf = [(d, e, p) for d, e, p in matched if e["pdf_path"]]
with_abstract = [(d, e, p) for d, e, p in matched if e["abstract"]]
print(f"  With PDF: {len(with_pdf)}")
print(f"  With EndNote abstract: {len(with_abstract)}")

# Check title-only notes
title_only_upgradable = []
for doi, edata, pdata in matched:
    nf = NOTES / pdata["note_file"]
    if nf.exists():
        content = nf.read_text(encoding="utf-8")
        if "zotero_status: title-only" in content:
            title_only_upgradable.append((doi, edata, pdata))
print(f"  Title-only notes with EndNote match: {len(title_only_upgradable)}")

if title_only_upgradable:
    print("\n  Title-only notes that could be upgraded:")
    for doi, edata, pdata in title_only_upgradable[:25]:
        flags = []
        if edata["pdf_path"]: flags.append("PDF")
        if edata["abstract"]: flags.append("ABS")
        print(f"    [{pdata['order']}] {pdata['note_file']}  {' '.join(flags)}")

# Unmatched PRISMA
unmatched = [doi for doi in prisma if doi not in enl]
print(f"\n  PRISMA notes NOT in EndNote: {len(unmatched)}")

# ---- 4. Optional extract
if do_extract and with_pdf:
    subset = with_pdf[:limit] if limit else with_pdf
    print(f"\nExtracting full text from {len(subset)} PDFs...")
    extracted = 0
    for doi, edata, pdata in subset:
        pdf_rel = edata["pdf_path"]
        pdf_full = os.path.join(DATA, "PDF", pdf_rel)
        if not os.path.exists(pdf_full):
            print(f"  MISSING: {pdf_full}")
            continue
        try:
            reader = PdfReader(pdf_full)
            text = "".join(page.extract_text() or "" for page in reader.pages)
            print(f"  [{extracted+1}] {pdata['note_file']}: {len(text)} chars, {len(reader.pages)} pages")
            extracted += 1
        except Exception as ex:
            print(f"  ERROR [{pdata['note_file']}]: {ex}")
    print(f"  Extracted: {extracted} PDFs")

"""Dump current Abstract section text for a given batch's notes, plus which
analytical sections are still placeholders. Writes LR 2round/_batchdump.md.
Usage: python dump_batch.py 1
"""
import csv, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / "01_source"
batch = sys.argv[1] if len(sys.argv) > 1 else "1"

with open(HERE / "csv" / "zotero_keymap.csv", encoding="utf-8-sig") as f:
    rows = [r for r in csv.DictReader(f) if r["batch"] == batch]
rows.sort(key=lambda r: int(r["order"]))

PLACE = "*To be completed at full-text review.*"
out = []
for r in rows:
    p = NOTES / r["note_file"]
    t = p.read_text(encoding="utf-8")
    # abstract section
    m = re.search(r'## Abstract \^sec-abstract\s*\n+(.*?)\n+## ', t, re.S)
    abs = (m.group(1).strip() if m else "(no abstract section)")
    placeholders = t.count(PLACE)
    out.append(f"### [{r['order']}] {r['note_file']}  key={r['zotero_key']} oa={r['oa']} pdf={r['has_pdf']}")
    out.append(f"placeholders={placeholders}")
    out.append("ABSTRACT:")
    out.append(abs)
    out.append("")

(HERE / "_batchdump.md").write_text("\n".join(out), encoding="utf-8")
print(f"batch {batch}: {len(rows)} notes dumped")

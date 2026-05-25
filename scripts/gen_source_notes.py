"""Batch generate 01_source skeleton notes from LR_GPT.md reference list."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LR = ROOT / "MD" / "LR_GPT.md"
SRC = ROOT / "01_source"
SRC.mkdir(exist_ok=True)

text = LR.read_text(encoding="utf-8")
m = re.search(r"^\[11\]\s", text, re.MULTILINE)
if not m:
    print("ERROR: Could not find [11]")
    exit(1)

ref_entries = re.split(r"\n(?=\[\d+\])", text[m.start():])

def parse_entry(entry):
    ref_m = re.match(r"^\[(\d+)\]\s+", entry)
    if not ref_m:
        return None
    ref_num = ref_m.group(1)
    rest = entry[ref_m.end():]
    
    # Find title between first pair of quotes
    q1 = rest.find('"')
    if q1 == -1: return None
    q2 = rest.find('"', q1 + 1)
    if q2 == -1: return None
    
    authors = rest[:q1].rstrip(', ').strip()
    title = rest[q1+1:q2]
    rest2 = rest[q2+1:].strip().lstrip(',.')
    
    # Year
    yr = re.search(r'(19\d{2}|20\d{2})', rest2)
    year = yr.group(1) if yr else "????"
    
    # DOI
    doi_m = re.search(r"doi:\s*(10\.\S+)", rest2)
    doi = doi_m.group(1).rstrip(".") if doi_m else ""
    
    # First author last name
    first_author = authors.split(",")[0].strip()
    last_name = first_author.split()[-1] if first_author else "Unknown"
    citekey = f"{last_name}{year}"
    
    return {"ref": ref_num, "citekey": citekey, "authors": authors, "title": title, "year": year, "doi": doi}

existing = {f.stem.lower() for f in SRC.glob("*.md")}
created = skipped = 0

for entry in ref_entries:
    d = parse_entry(entry)
    if not d: continue
    if d["citekey"].lower() in existing:
        skipped += 1; continue
    
    fpath = SRC / f"{d['citekey']}.md"
    if fpath.exists():
        fpath = SRC / f"{d['citekey']}-{d['ref']}.md"
    
    doi_link = f'[{d["doi"]}](https://doi.org/{d["doi"]})' if d["doi"] else "N/A"
    note = f'---\nref: "[{d["ref"]}]"\ncitekey: "{d["citekey"]}"\ntitle: "{d["title"]}"\nauthors: "{d["authors"]}"\nyear: {d["year"]}\ndoi: "{d["doi"]}"\nzotero_status: not_checked\ncreated: "2026-05-25"\ntags:\n  - Needs-Verification\n---\n\n# {d["citekey"]}\n\n| Field | Value |\n|-------|-------|\n| **Ref** | [{d["ref"]}] |\n| **Title** | {d["title"]} |\n| **Authors** | {d["authors"]} |\n| **DOI** | {doi_link} |\n\n## Unverified / Pending\n\nSkeleton note - not yet verified against Zotero fulltext.\n'
    fpath.write_text(note, encoding="utf-8")
    created += 1
    print(f"  [{d['ref']}] {d['citekey']}")

print(f"\nDone. {created} new, {skipped} existing.")

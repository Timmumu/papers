"""Phase 1.7: Cross-reference 01_source DOIs against 2round748.csv to assign identification tags."""
import csv
import re
from pathlib import Path

# Read 2round748.csv DOIs
doi_set = set()
with open('LR 2round/csv/2round748.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        doi = row.get('DOI', '').strip().lower()
        if doi:
            doi_set.add(doi)
print(f'Unique DOIs in 2round748.csv: {len(doi_set)}')

# Scan 01_source/ for DOIs
src = Path('01_source')
db_notes = []
other_notes = []
no_doi_notes = []

for md in sorted(src.glob('*.md')):
    text = md.read_text(encoding='utf-8')
    doi_m = re.search(r'doi:\s*"?(10\.[^"\s]+)"?', text)
    citekey_m = re.search(r'citekey:\s*"([^"]+)"', text)
    citekey = citekey_m.group(1) if citekey_m else md.stem
    
    doi = doi_m.group(1).strip().lower() if doi_m else ''
    if doi:
        if doi in doi_set:
            db_notes.append((citekey, doi, md.name))
        else:
            other_notes.append((citekey, doi, md.name))
    else:
        no_doi_notes.append((citekey, md.name))

print(f'\n=== Identification Summary ===')
print(f'identification: databases  → {len(db_notes)} notes')
print(f'identification: other methods (DOI not in 748) → {len(other_notes)} notes')
print(f'identification: other methods (no DOI) → {len(no_doi_notes)} notes')
print(f'Total notes: {len(db_notes) + len(other_notes) + len(no_doi_notes)}')

# Print databases list
print(f'\n--- Databases ({len(db_notes)}) ---')
for ck, doi, fn in db_notes[:20]:
    print(f'  {ck}  doi:{doi}')
if len(db_notes) > 20:
    print(f'  ... and {len(db_notes)-20} more')

# Print other methods (with DOI but not in 748)
print(f'\n--- Other Methods - has DOI not in 748 ({len(other_notes)}) ---')
for ck, doi, fn in other_notes[:20]:
    print(f'  {ck}  doi:{doi}')
if len(other_notes) > 20:
    print(f'  ... and {len(other_notes)-20} more')

# Print no-DOI notes  
print(f'\n--- Other Methods - no DOI ({len(no_doi_notes)}) ---')
for ck, fn in no_doi_notes[:20]:
    print(f'  {ck}  ({fn})')
if len(no_doi_notes) > 20:
    print(f'  ... and {len(no_doi_notes)-20} more')

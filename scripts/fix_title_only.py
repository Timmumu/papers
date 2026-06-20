"""Fix title-only: match via keymap DOI + EndNote, with fallback to frontmatter DOI."""
import sqlite3, csv, re
from pathlib import Path

ENL = r'H:\phd\paper\Endnote\My EndNote Library.enl.backup'
KEYMAP = Path('LR 2round/csv/zotero_keymap.csv')
NOTES = Path('01_source')

# 1. EndNote abstracts
conn = sqlite3.connect(ENL)
c = conn.cursor()
c.execute('SELECT electronic_resource_number, abstract FROM refs WHERE trash_state=0')
enl_abs = set()
for doi_raw, abstract in c.fetchall():
    doi = (doi_raw or '').strip().lower()
    if doi and abstract:
        enl_abs.add(doi)
conn.close()
print(f'ENL abstracts: {len(enl_abs)}')

# 2. Keymap
note_doi = {}
with open(KEYMAP, encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        doi = (row.get('doi') or '').strip().lower()
        nf = row.get('note_file', '')
        if doi and nf:
            note_doi[nf] = doi
print(f'Keymap: {len(note_doi)}')

# 3. Process title-only
upgraded = 0
missing_doi = 0
no_enl = 0
for md in sorted(NOTES.glob('*.md')):
    t = md.read_text(encoding='utf-8')
    if 'zotero_status: title-only' not in t:
        continue
    
    doi = note_doi.get(md.name, '')
    if not doi:
        doi_m = re.search(r'doi:\s*"?(10\.[^"\s\n]+)"?', t)
        doi = doi_m.group(1).strip().lower() if doi_m else ''
    
    if not doi:
        missing_doi += 1
        continue
    
    if doi not in enl_abs:
        # Try without trailing slash or with https prefix variations
        found = False
        for variant in [doi.rstrip('/'), doi + '/', 'https://doi.org/' + doi]:
            if variant in enl_abs:
                doi = variant
                found = True
                break
        if not found:
            no_enl += 1
            continue
    
    new_t = t.replace('zotero_status: title-only', 'zotero_status: abstract-grounded')
    md.write_text(new_t, encoding='utf-8')
    upgraded += 1

print(f'Upgraded: {upgraded}')
print(f'Missing DOI: {missing_doi}')
print(f'No ENL match: {no_enl}')

# Final count
statuses = {}
for md in NOTES.glob('*.md'):
    zs = re.search(r'zotero_status:\s*(\S+)', md.read_text(encoding='utf-8'))
    s = zs.group(1) if zs else '?'
    statuses[s] = statuses.get(s, 0) + 1
print(f'Final: {dict(statuses)}')

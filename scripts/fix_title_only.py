"""Audit title-only notes: how many now have abstracts in EndNote backup?"""
import sqlite3, csv, re
from pathlib import Path

conn = sqlite3.connect(r'H:\phd\paper\Endnote\My EndNote Library.enl.backup')
c = conn.cursor()
c.execute("SELECT lower(electronic_resource_number), length(abstract) FROM refs WHERE trash_state=0")
enl_all = {}
for doi, abs_len in c.fetchall():
    if doi:
        enl_all[doi] = abs_len or 0
conn.close()
print(f"ENL total DOIs: {len(enl_all)}")

# Keymap
kp = Path('LR 2round/csv/zotero_keymap.csv')
nd = {}
with open(kp, encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        d = (r.get('doi') or '').strip().lower()
        nf = r.get('note_file', '')
        if d and nf:
            nd[nf] = d

# Title-only
NOTES = Path('01_source')
ttl = []
for md in sorted(NOTES.glob('*.md')):
    if 'zotero_status: title-only' in md.read_text(encoding='utf-8'):
        ttl.append(md.name)

has_abs = 0
no_abs = 0
no_enl = 0
for tn in ttl:
    doi = nd.get(tn, '')
    al = enl_all.get(doi, -1)
    if al == -1:
        no_enl += 1
    elif al > 0:
        has_abs += 1
        print(f'  HAS ABSTRACT: {tn} (abs_len={al})')
    else:
        no_abs += 1

print(f'\nTitle-only: {len(ttl)}')
print(f'  Has abstract in ENL: {has_abs}')
print(f'  No abstract in ENL:  {no_abs}')
print(f'  Not in ENL at all:   {no_enl}')

# If any have abstracts, upgrade them
if has_abs > 0:
    print(f'\nUpgrading {has_abs} notes...')
    up = 0
    for md in sorted(NOTES.glob('*.md')):
        t = md.read_text(encoding='utf-8')
        if 'zotero_status: title-only' not in t:
            continue
        doi = nd.get(md.name, '')
        al = enl_all.get(doi, -1)
        if al > 0:
            new_t = t.replace('zotero_status: title-only', 'zotero_status: abstract-grounded')
            md.write_text(new_t, encoding='utf-8')
            up += 1
    print(f'  Upgraded: {up}')
    
    statuses = {}
    for md in NOTES.glob('*.md'):
        zs = re.search(r'zotero_status:\s*(\S+)', md.read_text(encoding='utf-8'))
        s = zs.group(1) if zs else '?'
        statuses[s] = statuses.get(s, 0) + 1
    print(f'  Final: {dict(statuses)}')

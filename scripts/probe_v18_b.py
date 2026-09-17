# -*- coding: utf-8 -*-
"""Second-pass probes on v1.8: images embedded, RQ definitions, appendix, consistency of counts."""
import re, zipfile

P = r'h:\phd\6.pjt\LR1\papers\05_article\SLR for CDT (v1.8 260906).docx'
z = zipfile.ZipFile(P)
media = [n for n in z.namelist() if n.startswith('word/media/')]
print('embedded media files:', len(media))
for m in media:
    print('  ', m, z.getinfo(m).file_size)

full = open(r'h:\phd\6.pjt\LR1\papers\scripts\_v18_fulltext.txt', encoding='utf-8').read()
print('\nRQ mentions:', re.findall(r'RQ\s*\d+', full))
print('objective mentions:', re.findall(r'(?i)objective\s*\d', full)[:10])
print('Appendix A content chars after heading:', len(full.split('Appendix A. Classification')[-1]) if 'Appendix A. Classification' in full else 'HEADING NOT FOUND')
print('EndNote ref count:', full.count('<EndNoteBibliography>'))
# count consistency
for pat in [r'490', r'429', r'381', r'152', r'165', r'151', r'162']:
    print('count', pat, 'occurs', len(re.findall(r'(?<!\d)%s(?!\d)' % pat, full)))
# sentence-level language red flags
flags = re.findall(r'(?i)\b(distributation|is initially observed|it is now available two|Three observations can emerge|To this connection|shall be closed to test|the innovations are threefold|objectives twofold)\b', full)
print('language flags:', flags)

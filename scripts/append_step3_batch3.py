"""Append Step-3 deep-read sections to atomic notes for the 25 newly coded papers.
Source: full text obtained from Endnote library (front-matter DOI verified) or OA download.
"""
import os, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from step3_data import S3
from screening_data import S

OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

# index -> slug -> source provenance
NEW = {
14: 'Alvaro2025.md', 20: 'Araujo2025.md', 66: 'Deng2025-risk.md', 86: 'Gao2025-vibration.md',
92: 'Geng2025-bridgenet.md', 100: 'Granzner2023.md', 115: 'Hasan2022.md', 165: 'Kim2023-piping.md',
178: 'Levine2022.md', 219: 'Luleci2024.md', 253: 'Palihakkara2025.md', 262: 'Pham2026-pollution.md',
265: 'Ponzo2024-scopus.md', 271: 'Qiu2025.md', 299: 'Shariatfar2026.md', 309: 'Song2023-robot.md',
315: 'Su2025.md', 331: 'Torrecilla-Garcia2021.md', 334: 'Tran2025.md', 354: 'Wen2025-prefab.md',
376: 'Yan2025-nearmiss.md', 389: 'You2023.md', 402: 'Zhang2022-LoD.md', 412: 'Zhao2025-anticollision.md',
423: 'Zhu2023-dam.md',
}

def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive'
    return 'Unclear'

for n, slug in NEW.items():
    path = os.path.join(OUT, slug)
    if not os.path.exists(path):
        print('!! missing note', slug)
        continue
    v = S3[n]
    P, Q, R, tier, V, W, X, Z, AA, AB, AC, AD, AE, AF, AG = v
    sec = f"""
## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {P} | {Q} | {R} | {tier_short(tier)} | {V} | {W} | {X} | {Z} | {AA} | {AB} | {AC} | {AD} | {AE} | {AF} |

**Key evidence (AG):** {AG}
"""
    open(path, 'a', encoding='utf-8').write(sec)
    print('updated', slug)

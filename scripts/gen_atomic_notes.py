"""Generate atomic markdown notes for the first 100 papers of 429 papers.txt.
Screening codes (G,H,I,J,K, decision, note) are embedded from the manual Step-1 screening.
"""
import re, os

SRC = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
OUTDIR = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'
os.makedirs(OUTDIR, exist_ok=True)

# n -> (G,H,I,J,K, decision, note, filename_slug)
S = {
1:('No DT','No','No','Yes','Yes','Exclude','Tech-adoption survey; no DT, no DfS/DfQ focus','AbdulLateef2024'),
2:('Yes','Yes','No','Yes','Yes','Exclude','Energy/comfort/carbon only; safety shield is control constraint (edge 5)','Abuhussain2026'),
3:('No','No','No','Yes','Yes','Exclude','Cybersecurity of industrial CPS/SCADA; not AECO','Adamos2024'),
4:('No','Yes','No','Yes','Yes','Exclude','Smart energy systems CI; not built environment','Aghazadeh-Ardebili2025-resilience'),
5:('No','Yes','No','Yes','Yes','Exclude','Crowd management/surveillance; no built asset DfS/DfQ','Aghazadeh-Ardebili2025-fencing'),
6:('Yes','Yes','Yes','Yes','Yes','Include','Work-zone safety; predictive DT framework for conflict detection','Ahmad2026'),
7:('Yes','Yes','Yes','Yes','Yes','Include','Concept/scenario paper; DT+CPS for construction safety & health','Akanmu2021'),
8:('Yes','No','Yes','Yes','Yes','Exclude','SHM hybrid AI; no DT built/proposed','AlAmmairih2025'),
9:('Yes','No','Yes','Yes','Yes','Exclude','FEM+NN metamodel; authors state not a full digital twin','AlOmari2025'),
10:('Yes','No','No','Yes','Yes','Exclude','BIM-ICDD semantic linking; no DT; compliance not DfQ','AlSadoon2026'),
11:('No','No','No','Yes','Yes','Exclude','Nuclear power domain','Alberti2023'),
12:('Yes','No','Yes','Yes','Yes','Exclude','BIM-HDM framework; DT only future early warning','Allalou2026'),
13:('Yes','Yes','Yes','Yes','Yes','Include','DT-based fire safety management framework; conceptual + survey','Almatared2024'),
14:('Yes','Yes','Yes','Yes','Yes','Include','Building DT for emergency response & evacuation safety','Alvaro2025'),
15:('Yes','Yes','Yes','Yes','Yes','Include','DT for guiderail safety-hardware condition & preventive maintenance','Ammar2024'),
16:('No','No','No','Yes','Yes','Exclude','Legal/regulatory IoT paper; not AECO','Anna2021'),
17:('Yes','No','No','Yes','Yes','Exclude','AI-in-motorways review; DT one of many topics','Anthi2025'),
18:('No','Yes','No','Yes','Yes','Exclude','Cybersecurity; airport baggage system industrial testbed','Apolinario2024'),
19:('Yes','Yes','Yes','Yes','Yes','Include','DT definition/standardisation for construction; safety in scope','Aragon2025'),
20:('Yes','Yes','Yes','Yes','Yes','Include','DT conceptual model for site resource control incl. quality','Araujo2025'),
21:('Yes','Yes','Yes','Yes','Yes','Include','Cloud DT for infrastructure inspection; defects as georeferenced anchors','Arhrib2026'),
22:('Yes','Yes','Yes','Yes','Yes','Include','DT SHM, anomaly detection, damage warnings; 2-yr pilot','Armijo2024'),
23:('Yes','Yes','Yes','Yes','Yes','Include','SHM-DT framework, damage levels, early warning; heritage basilica','Aroquipa2025'),
24:('Yes','Yes','Yes','Yes','Yes','Include','Adoption drivers incl. safety & quality factors; survey','Arowoiya2024'),
25:('Yes','No','Yes','Yes','Yes','Exclude','CV pose estimation; DT only synthesizes training data','Assadzadeh2023'),
26:('Yes','No','Yes','Yes','Yes','Exclude','BIM+RPA weather alerts; static BIM, no live DT','Atencio2024'),
27:('Yes','No','No','Yes','Yes','Exclude','CE/digitalisation review; DT peripheral','Banihashemi2024'),
28:('Yes','Yes','Yes','Yes','Yes','Include','Review incl. geological DT, real-time risk analysis, construction safety','Bao2026'),
29:('Yes','No','Yes','Yes','No','Exclude','Russian journal; BIM/DT mentioned, full text non-English','Baulin2025-dismantling'),
30:('Yes','No','No','Yes','Yes','Exclude','Urban regeneration protocol; DT as future archive','Benedetti2022'),
31:('No','Yes','Yes','Yes','No','Exclude','Industrial port ops; Chinese journal, non-English','Bi2024'),
32:('Yes','No','Yes','Yes','Yes','Exclude','Pure FEM structural analysis; no DT','Blomfors2020'),
33:('Yes','No','No','Yes','Yes','Exclude','BIM-manager narrative review; no DT core','Borkowski2026'),
34:('Yes','No','Yes','Yes','Yes','Exclude','I-BIM maintenance framework; DT aspirational','Bosurgi2025'),
35:('Yes','Yes','Yes','Yes','Yes','Include','DT framework for critical infrastructure resilience & crisis mgmt','Brucherseifer2021'),
36:('Yes','No','No','Yes','Yes','Exclude','Data-management review; no DT core, no safety/quality','Bucher2024'),
37:('No','No','No','Yes','Yes','Exclude','Emotion recognition; no built asset, no safety/quality','Cai2026'),
38:('Yes','No','Yes','Yes','Yes','Exclude','Neural-SDF reconstruction; DT only downstream use','Cao2026'),
39:('Yes','No','No','Yes','Yes','Exclude','Static GIS-BIM/CMMS-3D; no live DT','Carrasco2024'),
40:('Yes','No','Yes','Yes','Yes','Exclude','BIM-Dynamo automation; initial step towards DT only','Cavieres-Lagos2024'),
41:('Yes','No','No','Yes','Yes','Exclude','Bibliometric; DT only a keyword trend','Cervantes2026'),
42:('Yes','Yes','Yes','Yes','Yes','Include','ANN surrogate within DT for bridge SHM, safety info, life-cycle','Cervenka2026'),
43:('Yes','No','No','Yes','Yes','Exclude','Tech-adoption survey; DT one of many','Chaaya2025'),
44:('Yes','Yes','Yes','Yes','Yes','Include','Real DT prototype on office-building site; health & safety potential','Chacon2024'),
45:('Yes','Yes','Yes','Yes','Yes','Include','DT structural model validated on field data; what-if risk scenarios','Chan2025'),
46:('Yes','Yes','Yes','Yes','Yes','Include','DT generation module + CV inspection; quality defect tracking','Chang2024-rebar'),
47:('Yes','Yes','Yes','Yes','Yes','Include','DT framework for settlement/deformation prediction; safety & risk','Chang2026-tunnel'),
48:('Yes','Yes','Yes','Yes','No','Exclude','Chinese journal; full text non-English','Chao2022'),
49:('Yes','Yes','Yes','Yes','Yes','Include','Real-time risk assessment, hazard inference, tunnel project applied','Chen2025-KG'),
50:('Yes','Yes','Yes','Yes','Yes','Include','DT for gin-pole lifting; safety risk reduced 32%','Chen2026-ginpole'),
51:('No','Yes','Yes','Yes','No','Exclude','Oil/gas pipeline industry; Chinese journal, non-English','Chen2021-pipeline'),
52:('Yes','Yes','Yes','Yes','No','Exclude','Chinese journal; non-English full text','Cheng2025'),
53:('Yes','No','Yes','Yes','Yes','Exclude','CV activity recognition; DT integration future work','Cho2025'),
54:('No','Yes','No','Yes','Yes','Exclude','Materials/manufacturing component DT; not AECO','Cogswell2022'),
55:('Yes','No','Yes','Yes','Yes','Exclude','BIM+AR safety inspection; no DT (duplicate of #56)','Corneli2025-scopus'),
56:('Yes','No','Yes','Yes','Yes','Exclude','Duplicate of ID 3660 (WoS copy); BIM-based, no DT','Corneli2025-wos'),
57:('No','No','No','Yes','Yes','Exclude','Traffic ITS survey; DT only future distribution topic','Creb2024'),
58:('Yes','No','Yes','Yes','Yes','Exclude','Pure FE soil-structure interaction study; no DT','Cruz2024-ssi'),
59:('Yes','No','Yes','Yes','Yes','Exclude','Pure FE seismic SSI analysis; no DT','Cruz2024-shearwave'),
60:('Yes','No','Yes','Yes','Yes','Exclude','Load-identification method; DT only data consumer','Dan2026-loadid'),
61:('Yes','Yes','Yes','Yes','Yes','Include','Regional bridge-group DT; condition perception & safety warning','Dan2022-bridgesgroup'),
62:('Yes','No','Yes','Yes','Yes','Exclude','Damage-index benchmarking; DT only future use','Danesi2025'),
63:('No','No','No','Yes','Yes','Exclude','Marine science RIs; not AECO','Danobeitia2023'),
64:('No','Yes','No','Yes','Yes','Exclude','Oil-refinery process CPS; industrial','Dedousis2023'),
65:('Yes','Yes','Yes','Yes','Yes','Include','Station DTs for incident decision support; response -17.4%','Delhibabu2026'),
66:('Yes','Yes','Yes','Yes','Yes','Include','DTCRAM for construction risk prediction/control','Deng2025-risk'),
67:('Yes','Yes','Yes','Yes','Yes','Include','RtBDM framework; real-time monitoring & decision for bridge safety','Deng2025-bridge'),
68:('Yes','Yes','Yes','Yes','Yes','Include','Closed-loop site DT + LLM; productivity & safety motivation','Deng2026-llm'),
69:('Yes','Yes','Yes','Yes','No','Exclude','Chinese journal (Tunnel Construction); non-English','Ding2024-tunnel'),
70:('Yes','No','Yes','Yes','Yes','Exclude','CV tracking framework; DT as end-goal only','Ding2025-evac'),
71:('Yes','Yes','Yes','Yes','No','Exclude','Chinese journal (CIMS); non-English full text','Dong2024-crane'),
72:('Yes','Yes','Yes','Yes','Yes','Include','Renovation DT tracking quality & safety KPIs; pilot + TAM','Doukari2026'),
73:('No','Yes','Yes','Yes','No','Exclude','Additive manufacturing; Chinese journal, non-English','Duan2021'),
74:('Yes','Yes','Yes','Yes','Yes','Include','SLR (229 pubs) + ISO 19650-based DT framework for construction assets','ElDin2022'),
75:('Yes','Yes','No','Yes','Yes','Exclude','DTSRM for cost/time/resources; safety only as extension','Elghaish2025'),
76:('Yes','Yes','Yes','Yes','Yes','Include','Highway project DT demonstrators incl. health & safety twin','Ellul2024'),
77:('Yes','No','Yes','Yes','Yes','Exclude','Level-2 static twin = calibrated BIM; no live data link','Eren2026'),
78:('Yes','Yes','Yes','Yes','Yes','Include','Closed-loop simulation DT for unsafe-behavior intervention','Fang2023'),
79:('Yes','No','Yes','Yes','Yes','Exclude','Scientometric review; DT only integration trend','Fayyad2025'),
80:('Yes','Yes','No','Yes','Yes','Exclude','FM reactive maintenance; safety incidental','Fialho2022'),
81:('Yes','No','No','Yes','Yes','Exclude','AI design co-pilot; no DT','Fisch2023-en'),
82:('Yes','No','No','Yes','No','Exclude','German duplicate of ID 3632; non-English','Fisch2023-de'),
83:('No','Yes','No','Yes','Yes','Exclude','Fusion-reactor maintenance robotics; not AECO','Fontanelli2024'),
84:('Yes','Yes','Yes','Yes','Yes','Include','Adaptable bridge DT; what-if simulations; safety & lifespan','Franciosi2024'),
85:('No','Yes','Yes','Yes','Yes','Exclude','Mining ventilation; not AECO built environment','Gao2026-mine'),
86:('Yes','Yes','Yes','Yes','Yes','Include','DT safety-management model; stress prediction 99.1% (verify Step 3)','Gao2025-vibration'),
87:('No','No','No','Yes','Yes','Exclude','Vehicle localization framework; not AECO','Gao2024-localization'),
88:('Yes','Yes','Yes','Yes','Yes','Include','Integrated WebGIS+WebBIM DT; defect modeling, maintenance, safety','Gao2024-bridge'),
89:('No','No','No','Yes','Yes','Exclude','Fusion-energy facility design; not AECO','Gazzotti2021'),
90:('No','Yes','Yes','Yes','No','Exclude','Mining; Chinese journal, non-English','Ge2020'),
91:('No','Yes','No','Yes','Yes','Exclude','EV charging/IoV scheduling; not AECO','Geng2026-ev'),
92:('Yes','Yes','Yes','Yes','Yes','Include','BN-based system DT; multi-source data; bridge-network risk','Geng2025-bridgenet'),
93:('Yes','No','Yes','Yes','Yes','Exclude','NDT data federation in Revit; DT as future tool','Ghazy2025'),
94:('No','Yes','No','Yes','Yes','Exclude','Aerospace remanufacturing','Ghorbani2022'),
95:('Yes','No','No','Yes','Yes','Exclude','Tech-adoption survey; DT one item in a list','Ghosh2023'),
96:('No','Yes','Yes','Yes','No','Exclude','Mining ventilation; Chinese journal, non-English','Gong2021'),
97:('Yes','Yes','Yes','Yes','Yes','Include','Robot DT for motion preview & safe workspace entry; construction HRC','Gonzalez-Boehme2023'),
98:('No','Yes','No','Yes','Yes','Exclude','Cyber-physical security of CI generally; not AECO-specific','Gordan2024'),
99:('Yes','No','Yes','Yes','Yes','Exclude','Robotics-for-SHM review; DT creation only attempts','Gorski2025'),
100:('Yes','Yes','Yes','Yes','Yes','Include','4-stage concept incl. FE-based DT; safety concept & remaining-life','Granzner2023'),
}

txt = open(SRC, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
n = 0
written = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    if n > 100:
        break
    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''
    rid = field('ID'); ti = field('TI'); ab = field('AB'); db = field('DB')
    aus = re.findall(r'^AU  - (.*)$', r, re.M)
    py = field('PY'); do = field('DO'); t2 = field('T2')
    srcdb = db if db else ('Web of Science' if 'WOS:' in r else 'Lens.org')
    g,h,i,j,k,dec,note,slug = S[n]
    g = {'No DT':'No'}.get(g,g)  # normalize
    au_str = '; '.join(aus)
    first_au = aus[0].split(',')[0] if aus else 'Unknown'
    ab_short = ab[:600] + ('...' if len(ab) > 600 else '')
    md = f"""# {first_au} et al. ({py}) — {ti}

- **ID:** {rid} | **Source:** {srcdb} | **DOI:** {do or 'n/a'}
- **Journal:** {t2}
- **Authors:** {au_str}

## Abstract summary
{ab_short}

## Step-1 Screening (Prompt A)
| G | H | I | J | K | Decision |
|---|---|---|---|---|---|
| {g} | {h} | {i} | {j} | {k} | **{dec}** |

**Note:** {note}
"""
    with open(os.path.join(OUTDIR, slug + '.md'), 'w', encoding='utf-8') as f:
        f.write(md)
    written += 1
print('written', written, 'notes')

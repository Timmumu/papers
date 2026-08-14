# Lin et al. (2026) — Creation and application of a geometric digital twin model for construction of spatial cable structures: A case study

- **ID:** 3899 | **Source:** Web of Science | **DOI:** 10.1007/s11709-026-1301-0
- **Journal:** ENGINEERING STRUCTURE AND CIVIL ENGINEERING
- **Authors:** Lin, S. W.; Duan, L. P.; Liu, J. M.; Miao, J.; Li, H. M.; Zhao, J. C.

## Abstract summary
This paper presents a dynamic geometric digital twin creation method for cable-net structures in construction which creates the building information model (BIM) for construction process visualization and finite element model (FEM) for cable shape and force prediction. The basic dynamic geometric information for parametric BIMs and FEMs is extracted from multi-stage laser scanning during construction. Multi-stage BIMs are presented as Industry Foundation Classes (IFC) format where the cables are created by approximating the curved shapes with straight segments. Complex components like cable clamps are imported as Revit Family and replicated at the measured locations. Multi-stage FEMs utilize the ABAQUS secondary development technology to parametrize geometric configuration, loads and constraints between components based on actual connections. A continuous dynamic BIM from one stage to ano…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Dynamic geometric DT for cable-net construction; shape/force prediction

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Dynamic geometric digital twin (gDT) for spatial cable-net structure construction (Shanghai Jiao Tong): multi-stage laser scanning extracts geometric info → parametric IFC/BIM (cables as straight segments, clamps as Revit families) + ABAQUS FEM (shape & force prediction); previous-stage FEM + construction progress + temperature data fill gaps between scan stages to build a continuous dynamic IFC model; stage modelling+computation <140 s, BIM-vs-point-cloud avg 15-20 mm, next-stage cable shape/force prediction deviations 1.3%/1.5%. One-way physical→virtual stage-by-stage update with prediction; no actuation and no learning loop (manual re-parameterisation).

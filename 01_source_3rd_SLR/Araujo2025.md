# Araújo et al. (2025) — Proposal of a conceptual model of digital twins for construction sites

- **ID:** 4028 | **Source:** Web of Science | **DOI:** 10.7764/RIC.00168.21
- **Journal:** REVISTA INGENIERIA DE CONSTRUCCION
- **Authors:** Araújo, C. S.; Corrêa, F. R.; Ferreira, E. D. M.; Costa, D. B.

## Abstract summary
Lack of proper information flow could drive the persistent challenges of low productivity and quality in the Construction industry. Digital Twin technology integrates physical and virtual environments, providing better data flow for more efficient management. However, current propositions of Digital Twins in Construction remain incipient. The literature indicates that they are poorly defined, with no consensus on their boundaries, components, or applications. Thus, unified conceptual structures are needed to highlight the role of Digital Twins in construction management, considering their potential to integrate various digital technologies. This study proposes a conceptual model for developing and implementing Digital Twins on construction sites. It focuses on managing and controlling physical resources, such as personnel, equipment, and materials. This model is part of a broader researc…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT conceptual model for site resource control incl. quality

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Quality (DfQ) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Conceptual (no test) | 3 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** DSR conceptual model (F1 data acquisition / F2 data analysis-simulation / F3 BIM transformation boxes) for DT on construction sites, generalised from the empirical Smart Twins 4.0 system (RFID+IoT+BIM tracking of metallic formwork in concrete wall construction; 151 panels inspected, 100% external defects, wear 42% — rework/quality control). Closed-loop is human-in-the-loop only; F2 simulation box proposed but NOT implemented (future Smart Twins 5.0); no ML and no self-improvement.

**Strength & gap filled (AH):** Proposes a closed-loop conceptual model of DTs for construction sites, structured as three functional boxes: F1 data acquisition (IoT/RFID), F2 data analysis and simulation, and F3 BIM transformation into a web-based model; it is grounded in the empirical Smart Twins 4.0 system, which tracked 151 formwork panels with RFID and a web-based BIM, finding 100% external and 98% internal defects.

**Deficiencies & future work (AI):** Smart Twins 4.0 is limited to a single physical resource (formwork), has restricted data analysis capabilities and interoperability, and still requires manual steps in data collection; the model simplifies real-world complexity, omits human roles beyond decision-making, and the authors state it needs future testing in different contexts.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** RFID UHF tag readings on Android devices + Web-based Revit/Dynamo BIM models of metallic formwork.
- **Integration mechanism:** Smart Twins 4.0 links physical formworks to their virtual BIM counterparts through automatic database integration (Firebase), i.e. a shared object identity between tag data and BIM elements; 151 panels were inspected with 100% external and 98% internal defects.
- **Why this code:** tag data and BIM share a common object-identity frame while analysis stays per type, so Aligned.

**Confidence (AC3):** Medium - the automatic database integration is explicit, but the paper does not describe a joint inference step.
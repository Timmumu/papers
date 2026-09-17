# Sun et al. (2025) — Digital twin of advanced geological conditions in rock tunnel construction

- **ID:** 3941 | **Source:** Web of Science | **DOI:** 10.1016/j.autcon.2025.106407
- **Journal:** AUTOMATION IN CONSTRUCTION
- **Authors:** Sun, H. Y.; Zhu, M. Q.; Dai, Y. M.; Li, X. J.; Rui, Y.; Zhu, W. J.; Zhu, H. H.

## Abstract summary
Geological uncertainty ahead of the tunnel face presents significant challenges to the safety and efficiency of tunnel construction. To address this issue, this paper explores the feasibility of using a digital twin approach to enhance geological modeling and rock classification. The proposed method integrates multi-source geological data to construct a multi-dimensional geological virtual model, and applies a fuzzy cloud probability model to quantify uncertainty, enabling intelligent classification of surrounding rock. Results from tests on five rock tunnel projects using the iS3 platform show that the overall rock classification accuracy of the method is 92.95%. These findings clearly demonstrate that the digital twin approach significantly improves geological transparency, risk management, and decision-making efficiency in complex rock tunnel environments. Future research will focus o…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT of geological conditions in rock tunnel construction; risk management

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Digital twin for advanced geological conditions in rock tunnel construction (Tongji U): multi-source geological data (water content, lithology, integrity) → multi-dimensional virtual models (geometric, attribute, behavior); fuzzy cloud probability model quantifies uncertainty for intelligent rock classification (92.95% accuracy); iS3 platform implements closed-loop data-model-decision; validated on five rock tunnel projects. Closed-loop data→model→decision→feedback → Tier 3; no learning loop (fuzzy cloud is probabilistic, not learning).


**Strength & gap filled (AH):** Closes the data-model-decision loop for geological uncertainty ahead of tunnel faces: TEM, GPR and borehole data become point-cloud models of water content, lithology and integrity via KNN interpolation, and a fuzzy cloud probability model quantifies uncertainty to classify surrounding rock per meter within a 30 m range, achieving 92.95 percent accuracy across 539 exposed-rock records of five tunnels on the Tongji iS3 platform.

**Deficiencies & future work (AI):** Decision factors cover only water content, lithology and integrity; GPR captures a single cross-section so longitudinal integrity variation is missing, databases are unevenly sized, and per-cycle computation of 10-60 s grows to 2-5 minutes for concurrent tunnels; the authors propose GPU and KD-tree acceleration plus extension to soft-soil and underwater tunnels.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** TEM, GPR and borehole geological data (five rock-tunnel projects, 539 exposed-rock records).
- **Integration mechanism:** KNN interpolation builds per-attribute point clouds, and the fuzzy cloud probability model jointly quantifies uncertainty to classify rock per metre within 30 m (92.95% accuracy) on the iS3 platform.
- **Why this code:** the classification output depends on three geological data types simultaneously, so Fused.

**Confidence (AC3):** High - the fuzzy cloud fusion is explicit.
(full-text source: Endnote)

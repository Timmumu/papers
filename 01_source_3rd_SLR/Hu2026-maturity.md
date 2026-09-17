# Hu et al. (2026) — Multi-dimensional framework for assessing digital twin maturity in construction machinery

- **ID:** 3956 | **Source:** Web of Science | **DOI:** 10.1016/j.jii.2026.101067
- **Journal:** JOURNAL OF INDUSTRIAL INFORMATION INTEGRATION
- **Authors:** Hu, R. B.; Gong, W. T.; Chen, K.; Luo, H. B.

## Abstract summary
Smart construction machinery enabled by digital twin (DT) technology has significant potential to enhance construction safety and efficiency. However, the lack of a dedicated maturity assessment model for construction machinery DT (CMDT) reveals a critical gap in existing research. This study proposes a structured framework for assessing CMDT maturity, designed to evaluate the readiness and developmental stage of DT implementations in construction machinery. The framework was developed based on a comprehensive literature review and expert interviews, yielding a maturity assessment model comprising five dimensions and 24 indicators across five maturity levels. The model adopts a two-stage assessment approach that integrates expert competency-based grouping and weighting with an improved bi-objective optimization model. To enhance the robustness of expert opinion aggregation, a penalty-wei…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT maturity model for construction machinery; safety & efficiency

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Unclear | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Single (one data type) | Single case study | 4 | Lifecycle / governance |

**Key evidence (AG):** Multi-dimensional framework for assessing construction machinery digital twin (CMDT) maturity (HUST): 24 maturity indicators across five dimensions from literature review + expert interviews; expert-opinion grouping via community detection with competency/quality-weighted groups; improved bi-objective optimization model (adjustable penalty weight balancing PDF overlap vs confidence of collective opinion) aggregates expert judgments into overall CMDT maturity; validated on a real-world DT-driven ACS (automated climbing system) high-rise project whose DT integrates safety sensors (inclinometers, leveling instruments) and operational sensors (oil pressure, laser rangefinders); identifies maturity levels and improvement pathways. Study assesses DT maturity - does not itself build/operate a DT (tier Unclear); no learning loop.



**Strength & gap filled (AH):** Fills the absence of a construction-machinery-specific digital twin maturity model: five dimensions and 24 indicators across five levels, built from literature and expert interviews, assessed by Louvain expert grouping plus a penalty-weighted bi-objective opinion aggregation; applied to an automated construction system, the framework located the twin at Level 3, with continuous learning and real-time data processing scoring only Level 2.

**Deficiencies & future work (AI):** The assessment depends entirely on expert questionnaires (20 for indicator weighting, 15 valid in the case study), so results are subjective despite probability-based aggregation, and one ACS case limits generalizability; the authors propose update-frequency thresholds, sensor log data to replace expert judgment, and extension to other sectors.
**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** expert questionnaires and interviews feeding 24 maturity indicators.
- **Integration mechanism:** none - Louvain grouping and the bi-objective aggregation model process one data type (expert judgements); the ACS case only contextualises the assessment.
- **Why this code:** SINGLE (AC=Single).

**Confidence (AC3):** High.
(full-text source: Endnote)

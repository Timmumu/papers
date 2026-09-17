# Hagen, A et al. (2024) — Asset management, condition monitoring and Digital Twins: damage detection and virtual inspection on a reinforced concrete bridge

- **ID:** R641 | **Source:** Scopus | **DOI:** 10.1080/15732479.2024.2311911
- **Journal:** Structure and Infrastructure Engineering
- **Authors:** Hagen A.; Andersen T.M.

## Abstract summary
In April 2021 Stavå bridge, a main bridge on E6 in Norway, was abruptly closed for traffic. A structural defect had seriously compromised the bridge’s structural integrity. The Norwegian Public Roads Administration (NPRA) closed it, made a temporary solution and reopened with severe traffic restrictions. The incident was alerted through what constitutes the bridge’s Digital Twin processing data from Internet of Things sensors. The solution was crucial in online and offline diagnostics, the case demonstrating the value of technologies to tackle emerging dangerous situations as well as acting preventively. A critical and rapidly developing damage was detected in time to stop the development, but not in time to avoid the incident altogether. The paper puts risk in a broader perspective for an organization responsible for highway infrastructure. It positions online monitoring and Digital Twi…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Stava bridge DT damage detection and virtual inspection


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | IoT sensor data, physics-based methods and ML are combined in one damage-detection and virtual-inspection pipeline for the bridge. | High |

**Key evidence (AG):** Stava bridge (E6, Norway) incident study (SAP/NPRA, SIE 2024): the bridge DT processing IoT sensor data alerted a rapidly developing structural defect, enabling online and offline diagnostics and virtual inspection; physics-based methods combined with machine learning for damage detection and diagnosis; positions SHM and DTs within risk- and condition-based maintenance; damage was detected in time to stop development though not to avoid closure. One-way monitoring->diagnostics->human maintenance decisions; no actuation, no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the diagnostics gap in bridge asset management: the Stava bridge DT alerted a critical defect from IoT data in time to stop its development, and physics+ML diagnostics plus virtual inspection demonstrated risk/condition-based maintenance in practice.

**AI — deficiencies & future work:** Single incident retrospective; the DT alerted but could not prevent the closure, ML damage detection details are partial, and a prospective operational deployment with quantified lead-time gains is not demonstrated.

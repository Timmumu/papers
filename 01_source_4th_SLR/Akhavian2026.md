# Akhavian, R et al. (2026) — Semantic-Gravity Iterative Closest Point and AI-assisted navigation for Robot-Ready Construction Digital Twins

- **ID:** R079 | **Source:** Scopus | **DOI:** 10.1016/j.autcon.2026.107134
- **Journal:** Automation in Construction
- **Authors:** Akhavian R.; Amani M.; Mootz J.; Beheshti B.; Ashe R.

## Abstract summary
This paper introduces BIM2RDT (Building Information Models to Robot-Ready Construction Digital Twins), an AI-assisted pipeline transforming static BIM into dynamic digital twins for construction robot navigation and safety monitoring. The framework fuses BIM geometry, unmanned ground vehicle (UGV) visual observations, and IoT sensor data to enable automated site monitoring and safety-aware path planning. A core contribution is Semantic-Gravity ICP (SG-ICP), a point cloud registration method leveraging LLM-guided semantic reasoning to assign BIM-family-specific upright priors, improving alignment robustness in low-feature construction scenes. The framework integrates YOLOE open-vocabulary detection for BIM-conditioned perception and demonstrates safety monitoring through Hand-Arm Vibration (HAV) sensing written into IFC-compatible digital twin representations. Controlled experiments show …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM2RDT robot-ready DT; safety monitoring + path planning

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Simulation | 4 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | BIM geometry, UGV visual observations and IoT/HAV sensing are fused in the twin, with semantic activity layers written to IFC. | Medium |

**Key evidence (AG):** BIM2RDT pipeline (SDSU/UCSD, AutCon 2026): transforms static BIM into robot-ready construction digital twins; Semantic-Gravity ICP uses LLM-guided semantic reasoning to assign BIM-family-specific upright priors for low-feature scan-to-BIM registration (RMSE reduced 60-97% in high-noise controlled experiments); YOLOE open-vocabulary detection conditions perception; HAV vibration sensing written into IFC-compatible twin (IfcEvent/IfcTask) feeds context-aware cost maps for safety-aware robot path planning. Sensing->twin->planning loop with IFC updates, but robot actuation not demonstrated (navigation constraints proposed); controlled experiments only; no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Semantic-Gravity ICP with LLM-inferred upright priors cuts registration RMSE by 60-97% in low-feature scenes, and the BIM2RDT loop writes sensor-detected safety activities (HAV) into IFC for context-aware robot planning.

**AI — deficiencies & future work:** Controlled experiments without real construction-site robots; LLM orchestration is narrow/bounded (no long-horizon autonomy); actuation not demonstrated; generalisation across site types untested.

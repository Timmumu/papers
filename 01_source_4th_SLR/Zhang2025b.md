# Zhang, Y et al. (2025) — Research on the Digital Twin System for Rotation Construction Monitoring of Cable-Stayed Bridge Based on MBSE

- **ID:** R379 | **Source:** Scopus | **DOI:** 10.3390/buildings15091492
- **Journal:** Buildings
- **Authors:** Zhang Y.; Zhao Y.; Li Z.; He W.; Liu Y.

## Abstract summary
Digital twin is a virtual replica of a physical system that updates in real time using sensor data to enable simulations and predictions. For bridges constructed using rotation construction methods, the rotation phase demands continuous monitoring of structural behavior and coordination with surrounding traffic infrastructure. Therefore, a digital twin system for monitoring rotation construction is vital to ensure safety and schedule compliance. This paper explores the application of model-based systems engineering (MBSE), a modern approach that replaces text-based documentation with visual system models, to design a digital twin system for monitoring the rotation construction of a 90 m + 90 m single-tower cable-stayed bridge. A V-model architecture for the digital twin system, based on requirements analysis, functional analysis, logical design, and physical design analysis (RFLP), is pr…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** MBSE DT for cable-stayed bridge rotation construction monitoring

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 1 | 0 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Conceptual (no test) | 3 | BIM-to-Digital-Twin architecture |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | DHT11, MPU6050, wind and laser displacement sensors stream over MQTT to the Unreal prototype for dataflow verification and threshold alarms, sharing the twin frame while each channel is checked separately. | Medium |

**Key evidence (AG):** MBSE-based design of a DT system for rotation-construction monitoring of a 90m+90m single-tower cable-stayed bridge (SWJTU): V-model architecture via RFLP (requirements-functional-logical-physical) process; SysML models for requirements/functions/behavior/integration; DT intended to predict risks and optimize rotation construction plans before implementation; MBSE improves design efficiency and early flaw detection. Design-phase work only - DT not yet implemented/deployed, model validation is future work; no live data link, no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Fills the gap of system-level design methods for bridge construction digital twins: MBSE with a V-model architecture over the RFLP process models requirements, functions, logic and physics in SysML for monitoring a 90+90 meter cable-stayed bridge rotation (21,200 tons, 79 degrees), and a 1:100 scale prototype with DHT11, MPU6050, wind and laser displacement sensors over MQTT to Unreal Engine verifies data flow and threshold alarms.

**AI — deficiencies & future work:** The actual bridge was still under construction and rotation had not started, so verification is limited to a 1:100 scale model and the design decomposition phase; the authors acknowledge implementation costs, resource needs, system complexity and applicability constraints. Future research targets standardization frameworks, integrated toolchains and machine learning for long-term deformation and predictive maintenance.

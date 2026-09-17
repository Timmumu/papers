# Zhang et al. (2025) — Research on the Digital Twin System for Rotation Construction Monitoring of Cable-Stayed Bridge Based on MBSE

- **ID:** 3918 | **Source:** Web of Science | **DOI:** 10.3390/buildings15091492
- **Journal:** BUILDINGS
- **Authors:** Zhang, Y. H.; Zhao, Y. M.; Li, Z. Y.; He, W.; Liu, Y.

## Abstract summary
Digital twin is a virtual replica of a physical system that updates in real time using sensor data to enable simulations and predictions. For bridges constructed using rotation construction methods, the rotation phase demands continuous monitoring of structural behavior and coordination with surrounding traffic infrastructure. Therefore, a digital twin system for monitoring rotation construction is vital to ensure safety and schedule compliance. This paper explores the application of model-based systems engineering (MBSE), a modern approach that replaces text-based documentation with visual system models, to design a digital twin system for monitoring the rotation construction of a 90 m + 90 m single-tower cable-stayed bridge. A V-model architecture for the digital twin system, based on requirements analysis, functional analysis, logical design, and physical design analysis (RFLP), is pr…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** MBSE-designed DT for bridge rotation construction monitoring; risk prediction

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 1 | 0 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Conceptual (no test) | 3 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** MBSE-based design of a DT system for rotation-construction monitoring of a 90m+90m single-tower cable-stayed bridge (SWJTU): V-model architecture via RFLP (requirements-functional-logical-physical) process; SysML models for requirements/functions/behavior/integration; DT intended to predict risks and optimize rotation construction plans before implementation; MBSE improves design efficiency and early flaw detection. Design-phase work only - DT not yet implemented/deployed, model validation is future work; no live data link, no learning loop.


**Strength & gap filled (AH):** Fills the gap of system-level design methods for bridge construction digital twins: MBSE with a V-model architecture over the RFLP process models requirements, functions, logic and physics in SysML for monitoring a 90+90 meter cable-stayed bridge rotation (21,200 tons, 79 degrees), and a 1:100 scale prototype with DHT11, MPU6050, wind and laser displacement sensors over MQTT to Unreal Engine verifies data flow and threshold alarms.

**Deficiencies & future work (AI):** The actual bridge was still under construction and rotation had not started, so verification is limited to a 1:100 scale model and the design decomposition phase; the authors acknowledge implementation costs, resource needs, system complexity and applicability constraints. Future research targets standardization frameworks, integrated toolchains and machine learning for long-term deformation and predictive maintenance.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** DHT11, MPU6050, wind and laser displacement sensors on a 1:100 rotation-construction prototype.
- **Integration mechanism:** MQTT carries the streams into the Unreal twin which verifies dataflow and triggers threshold alarms per channel; the full bridge DT was not yet deployed when the paper was written.
- **Why this code:** streams share the twin frame with per-channel processing, so Aligned.

**Confidence (AC3):** Medium - the prototype dataflow is explicit; the final system is design-stage.
(full-text source: Endnote)

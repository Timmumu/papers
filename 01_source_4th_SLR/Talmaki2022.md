# Talmaki, S.A et al. (2022) — Sensor Acquisition and Allocation for Real-Time Monitoring of Articulated Construction Equipment in Digital Twins

- **ID:** R538 | **Source:** Scopus | **DOI:** 10.3390/s22197635
- **Journal:** Sensors
- **Authors:** Talmaki S.A.; Kamat V.R.

## Abstract summary
The visibility available to an equipment operator on a dynamic construction site can often be blocked by various obstacles such as materials, temporary or permanent facilities, other equipment, and workers. Equipment monitoring in real-time digital twins can thus play a crucial role in accident prevention. This paper develops a scalable technical approach and presents a prototype application framework for transmitting real world sensor data to update 3D equipment models inside a graphical digital twin for concurrent visualization of a monitored construction operation. The developed framework and workflow can be extended to visualize any construction operation, as it occurs, inside a dynamic 3D world simply by outfitting the real equipment with appropriate sensors and connecting them to their virtual counterparts. The implemented proof-of-concept interface is described in the context of a…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Sensor allocation for real-time equipment DTs; strike avoidance

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| SINGLE | Only orientation-sensor data (XSens MTw on boom, stick and bucket) drive the forward-kinematic DT updates; vision references in the text are background literature, not an implemented data source. | High |

**Key evidence (AG):** Sensor acquisition and allocation for real-time monitoring of articulated construction equipment in digital twins (U Michigan): orientation sensors on backhoe loader boom/stick/bucket → real-time 3D DT visualization + proximity monitoring with preset safety thresholds → audio-visual warnings for operators; proof-of-concept for excavator operators preventing underground utility strikes; validation experiments characterize spatio-temporal discrepancies. One-way monitoring→DT visualization→warnings; no actuation and no learning loop.

*Full-text source: 04c-port*

**AH — strength & gap filled:** Addresses the micro-level gap of mapping live articulated-equipment motion into digital twins: orientation sensors (XSens MTw) on the boom, stick and bucket of a Caterpillar 430E IT backhoe drive forward-kinematic updates of a 3D twin with proximity monitoring, achieving a 0.06 m mean separation error with 0.05 m standard deviation in 15 configurations and testing audio-visual warnings against 2.0-3.0 m safety buffers.

**AI — deficiencies & future work:** Validation used a stationary backhoe in an indoor facility with a flat virtual ground model, bucket geometric differences and 0.5-degree sensor accuracy causing discrepancies; safety-buffer penetration rose with operating speed (15 to 68 percent), so dynamic tolerance zones, linear encoders, operator training, and extension to cranes, dump trucks and graders are identified as future work.

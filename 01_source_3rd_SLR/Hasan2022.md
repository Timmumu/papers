# Hasan et al. (2022) — Augmented reality and digital twin system for interaction with construction machinery

- **ID:** 3973 | **Source:** Web of Science | **DOI:** 10.1080/13467581.2020.1869557
- **Journal:** JOURNAL OF ASIAN ARCHITECTURE AND BUILDING ENGINEERING
- **Authors:** Hasan, S. M.; Lee, K.; Moon, D.; Kwon, S.; Jinwoo, S.; Lee, S.

## Abstract summary
Smart construction utilizes the latest IoT "smart" technologies, such as Cyber-Physical Systems, to aid in construction processes. A Cyber-Physical System (CPS) is an amalgamation of computation, networking and physical objects. There are various examples of CPS being employed in sectors varying from manufacturing, robotics, and smart cities. Where the application and literature are lacking, however, is construction. This paper focuses on construction machinery operation and work tracking through CPS. The relevant technologies required for creating a system with these capabilities are Augmented Reality (AR) and Digital Twin (DT). Two salient features of a CPS are real-time state knowledge and control. These are handled by the sensors and micro-controllers, respectively, allowing for bi-directional communication between the virtual models and physical objects. Remote control and tracking/…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** AR+DT CPS for construction machinery; precision & safety

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Single (one data type) | Simulation | 3 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Lab prototype of AR + Digital Twin Cyber-Physical System (DPL) for construction-machinery interaction (stationary tower-crane analogue): Arduino MCU sensor/actuator net (ultrasonic distance sensor for safety/clash detection, MPU-6050 accel/gyro) ↔ Unity3D 3D DT over Wi-Fi with bidirectional data/control (AR marker controller remotely operates servos; sensor data drives 3D model; DT latency 0.5–1.0 s). Explicitly bidirectional — virtual acts back on physical — but lab-only robotic analogue, no ML, no learning.

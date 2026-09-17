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

**Strength & gap filled (AH):** Brings bidirectional cyber-physical interaction to construction machinery where literature is scarce: a laboratory prototype of an AR and digital twin CPS using an Arduino Uno and Yun sensor and actuator net (HC-SR04 ultrasonic, MPU-6050 inertial) on a tower crane analogue, with a Unity3D server relaying serial data to a marker-based AR controller at 0.25 s command latency and a DT animation lag of 0.5 to 1.0 s.

**Deficiencies & future work (AI):** Validation is confined to a laboratory analogue of a stationary tower crane, so no quantitative on-site performance could be measured, and the MPU-6050 readings were excluded from the twin because of latency and twitching; the authors propose a proprietary MCU package and dedicated connections instead of open Wi-Fi as future work.

**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** HC-SR04 ultrasonic distance data for safety/clash detection; MPU-6050 inertial readings excluded from the twin.
- **Integration mechanism:** none - one active sensor stream drives the Unity3D twin over Wi-Fi; control commands run on the same Arduino loop but are actuator actions, not a second data type.
- **Why this code:** a single data type is effectively used, so SINGLE (AC=Single).

**Confidence (AC3):** High - the MPU-6050 exclusion is stated in the full text.
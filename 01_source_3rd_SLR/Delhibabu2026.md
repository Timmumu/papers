# Delhibabu et al. (2026) — Interconnected digital twins of subway stations for decision support systems

- **ID:** 3626 | **Source:** Scopus | **DOI:** 10.1016/j.rineng.2026.110745
- **Journal:** Results in Engineering
- **Authors:** Delhibabu, R.; Zhukova, N.; Subbotin, A.

## Abstract summary
This article examines a digital twin (DT) for complex infrastructure assets using the subway system as a case study. The proposed solution includes twins for each station, which are interconnected to interact during various operational scenarios. Existing digital twins for subway systems are examined, and their shortcomings—primarily the latency in operator information retrieval due to slow model rebuilding—are identified. The study addresses decision support during medium- and large-scale incidents requiring the synchronization of multiple departments. The authors propose a digital twin architecture based on data collected from cameras, microphones, and sensors, processed within a fog computing environment. A separate digital twin is developed for each station, capable of utilizing templates from previously built assets. An accompanying mobile application with an intelligent assistant d…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Station DTs for incident decision support; response -17.4%

## Step-3 Deep-Read Coding (Prompt B) 

**Strength & gap filled (AH):** Fills the incident-response gap of subway station digital twins: interconnected per-station twins process camera, microphone and sensor data in a fog computing environment, a fine-tuned YOLOv8 detector (mAP 0.5 of 92.4 percent) spots events shown on a mobile app with a voice assistant, and personnel response times improved by 17.4 percent versus the REPEAT platform across 50 simulated trials.

**Deficiencies & future work (AI):** Results come from simulated emergency scenarios, and continuous TCP/IP connectivity is assumed, so deep subterranean network degradation could break the fog-to-mobile pipeline; speech recognition reaches only a 14.2 percent word error rate under 85 dB noise, and the app runs only on Android and Linux; future plans include signaling and control integration to automatically stop trains and escalators.
**Fusion depth (AC1):** Co-present

**Fusion evidence (AC2):**
- **Data streams:** cameras (YOLOv8, mAP0.5 92.4%), microphones (speech recognition), environmental sensors.
- **Integration mechanism:** each modality is processed by its own pipeline in the fog environment (vision detection vs speech assistant); the full text does not describe a shared frame joining them.
- **Why this code:** multiple data types are used but each stays in its own pipeline, so Co-present; torn with Aligned, the lower level was chosen because no registration is stated (rules 3/5).

**Confidence (AC3):** Medium - separation of pipelines is clear, but a hidden time-synchronisation cannot be fully excluded from the available record.
(full-text source: Interconnected digital twins of subway stations for decision support (VIT/FRC RAS): per-station DTs interconnected to interact during operational scenarios; cameras, microphones, sensors processed in fog computing; mobile app with intelligent assistant displays detected events and answers queries via voice; event detection for hazardous situations (fire/explosion); implementation improved personnel response time by 17.4% vs REPEAT platform. One-way monitoring→event detection→decision support for operators; no actuation and no learning loop.)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Endnote

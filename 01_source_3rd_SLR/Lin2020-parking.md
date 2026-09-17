# Lin et al. (2020) — Developing WSN/BIM-Based Environmental Monitoring Management System for Parking Garages in Smart Cities

- **ID:** 3945 | **Source:** Web of Science | **DOI:** 10.1061/(ASCE)ME.1943-5479.0000760
- **Journal:** JOURNAL OF MANAGEMENT IN ENGINEERING
- **Authors:** Lin, Y. C.; Cheung, W. F.

## Abstract summary
In recent years, there have been many serious problems with air pollution (such as hazardous gases) in environmental management for parking garages of cities. These problems should be continuously improved and enhanced for smart cities. Building information modeling (BIM) has been revolutionary in construction industry applications; it integrates different kinds of construction information into a 3D digital model and can be applied in all stages of a project lifecycle. Furthermore, the wireless sensor network (WSN) is an important key technology in Internet of Things (IoT) development. In order to improve the performance of environmental monitoring management of parking garages in smart cities, this study proposes a planning approach for integration of WSN and BIM technologies and develops an advanced monitoring and control system for underground parking garage environment monitoring, ad…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** WSN/BIM DT for parking garage environmental hazard monitoring

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 3 | Semantic interoperability |

**Key evidence (AG):** WSN/BIM environmental monitoring & control system for underground parking garage (Taipei case): WSN nodes (coordinator/sensor/router/control) collect CO, temperature, humidity in real time; data transferred over self-constituted WSN and dynamically displayed on corresponding spatial components of a 3D BIM model, making the BIM a real-time DT; actuation (ventilator + flashing alarm on high CO) is performed by the WSN control node directly (sensor→control-node safety loop), not through the virtual twin; reaction ~1-2 s. BIM/DT is a one-way monitoring/visualisation layer; no ML and no learning loop.

**Strength & gap filled (AH):** Fills the planning gap for WSN and BIM integration in garage environmental monitoring: a working digital twin system with Zigbee mesh nodes (MQ-7 CO and DHT-11 temperature and humidity) that react to simulated hazardous gas within 1 to 2 s, automatically switching on ventilator and flashing alarm, with 250 m direct and over 450 m relayed communication, color-coded BIM visualization via Navisworks API, and roughly 40 percent cost saving versus handheld detectors.

**Deficiencies & future work (AI):** Validation used only three sensor locations in one Taipei garage with simulated gas, standard-gas calibration is recommended for quantitative readings, and battery capacity limits node operation to about one week. Future work includes adopting more IoT technologies and integrating BIM with AI for smarter environment management in smart cities.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** Zigbee WSN nodes (MQ-7 CO, DHT-11 temperature/humidity) in a Taipei parking garage.
- **Integration mechanism:** readings map onto matching BIM components for real-time colour display; the safety loop (ventilator + alarm, 1-2 s) is executed directly by the WSN control node, bypassing the twin.
- **Why this code:** sensor channels share the BIM asset frame but inference/actuation stays per stream, so Aligned.

**Confidence (AC3):** High - the BIM component mapping is explicit.
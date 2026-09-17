# Álvaro et al. (2025) — GUIDE2FR: A smart monitoring platform with a digital twin of a firefighter training tower for emergency scenarios

- **ID:** 3668 | **Source:** Scopus | **DOI:** 10.1016/j.iot.2025.101768
- **Journal:** Internet of Things (The Netherlands)
- **Authors:** Álvaro, M. D.; Novak, R.; Barbosa, P. R. F.; Capelo, I. C.; Gallego, M.; Rodriguez-Sanchez, M. C.

## Abstract summary
This paper describes the implementation of a digital twin for buildings to enhance the emergency response capabilities of first responder teams, including firefighters, police, and emergency medical services. The proposed platform improves the planning of preventive evacuation strategies and supports real-time operational decisions during emergencies. It integrates wireless monitoring beacons, specifically designed for hostile environments, a cloud-based data management system, and a predictive model to monitor environmental air quality parameters, which are critical during emergency scenarios. The platform uses a digital twin to simulate the building's behavior, incorporating multimedia content and time series graphs to enhance situational awareness and decision-making. Real-time building data are seamlessly integrated with predictive models generated from smart building sensors, offeri…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Building DT for emergency response & evacuation safety

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** GUIDE2FR emergency-monitoring DT of a firefighter training tower (Alcorcón): Wi-Fi/LoRa beacon network (temp, humidity, CO2, TVOC) + RTSP video synchronised in a Grafana plugin; offline-trained ML forecasting pipeline (SVR/RF/Huber/GPR, forward-chaining CV, tested on 4 beacons at Fire Station 9) visualised in the DT; one-way data flow to human decision-makers, no actuation and no online learning loop.

**Strength & gap filled (AH):** Fills the gap between fire-safety DT research and operational emergency response: a functioning building DT (GUIDE2FR) fusing Wi-Fi/LoRa environmental beacons with live RTSP video in a Grafana plugin, plus an offline-trained ML forecasting pipeline (SVR, Huber, Random Forest, Gaussian Process, forward-chaining CV, adaptive ensemble) tested on data from four beacons during firefighter training exercises at Fire Station 9 in Madrid.

**Deficiencies & future work (AI):** No actuation or bidirectional link to building systems: forecasting models are offline-trained and never updated online. The platform relies on proprietary ArcGIS, assumes a reliable wireless network, and sensor accuracy under extreme conditions is unverified; future work targets open-source visualization and integration with more real assets for active response and evacuation mechanisms.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** Wi-Fi/LoRa beacon time series (temperature, humidity, CO2, TVOC) + RTSP surveillance video on a firefighter training tower.
- **Integration mechanism:** each video segment is timestamped and stored by the Video Management Module, and the custom Grafana plugin cross-references RTSP streams with MySQL sensor time series, giving both a shared temporal frame; the ML forecasting pipeline (SVR/RF/Huber/GPR) runs on sensor series only.
- **Why this code:** the two data types are linked by a shared timestamp frame while inference stays per type, so Aligned.

**Confidence (AC3):** High - the timestamped video-to-MySQL synchronisation is described verbatim in the full text.
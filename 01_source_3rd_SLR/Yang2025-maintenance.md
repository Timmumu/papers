# Yang et al. (2025) — Design and Validation of a Real-Time Maintenance Monitoring System Using BIM and Digital Twin Integration

- **ID:** 3874 | **Source:** Web of Science | **DOI:** 10.3390/buildings15081312
- **Journal:** BUILDINGS
- **Authors:** Yang, S. W.; Lee, Y. K.; Kim, S. A.

## Abstract summary
This study presents a real-time monitoring system integrating Building Information Modeling (BIM) and digital twin technology to enhance maintenance efficiency and safety in urban infrastructure. Unlike conventional periodic inspections, which miss dynamic changes and increase costs, this system uses a BIM model at LOD 400 for a solar-powered noise barrier tunnel integrated with the Wansan Tunnel in South Korea. It incorporates IoT sensor data, including vibration, tilt, light, air quality, and water detection, which are synchronized via the Autodesk Forge API, and WebSockets and visualized on a web-based dashboard. A demonstration from 22 October to 7 November 2024 confirmed that this system had stable data transmission, with light sensor rates exceeding 90%, and enabled the detection of anomalies such as irregular illuminance and structural shifts, thereby supporting informed maintenan…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM+DT real-time maintenance monitoring of tunnel; anomaly detection

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** Real-time maintenance monitoring system using BIM and digital twin integration (Sungkyunkwan U): LOD 400 BIM model of solar-powered noise barrier tunnel + IoT sensors (vibration, tilt, light, air quality, water detection) synchronized via Autodesk Forge API + WebSockets; web-based dashboard for visualization; anomaly detection via two-tiered approach (device alerts + post-processed trend analysis); validated on Wansan Tunnel in South Korea. One-way monitoring→visualization→maintenance decisions; no actuation and no learning loop.


**Strength & gap filled (AH):** Addresses the gap between static periodic inspections and real-time infrastructure maintenance: a LOD 400 BIM model of a solar-powered noise barrier tunnel integrated with the Wansan Tunnel in Jeonju is synchronized through Autodesk Forge API and WebSockets with vibration, tilt, light, air quality, and water detection sensors, achieving over 90% light-sensor transmission and detecting illuminance and structural anomalies during a 17-day demonstration.

**Deficiencies & future work (AI):** Nuanced anomalies such as gradual tilt drift require offline post-processing rather than live dashboard analytics; air quality sensors lost up to 30.65% of expected records and one water sensor never transmitted; only one site and asset type was validated. Future work embeds predictive analytics in the live platform, adds buffering and failover mechanisms, and extends validation to bridges and tunnels.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** five IoT sensor types on a solar-powered noise-barrier tunnel (Wansan Tunnel, 17-day demonstration).
- **Integration mechanism:** Forge API + WebSockets attach the sensor streams to BIM elements for dashboard visualisation; device alerts and post-processed trend analysis act per channel.
- **Why this code:** streams share the BIM asset frame with per-channel inference, so Aligned.

**Confidence (AC3):** High - the Forge/WebSocket synchronisation is explicit.
(full-text source: Endnote)

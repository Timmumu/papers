# Pham et al. (2026) — Designing a BIM-enhanced digital twin architecture for construction pollution management in building renovation projects

- **ID:** 3881 | **Source:** Web of Science | **DOI:** 10.1080/15623599.2026.2651946
- **Journal:** INTERNATIONAL JOURNAL OF CONSTRUCTION MANAGEMENT
- **Authors:** Pham, T. A.; Ioannou, P. G.; Likhitruangsilp, V.

## Abstract summary
Pollution created by building renovation activities poses a hazard to human health and the proximate environment. Integrating building information modelling (BIM) with digital twin (DT) technology offers a promising means for real-time monitoring and enabling collaboration among project participants. However, it is challenging to transform the BIM models of a renovated facility into a DT platform for monitoring and reporting construction pollution on-site. This paper proposes a BIM-enhanced DT architecture for managing construction pollution in building renovation projects. The platform entails five key components: physical entity (PE), virtual model (VM), DT data (DD), services (Ss), and connections (CNs). To resolve ambiguities in information requirements, a novel Level of Information Need (LOIN) framework for BIM-enhanced DT was established. The interplay among LOIN, Level of Developm…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** BIM-enhanced DT for renovation pollution (health hazard) management

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | BIM-to-Digital-Twin architecture |

**Key evidence (AG):** BIM-enhanced DT architecture for construction pollution management in renovation (auditorium, Chulalongkorn Univ): five components (PE/VM/DD/Ss/CN), novel hybrid LOIN-LOD framework (LOD-G 200 as-is scan-to-BIM → LOD-G 350 as-designed) defining as-needed BIM information for DT; six IoT sensor clusters (PM2.5, CO2, noise, vibration) streamed via MQTT/Firebase into Node-RED rule-based engine with threshold alerts + React/Autodesk Forge dashboard; 1-s real-time monitoring. Bidirectional feedback/actuator control described but "implementation remains limited" — no automated actuation, no ML, no learning loop.

**Strength & gap filled (AH):** Proposes a BIM-enhanced digital twin architecture for construction pollution management in building renovation, defined by five components (physical entities, virtual models, DT data, services, connections) and a hybrid LOIN-LOD framework specifying minimum modelling requirements; a Chulalongkorn University auditorium pilot integrated six IoT sensor clusters (noise, PM2.5, CO2, vibration) with MQTT, Firebase, Node-RED threshold alerts and a React plus Forge dashboard, with 1-second data transmission.

**Deficiencies & future work (AI):** The actuator and HVAC responses to threshold breaches are designed but not implemented, semantic ontology integration remains unexplored, and the pilot lacks construction progress tracking and complaint channels; low-cost sensor reliability and a calibration loop are open issues, while Forge visualization of large datasets caused performance bottlenecks. Future work targets cognitive DT components, semantic standards, AI analytics and complaint management.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** noise, PM2.5, CO2 and vibration IoT clusters on a Chulalongkorn University auditorium pilot (1-s transmission).
- **Integration mechanism:** sensors are linked to BIM assets (hybrid LOIN-LOD framework) and rules run per channel in Node-RED with threshold alerts; actuator/HVAC responses are designed but not implemented.
- **Why this code:** streams share the BIM asset frame while inference stays per channel, so Aligned.

**Confidence (AC3):** High - the MQTT/Firebase/Node-RED linkage is explicit.
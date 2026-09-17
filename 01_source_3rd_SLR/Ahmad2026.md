# Ahmad et al. (2026) — Lessons Learned from the Real-World Deployment of Multisensor Fusion for Proactive Work Zone Safety Application

- **ID:** 3756 | **Source:** Scopus | **DOI:** 10.1177/03611981261441281
- **Journal:** Transportation Research Record
- **Authors:** Ahmad, M. U.; Dasgupta, S.; Rahman, M.; Khan, S.; Haque, M. W.; Saba, S. R.; Bodoh, D.; Huynh, N.; Zhao, L.; Ozguven, E. E.

## Abstract summary
Proactive safety systems that anticipate and mitigate traffic risks before incidents occur are increasingly recognized as essential for improving work zone safety. Unlike traditional reactive safety approaches, proactive systems rely on real-time sensing, trajectory prediction, and intelligent infrastructure to detect potential safety hazards. Existing simulation-based and real-world deployment studies often overlook and rarely discuss the practical challenges associated with deploying such proactive systems in operational settings, particularly those involving roadside infrastructure enabled multisensor integration and fusion. This study addresses that gap by presenting deployment insights and technical lessons learned from a real-world implementation of a proactive safety system utilizing multiple sensors mounted on a roadside infrastructure at an active bridge repair work zone along t…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Work-zone safety; predictive DT framework for conflict detection

## Step-3 Deep-Read Coding (Prompt B) — full text via arXiv:2508.01599 (GREEN OA preprint)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | DfS | None | Other / Mixed | Multi | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Real deployment of LiDAR + radar + camera roadside sensing with edge computing at an active bridge-repair work zone (N-2/US-75, Lincoln NE); calibration and RTK-GNSS/IMU validation give lane-level fused trajectories. The Predictive Digital Twin (PDT) framework — Digital Shadow (fused real-time state) + Digital Sibling (multi-modal trajectory prediction, e.g. HPNet/QCNet), TTC/PET/min-distance conflict metrics, C-V2X BSM/PSM and wearable alerts — is **proposed as architecture (Fig. 15) but not implemented**; only the shadow layer was validated. Hence Tier 2 (one-way), AA = None (no self-improvement mechanism for the twin; prediction models are fixed components).

**Strength & gap filled (AH):** Fills the gap between work zone safety DT research and real-world deployment: LiDAR+radar+camera fusion validated with RTK-GNSS at a real work zone achieving lane-level accuracy, feeding a predictive DT framework pairing a Digital Shadow and Digital Sibling with TTC/PET conflict metrics and C-V2X warnings for proactive safety.

**Deficiencies & future work (AI):** Deployment lessons rather than controlled validation: one real work zone, and the predictive framework (conflict metrics, C-V2X warnings) stays at framework level without demonstrated closed-loop actuation; no explicit future work is stated.

**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** LiDAR, radar and camera data deployed together at a real work zone.
- **Integration mechanism:** the multisensor fusion deployment is validated against RTK-GNSS at lane-level accuracy and feeds TTC/PET conflict metrics; the predictive Digital Shadow + Digital Sibling framework with C-V2X warnings is proposed but not implemented.
- **Why this code:** jointly deployed and jointly validated multi-sensor streams make the safety output depend on all three types simultaneously, so Fused.

**Confidence (AC3):** Medium - the full text is the arXiv OA preprint (staged from the Endnote attachment), reporting deployment lessons rather than a peer-reviewed validation.
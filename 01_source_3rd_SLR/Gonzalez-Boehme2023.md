# Gonzalez-Boehme et al. (2023) — Mixed Reality for Safe and Reliable Human-Robot Collaboration in Timber Frame Construction

- **ID:** 4005 | **Source:** Web of Science | **DOI:** 10.3390/buildings13081965
- **Journal:** BUILDINGS
- **Authors:** Gonzalez-Boehme, L. F.; Valenzuela-Astudillo, E.

## Abstract summary
In the field of construction, human-robot collaboration and mixed reality (MR) open new possibilities. However, safety and reliability issues persist. The lack of flexibility and adaptability in current preprogrammed systems hampers real-time human-robot collaboration. A key gap in this area lies in the ability of the robot to interpret and accurately execute operations based on the real-time visual instructions and restrictions provided by the human collaborator and the working environment. This paper focuses on an MR-based human-robot collaboration method through visual feedback from a vision-based collaborative industrial robot system for use in wood stereotomy which we are developing. This method is applied to an alternating workflow in which a skilled carpenter lays out the joinery on the workpiece, and the robot cuts it. Cutting operations are instructed to the robot only through l…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Robot DT for motion preview & safe workspace entry; construction HRC

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Mixed Reality-based human-robot collaboration for timber frame construction (USM Chile): vision-based collaborative industrial robot system for wood stereotomy; carpenter lays out joinery with conventional marks, robot cuts based on visual interpretation; digital twin of robot previsualizes all motions for task validation and safety (when to enter workspace); real-time visual feedback between human and robot; 3D model of cut shape constructed from vision system data. Bidirectional human-robot collaboration with robot executing physical tasks → Tier 3; no ML learning loop (rule-based mark interpretation).


**Strength & gap filled (AH):** Addresses the real-time human-robot communication gap in timber frame construction: a vision-based collaborative robot interprets the layout marks drawn by a carpenter as cutting operations, and a robot digital twin shown through HoloLens 2 mixed reality previews all motions, danger zones and collision warnings so the carpenter can safely time entry to the collaborative workspace under ISO/TS 15066.

**Deficiencies & future work (AI):** Only robot-operator collision risk is detected automatically; tracking of other workspace elements must still be added, and the system awaits calibration of assembly tools and tests with real carpenters. Future work includes defining shared human-robot spaces, optimizing auxiliary trajectories and tool orientations, and handling robot payload constraints.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** vision-system data (layout-mark interpretation) + robot kinematic state mirrored in the DT.
- **Integration mechanism:** the 3D cut model is constructed from vision data and mapped into the robot DT shown through HoloLens 2, giving both streams one robot-centred reference frame; safety zoning and motion preview operate on the DT.
- **Why this code:** two data types share a common frame (robot kinematics) with per-type processing, so Aligned.

**Confidence (AC3):** High.
(full-text source: Endnote)

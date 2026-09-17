# Wu et al. (2021) — Research on Digital Twin Construction and Safety Management Application of Inland Waterway Based on 3D Video Fusion

- **ID:** 3530 | **Source:** Scopus | **DOI:** 10.1109/ACCESS.2021.3101653
- **Journal:** IEEE Access
- **Authors:** Wu, Z.; Ren, C.; Wu, X.; Wang, L.; Zhu, L.; Lv, Z.

## Abstract summary
The digital twin can reconstruct the scenes of real traffic operation of inland waterways in virtual space, giving birth to new ideas for the digital transformation and upgrading of water safety management. Aiming at the problems of video fragmentation, sub-system data separation and untimely emergency response in the current inland waterway safety monitoring, this paper proposes a new method for reconstructing and applying a digital twin of inland waterways based on 3D video fusion which consists of four parts: (1) Combining drone tilt photography and BIM modeling technology to construct a three-dimensional scene model of inland waterways; (2) Proposing a multi-channel video three-dimensional registration and rendering method to integrate in real time discrete surveillance videos of different angles of view with three-dimensional scene model to establish the spatial correlation between …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Inland waterway DT with 3D video fusion; safety management

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | Mentioned only | Perception / Computer Vision | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Inland waterway digital twin based on 3D video fusion (China Academy of Transportation Sciences): drone tilt photography + BIM build a static 3D waterway scene; multi-channel surveillance-video 3D registration/rendering fuses discrete videos into the scene (2D/3D linkage); multi-source IoT sensing data (AIS, etc.) integrated into the digital twin scene for water safety management (facility management, daily monitoring, illegal-evidence collection, emergency response); demonstrated on Changhu-Shen Line segment. One-way fusion/monitoring/visualisation for managers; "scene iteration driven by online data" is stated as next-step future work — not yet implemented, no learning loop.

**Strength & gap filled (AH):** Addresses video fragmentation, subsystem data separation (AIS, smart bayonet) and untimely emergency response in inland waterway safety monitoring: drone tilt photography plus BIM build a static scene, multi-channel video is 3D-registered and fused with 25 cameras, and multi-source IoT data form a digital twin demonstrated on a Changhu-Shen Line segment with two- and three-dimensional linkage.

**Deficiencies & future work (AI):** The platform is a monitoring and visualization system without predictive analytics or actuation, validated on only one waterway segment; future work focuses on digital twin scene iteration driven by online data, simulation and fusion drawing of water traffic operation, and updating of the water environment from monitoring data.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** 25 surveillance-video channels + drone tilt-photography/BIM scene + AIS and smart-bayonet IoT data (Changhu-Shen Line).
- **Integration mechanism:** 3D registration renders the video into the shared scene with 2D/3D linkage, and IoT sources are displayed for facility monitoring, evidence collection and emergency response; online-data-driven scene iteration is future work.
- **Why this code:** streams share the registered scene frame while analysis stays per source, so Aligned.

**Confidence (AC3):** High - the video 3D-registration mechanism is explicit.
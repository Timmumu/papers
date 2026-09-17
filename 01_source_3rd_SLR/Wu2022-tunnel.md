# Wu et al. (2022) — A Novel Method for Tunnel Digital Twin Construction and Virtual-Real Fusion Application

- **ID:** 3656 | **Source:** Scopus | **DOI:** 10.3390/electronics11091413
- **Journal:** Electronics (Switzerland)
- **Authors:** Wu, Z.; Chang, Y.; Li, Q.; Cai, R.

## Abstract summary
Tunnels play important roles in integrated transport infrastructure. A digital twin reproduces a real tunnel scene in virtual space and provides new means for tunnel digital maintenance. Aiming at the existing problems of video fragmentation, separation of video and business data, and lack of two-and three-dimensional linkage response methods in tunnel digital operation, in this paper, we propose a novel method for tunnel digital twin construction and virtual-real integration operation. Firstly, the digital management requirements of tunnel operations are systematically analyzed to clarify the purpose of digital twin construction. Secondly, BIM technology is used to construct a static model of the tunnel scene that conforms to the real tunnel main structure. Thirdly, a three-dimensional registration and projection calculation method is proposed to integrate tunnel surveillance video into…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Tunnel DT construction + virtual-real fusion; accident rescue & emergency

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Tunnel digital twin construction and virtual-real fusion application (China Academy of Transportation Sciences): BIM technology constructs static tunnel scene model; 3D registration/projection integrates multi-channel surveillance video into 3D virtual scene in real time; multi-source sensing data fused for traffic flow, accident rescue, facility management, emergency response; management model for tunnel operations. One-way monitoring→virtual-real fusion→management; no actuation and no learning loop.


**Strength & gap filled (AH):** Fills the gap of fragmented tunnel surveillance video, separation of video and business data, and missing two- and three-dimensional linkage in tunnel digital operations: a BIM static scene model fused in real time with multi-channel surveillance video through 3D registration and projection plus multi-source IoT sensing data, demonstrated on a tunnel in China for traffic flow, accident rescue, facility management, and emergency response.

**Deficiencies & future work (AI):** Camera position and attitude must be calibrated one by one, two-way interaction between the virtual and real models is not yet realized, and the video data structure algorithm lacks integration; field cameras have low resolution and incomplete coverage. Future work includes online data-driven 3D scene updates, data-driven traffic operation simulations, and predictive deduction.
**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** multi-channel surveillance video + BIM static scene + multi-source IoT sensing data.
- **Integration mechanism:** 3D registration/projection places video streams into the shared 3D scene (virtual-real fusion), while traffic-flow, accident-rescue and facility-management services analyse per source.
- **Why this code:** streams share one registered scene frame with per-source services, so Aligned.

**Confidence (AC3):** High - the 3D registration mechanism is explicit.
(full-text source: Endnote)

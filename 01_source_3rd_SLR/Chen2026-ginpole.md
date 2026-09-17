# Chen et al. (2026) — Digital Twin-Enabled Robust Parallel Control of Construction Engineering Equipment Under Uncertainty

- **ID:** 3953 | **Source:** Web of Science | **DOI:** 10.3390/buildings16101982
- **Journal:** BUILDINGS
- **Authors:** Chen, R.; Xu, H. T.; Zhang, L. M.; Rong, J. G.; Wei, C.; Chang, H.; Zhang, H. Y.

## Abstract summary
This paper proposes a digital twin framework for robust parallel control of the mobile gin pole in ultra-high voltage (UHV) transmission line construction, aiming to improve safety and operational efficiency under uncertain conditions. The new framework integrates kinetic analysis, machine learning models, and multi-objective optimization algorithms to address the challenges of heavy-lifting operations in complex terrains. The method conducts finite-element kinetic analysis based on the actual structure of the mobile gin pole. A Tyrannosaurus Rex Optimization Algorithm (TROA) is employed to enhance the performance of the Extra Randomized Trees (ET) model for predicting key parameters such as maximum axial stress and shear stress. The framework leverages the Non-Dominated Sorting Genetic Algorithm III (NSGA-III) to optimize safety and efficiency metrics by adjusting key control parameters…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT for gin-pole lifting; safety risk reduced 32%

## Step-3 Deep-Read Coding (Prompt B) — full text via MDPI Buildings (GOLD OA, mdpi-res mirror)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional) | 0 | 1 | 0 | DfS | Mentioned only | Other / Mixed (TROA-ET + NSGA-III + FEM) | Multi | Single case study | 4 | Design for Safety |

**Key evidence (AG):** DT-enabled robust parallel control of a mobile gin pole in UHV transmission-line construction. FEM kinetic analysis converted into a TROA-optimised Extra-Trees surrogate (R2 0.9642 for max axial/shear stress); NSGA-III co-optimises safety and efficiency; embedded in a DT parallel-control architecture (perception, prediction, guidance). Real 110 kV project with bidirectional 4G/MQTT link over CANopen (data + control commands); safety risk reduced up to 32.3%, efficiency +42.7%. Surrogate is offline-trained; self-improvement only framed as architecture potential.

**Strength & gap filled (AH):** Addresses robust parallel control of construction equipment under uncertainty: a mobile gin pole digital twin for UHV construction embeds finite-element kinetic analysis with a TROA-ET surrogate model (R2 0.9642) and NSGA-III safety-efficiency optimisation within a DT parallel-control architecture supported by bidirectional 4G and MQTT links.

**Deficiencies & future work (AI):** The available record states no explicit future work; validation is documented only for the mobile gin pole application, and whether the TROA-ET surrogate is updated online, transferred to other equipment types, or tested against field disturbances beyond the stated scenario is not established.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** FEM kinetic analysis outputs, TROA-ET surrogate predictions (R2 0.9642), and CANopen control/operational commands over 4G/MQTT.
- **Integration mechanism:** the measured operational loop and the offline surrogate share the parallel-control DT and its communication channel, yet each is computed separately; NSGA-III optimisation consumes surrogate outputs on a real 110 kV project.
- **Why this code:** streams are linked through the common DT control channel but no fused multi-source inference is described, so Aligned (downgrade from Fused per rule 5).

**Confidence (AC3):** Medium - based on the available MDPI record; no staged full text exists for deeper verification.
# Wang et al. (2024) — Enabling Building Information Model-driven human-robot collaborative construction workflows with closed-loop digital twins

- **ID:** 3779 | **Source:** Scopus | **DOI:** 10.1016/j.compind.2024.104112
- **Journal:** Computers in Industry
- **Authors:** Wang, X.; Yu, H.; McGee, W.; Menassa, C. C.; Kamat, V. R.

## Abstract summary
The introduction of assistive construction robots can significantly alleviate physical demands on construction workers while enhancing both the productivity and safety of construction projects. Leveraging a Building Information Model (BIM) offers a natural and promising approach to driving robotic construction workflows. However, because of uncertainties inherent in construction sites, such as discrepancies between the as-designed and as-built components, robots cannot solely rely on a BIM to plan and perform field construction work. Human workers are adept at improvising alternative plans with their creativity and experience and thus can assist robots in overcoming uncertainties and performing construction work successfully. In such scenarios, it is critical to continuously update the BIM as work processes unfold so that it includes as-built information for the ensuing construction and …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Closed-loop DT for BIM-driven human-robot workflows; as-built updating

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** BIM-driven closed-loop digital twin framework for human-robot collaborative construction (TAMU/U Michigan): BIM drives robot functions; robot adaptively adjusts plans based on actual site conditions; human co-worker oversees and intervenes (change task sequence, workspace geometry, new motion plan); as-built information sent back to BIM forming closed-loop; drywall installation case study + Gazebo simulation + physical robotic arm experiments. Bidirectional closed-loop — BIM updated with as-built data → Tier 3; no learning loop (adaptation is rule-based, not learning).


**Strength & gap filled (AH):** Closes the missing loop between BIM and robotic construction: a Rhino-based BIM with layered shop-drawing data drives a KUKA KR120 robot through ROS and MoveIt, automatically generated Unity digital twins let humans approve plans and intervene, robot-proposed adaptations resolve parent and nearby-object deviations, and sensed as-built data are written back to the BIM, verified on a drywall installation case and block pick-and-place tests with 100 percent success at 10 mm gaps.

**Deficiencies & future work (AI):** Laboratory-only validation on a 1:2 scale with one slow robot at 3 to 7 percent speed, AprilTag localization errors causing collisions at 1 mm gaps, manually authored BIM sequence and gripping data, and no support for deformable or fluid materials. Future work includes continuous component tracking, a second arm with vacuum gripping, computational design of fabrication data, force-feedback control, and efficiency studies.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** Rhino BIM geometry + AprilTag/vision localisation + sensed as-built data (KUKA KR120, drywall + block pick-and-place).
- **Integration mechanism:** robot-proposed adaptations resolve parent and nearby-object deviations by combining BIM, sensing and current state, and sensed as-built data are written back into the BIM, closing the loop (100% success at 10 mm gaps).
- **Why this code:** motion-planning output depends on multiple data types simultaneously and the loop is bidirectional, so Fused.

**Confidence (AC3):** High - the BIM-sensing closed loop is explicit.
(full-text source: Endnote)

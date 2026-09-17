# Wang et al. (2021) — Interactive and Immersive Process-Level Digital Twin for Collaborative Human-Robot Construction Work

- **ID:** 3985 | **Source:** Web of Science | **DOI:** 10.1061/(ASCE)CP.1943-5487.0000988
- **Journal:** JOURNAL OF COMPUTING IN CIVIL ENGINEERING
- **Authors:** Wang, X.; Liang, C. J.; Menassa, C. C.; Kamat, V. R.

## Abstract summary
Human cognition plays a critical role in construction work, particularly in the context of high-level task planning and in-field improvisation. On the other hand, robots are adept at performing numerical computation and repetitive physical tasks with precise motion control. The unstructured and complex nature of construction environments and the inability to maintain tight tolerances in assembled workpieces pose several unique challenges to the wide application of robots in construction work. Thus, the robotization of field construction processes is best conceived as a collaborative human-robot endeavor that takes advantage of both human and robot intelligence as well as robots' physical operation capabilities to overcome uncertainties and successfully perform useful construction work onsite. This paper proposes an interactive and immersive process-level digital twin (I2PL-DT) system in …

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Immersive process-level DT for human-robot construction; safety supervision

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Design for Safety |

**Key evidence (AG):** Interactive and immersive process-level digital twin (I2PL-DT) in VR for collaborative human-robot construction work (Univ. of Michigan): human in VR does high-level task planning/supervision and trajectory guidance; KUKA mobile robotic arm (emulator) does sensing, motion planning (SBT/motion-plan generation, collision-free) and physical execution via ros_control + PID to real actuators; seamless bidirectional communication between human and robot with real-time robot status supervision; augmented telepresence prevents workers from exposure to on-site hazards (safety benefit); drywall installation case with imperfect framing, 20-subject human-in-the-loop study. Genuine virtual→physical robot control → Tier 3; no ML learning loop.

**Strength & gap filled (AH):** Addresses the gap between robot teleoperation and safe collaborative construction: the I2PL-DT couples immersive VR with a ROS-connected KUKA arm so workers without programming skills perform high-level task planning, preview and approve collision-free motions, and supervise execution with bidirectional communication, verified on a drywall installation case with imperfect framing and a 20-subject human-in-the-loop study reporting positive usability.

**Deficiencies & future work (AI):** The arm keeps a fixed pose while its base moves, execution halts and waits for humans when obstacles appear, material positions are assumed known, and point-cloud processing causes delays; verification is mostly simulated rather than on a real site. Future work targets dynamic arm pose adjustment, autonomous path adaptation, vision-based material detection, real-time performance, and long-term human factors studies on physical KUKA KR120 arms.

**Fusion depth (AC1):** Aligned

**Fusion evidence (AC2):**
- **Data streams:** human VR high-level task plans/trajectory guidance + KUKA robot state via ros_control/PID (drywall installation case).
- **Integration mechanism:** bidirectional communication synchronises the VR view with the robot state for supervision; SBT/motion planning and physical execution are separate stages of the loop.
- **Why this code:** the two streams share the robot-state frame with per-stage processing, so Aligned.

**Confidence (AC3):** High - the bidirectional synchronisation is explicit.
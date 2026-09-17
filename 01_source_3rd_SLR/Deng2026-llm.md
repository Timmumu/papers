# Deng et al. (2026) — Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Allocation in Construction

- **ID:** 3760 | **Source:** Scopus | **DOI:** 10.1109/TASE.2026.3697962
- **Journal:** IEEE Transactions on Automation Science and Engineering
- **Authors:** Deng, M.; Fu, B.; Li, L.; Wang, X.

## Abstract summary
Multi-robot systems are emerging as a promising solution to the growing demand for productivity and safety across industrial sectors. However, effectively coordinating multiple robots in dynamic and uncertain environments, such as construction sites, remains a challenge, particularly due to unpredictable factors like material delays, unexpected site conditions, and weather-induced disruptions. To address these challenges, this study proposes an adaptive task allocation framework that strategically leverages the synergistic potential of Digital Twins, Integer Programming (IP), and Large Language Models (LLMs). The multi-robot task allocation problem is formally modeled using IP, considering task dependencies, robot heterogeneity, scheduling constraints, and replanning needs. A narrative-driven schedule adaptation mechanism is introduced, where unstructured natural language inputs are inte…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Closed-loop site DT + LLM; productivity & safety motivation

## Step-3 Deep-Read Coding (Prompt B) 

**Strength & gap filled (AH):** Addresses static, code-bound multi-robot scheduling: a closed-loop digital twin in Unity, synchronized with ROS and Gazebo, supports integer-programming task allocation whose constraints are updated by an LLM interpreting plain-language site narratives, achieving over 97 percent constraint and parameter extraction accuracy with GPT-4.1, optimal plans within about one second and 0.08-second replanning across 1024 scenarios of 27 tasks and 15 robots.

**Deficiencies & future work (AI):** Validated only in simulation: Gazebo idealizes robot-human collaboration and material handling, human worker actions are not modeled, and the LLM is limited to constraint extraction; extending to further construction scenarios, proactive conflict detection and pre-optimization reasoning are future work, with physical robot deployment still pending.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** natural-language site narratives (text) + synchronised robot/operation state in the Unity-ROS-Gazebo DT.
- **Integration mechanism:** LLM-extracted constraints (97% accuracy with GPT-4.1) are fed into the integer-programming allocator whose output depends on both the textual constraints and the live DT state; replanning runs in about 0.08 s.
- **Why this code:** a model whose output depends on two data types simultaneously (text + system state), so Fused; demonstrated across 1024 scenarios.

**Confidence (AC3):** High - the LLM-constraint-to-optimiser mechanism is explicit, though validation is simulation-only.
(full-text source: Adaptive multi-robot task allocation framework (UTK/Amazon/TAMU): DT system enables real-time synchronization between physical operations and digital representations as user interface, creating closed-loop feedback; Integer Programming models task allocation (dependencies, heterogeneity, scheduling, replanning); LLM interprets natural-language inputs to autonomously update optimization constraints (97% accuracy in constraint/parameter extraction) without manual programming; case study demonstrates computational efficiency and LLM reasoning. Closed-loop feedback + LLM-based constraint adaptation → Tier 3; no learning loop (LLM is inference-time, not self-improving).)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Transformer / Large Language Model (LLM) | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Endnote

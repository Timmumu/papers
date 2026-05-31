---
ref: "[2]"
citekey: "Akhavian2025"
title: "Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework"
authors: "R. Akhavian, M. Amani, J. Mootz, R. Ashe, B. Beheshti"
year: 2025
journal: "arXiv preprint arXiv:2509.20705"
zotero_key: "7REV8TWX"
zotero_status: verified
last_verified: "2026-05-25"
tags: ["BIM-to-DT", "DfS", "Perception", "Verified"]
---

# Akhavian2025 — BIM2RDT (Robot-Ready Site Digital Twin, arXiv preprint)

| Field | Value |
|-------|-------|
| **Ref** | [2] |
| **Authors** | R. Akhavian, M. Amani, J. Mootz, R. Ashe, B. Beheshti |
| **Year / Venue** | 2025 / arXiv:2509.20705 (preprint, not peer-reviewed) |
| **Zotero** | 7REV8TWX |

## Abstract ^sec-abstract

BIM2RDT proposes an *agentic AI safety-first* framework that takes static, design-time BIM models and converts them, in real time on a robotic platform, into *Robot-Ready Site Digital Twins*. The core technical contribution is **SG-ICP (Semantic-Gravity Iterative Closest Point)** — an ICP variant that fuses semantic class labels and the gravity vector to overcome ICP's well-known sensitivity to initial pose in cluttered, ambiguous construction scenes. The framework couples perception with an agentic orchestrator that performs as-built verification and triggers safety alerts (e.g., hand-arm vibration (HAV) daily limits). ^p1

## Introduction & Background ^sec-intro

Authors frame the gap as: BIM provides a rich *a priori* model of "what should be there," but cannot reflect what *is* there during construction; conventional point-cloud → BIM alignment (vanilla ICP) is brittle under occlusion, ambiguous features (scaffolding, equipment stacks), and viewpoint diversity typical of active construction sites. ^p1

The proposed answer is to make the *twin* both robot-mountable and agentic — i.e., capable of autonomous decisions about navigation, monitoring, and safety alerts. Safety-first means the orchestrator treats compliance alerts (e.g., HAV limit) as non-overridable inner loops, while perception/planning are outer loops. ^p2

## Method ^sec-method

1. **SG-ICP algorithm:** classical point-to-plane ICP is augmented with (a) a semantic term penalising matches across semantic classes and (b) a gravity term enforcing physically plausible orientations (upright objects resistant to tipping). ^p1
2. **Agentic AI orchestrator:** an LLM-style planner mediates between perception (SG-ICP alignment), BIM (priors), and safety sensors (e.g., HAV monitors), invoking tools and emitting warnings. ^p2
3. **Validation scenarios:** 4 controlled scenarios benchmark SG-ICP vs vanilla ICP across viewpoint variation; a robot exploration experiment validates OOI (object-of-interest) alignment; an HAV-integration scenario demonstrates safety-loop closure. ^p3

## Key Findings ^sec-results

- SG-ICP substantially outperforms vanilla ICP in scenarios with ambiguous features or poor initial poses (Scenarios 1 and 3 show the largest gains). ^f1
- Robust as-built verification reduces costly rework by enabling early detection of geometric deviations. ^f2
- The agentic orchestrator successfully closes the loop between perception and safety: HAV warnings fire automatically when daily-limit thresholds are crossed in the integrated DT. ^f3
- Physically consistent orientations (gravity term) support safer autonomous robot navigation. ^f4

## Discussion & Implications ^sec-discussion

The authors argue BIM2RDT operationalises the *cognitive* DT vision for AECO: perception is no longer raw point-cloud crunching but semantics-informed alignment, and the twin actively reasons (via the agentic orchestrator) rather than just rendering data. ^p1

**Limitations** the authors flag explicitly: experiments are in controlled settings (scalability to large dynamic sites unproven); the framework depends on high-quality BIM priors and degrades with incomplete/poor digital models; real-time data synchronisation and conflict resolution across heavy streams not yet fully addressed. ^p2

## Conclusion ^sec-conclusion

BIM2RDT integrates semantic-gravity ICP with an agentic AI orchestrator and safety sensors to convert design-time BIM into a Robot-Ready Site Digital Twin that performs as-built verification and proactive safety enforcement. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance

- **Lifecycle stage:** construction (active monitoring) bridging to operation.
- **Cognitive capability:** perception (SG-ICP) + agentic reasoning (LLM orchestrator) + safety-first action loops — a textbook example of the SLR's "cognitive DT" criteria.
- **Why cited in LR_cc.md:** Akhavian2025 is the principal exemplar in the manuscript's argument that 2024-2025 marks the shift from BIM-as-database to *agentic, perception-grounded* DTs. It substantiates the claim that semantic priors + autonomous safety enforcement are the defining 2025-era capabilities, and exemplifies how a preprint can already document an end-to-end agentic safety stack.
- **Caveat:** arXiv preprint — flag as not yet peer reviewed when used in the manuscript.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| 2024-2025 emergence of agentic-AI DTs in AECO | #^sec-abstract, #^p2 (intro) |
| Semantic + physical priors needed for robust as-built alignment | #^f1, #^p1 (method) |
| Safety-first orchestration is feasible in current DTs | #^f3, #^sec-conclusion |
| Limitations of preprint evidence (controlled-setting only) | #^p2 (discussion) |

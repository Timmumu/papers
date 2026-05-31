---
ref: "[85]"
citekey: "Greif2020"
title: "Peeking into the void: Digital twins for construction site logistics,"
authors: "T. Greif, N. Stein, and C. M. Flath"
year: 2020
doi: "10.1016/j.compind.2020.103264"
zotero_key: "3MAJ4UNU"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
---

# Greif2020 — Digital Twins for Construction Site Logistics

| Field | Value |
|-------|-------|
| **Ref** | [85] |
| **Authors** | T. Greif, N. Stein, C. M. Flath |
| **Year / Venue** | 2020 / Computers in Industry 121:103264 |
| **DOI** | [10.1016/j.compind.2020.103264](https://doi.org/10.1016/j.compind.2020.103264) |
| **Zotero** | 3MAJ4UNU |

## Abstract ^sec-abstract

Construction is one of the least-digitized industries. To address rising costs, the authors conceptualise a *lightweight digital twin* for non-high-tech industries and demonstrate it on bulk-material silo logistics with an industrial partner. Fill-level monitoring delivers informational, automational, and transformational value, but exploiting it requires a decision-support system (DSS) for dispatch and replenishment because the new optionality drastically increases operational complexity. ^p1

## Introduction & Background ^sec-intro

ICT advances (cloud, IoT, AI) have disrupted many sectors, yet construction remains laggard — characterised by limited supply-chain visibility and inefficient logistics. The paper positions a "lightweight" DT as a pragmatic entry-point for low-tech industries, in contrast to the high-fidelity DTs typically discussed in aerospace/manufacturing. ^p1

The work is framed around a single case company (a leading building-materials supplier) whose bulk silos move repeatedly between plants and sites with no awareness of fill state. The opportunity is to give silos a digital representation of fill level and enable a *direct-repositioning* logistics regime instead of plant→site→plant round-trips. ^p2

## Method ^sec-method

The study follows a design-science approach. ^p1
1. **Problem description (§2):** Document standard silo supply and replenishment processes, identifying back-haul waste and stockout risk. ^p2
2. **Digital supply chain (§4):** Augment each silo with a fill-level sensor and connect it to a cloud platform, providing the missing observable for a silo digital twin. ^p3
3. **Process transformation (§5):** Re-design the logistics process to allow silo-to-silo direct repositioning, framed as a coupled Pickup-and-Delivery Problem (PDP) and Inventory Routing Problem (IRP). ^p4
4. **DSS design (§6):** Implement a prototype DSS that integrates the DT data feed with a dynamic optimisation engine and validate it via simulation across maintenance and replenishment scenarios. ^p5

## Key Findings ^sec-results

- A naive threshold-based replenishment policy on top of the new sensor data **does not** reduce cost — value only materialises when sensing is coupled with integrated PDP+IRP optimisation. ^f1
- Direct silo repositioning between sites reduces kilometers driven and therefore CO₂ emissions (per Léonardi & Baumgartner, 2004). ^f2
- The DSS-based dynamic policy unlocks transformational value (process redesign), not just informational/automational value. ^f3
- Success hinges on aligning future capital investment (infrastructure + operating assets) with the new operational practice; the gap between success and failure is narrow. ^f4

## Discussion & Implications ^sec-discussion

The authors argue that a *lightweight* DT is sufficient for industries where high-fidelity physics simulation is impractical, provided that the DT is paired with decision-support automation that handles the combinatorial explosion of the new options. ^p1

The case generalises beyond silos: any logistics asset whose location/state was previously opaque could be twinned with low-cost IoT and unlock similar value tiers, provided the organisation invests in the optimisation layer. ^p2

Limitation: findings rest on a single industrial collaborator; external validity to other contractors and materials remains open. ^p3

## Conclusion ^sec-conclusion

Transforming "dumb" silos into smart data-processing units enables a new direct-repositioning logistics system with both cost and emissions benefits, but only when fill-sensor data is fused with a DSS that solves the coupled PDP-IRP dynamically. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance

- **AECO lifecycle stage(s) addressed:** construction (logistics & supply-chain operations).
- **Cognitive capability:** perception (fill-level sensing) → reasoning (PDP/IRP optimisation) → decision support (human-in-the-loop dispatch).
- **Why cited in LR_cc.md:** Greif2020 is the canonical "lightweight DT + DSS" exemplar that grounds the SLR's argument that AECO DT value is unlocked not by twin fidelity alone but by coupling perception with decision-making automation. It exemplifies the *informational → automational → transformational* value progression invoked when classifying DT maturity in the AECO context.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| DT in construction logistics generates value through informational→automational→transformational tiers | #^sec-abstract, #^f3 |
| Sensor data alone insufficient; needs decision-support automation | #^f1, #^p1 (discussion) |
| Lightweight DT viable for low-tech AECO contexts | #^p1 (intro), #^p1 (discussion) |
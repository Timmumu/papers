---
ref: ""
citekey: "Junxiang-Zhu2025"
title: "Semantics-based connectivity graph for indoor pathfinding powered by IFC-Graph"
authors: "Junxiang Zhu; Mun On Wong; Nicholas Nisbet; Jinying Xu; Tom Kelly; Sisi Zlatanova; Ioannis Brilakis"
year: 2025
journal: "Automation in Construction"
doi: "10.1016/j.autcon.2025.106019"
zotero_key: "E9UPI6EW"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Building", "Digital-Twin", "Facility-Management", "Semantic", "Unsorted", "source: lens", "identification: databases"]
---
# Junxiang-Zhu2025 — Semantics-based connectivity graph for indoor pathfinding powered by IFC-Graph

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Junxiang Zhu; Mun On Wong; Nicholas Nisbet; Jinying Xu; Tom Kelly; Sisi Zlatanova; Ioannis Brilakis |
| **Year / Venue** | 2025 · *Automation in Construction* |
| **DOI** | [10.1016/j.autcon.2025.106019](https://doi.org/10.1016/j.autcon.2025.106019) |
| **Zotero** | `E9UPI6EW` |
| **Screening** | V1: digital twin \| V2: building|buildings|facility management|foundation \| V3: semantic |

## Abstract ^sec-abstract

Pathfinding is important for many indoor location-based applications such as facility management and indoor navigation. Conventional approaches for constructing indoor networks for pathfinding are mostly based on geometry processing, which can be computing-intensive and time-consuming, especially for buildings with complex irregular shapes. In addition, the generated geometric networks often lack semantics. This paper proposes a new semantics-based approach for constructing navigable indoor networks. This approach uses the rich semantic information from Industry Foundation Classes (IFC) in the form of IFC-Graph (i.e., a graph-based representation of building information developed in a prior study) so as to meet the needs of indoor pathfinding. Real-world building models are used to validate the proposed approach. The results show that 1) the semantics-based approach has advantages in object-to-object pathfinding such as space-to-space, space-to-exit, and space-to-facility, 2) the use of graph technology makes it flexible to add semantic information to the network to better support pathfinding applications. The semantics-based approach can fit into digital twin technology and integrate with augmented reality. • Devised a semantics-driven approach to construct indoor connectivity graph. • Developed a semantics-based connectivity graph to ensure object-to-object pathfinding. • Extended IFC with a custom entity IfcRelConnectsSpace to enable vertical connectivity. • Provided examples of pathfinding that better reflect perception of end-users. • Extended the concepts of semantic graphs for knowledge integration in indoor pathfinding.

## Introduction & Background ^sec-intro

Pathfinding is important for indoor location-based applications (FM, navigation). Conventional geometry-based indoor network construction is computing-intensive and lacks semantics. The paper proposes a **semantics-based approach for constructing navigable indoor networks** using IFC-Graph.

## Method ^sec-method

Uses rich semantic information from IFC in IFC-Graph form. A custom entity (IfcRelConnectsSpace) extends IFC for vertical connectivity. Semantics-based connectivity graph supports object-to-object pathfinding (space-to-space, space-to-exit, space-to-facility). Validated on real building models.

## Key Findings ^sec-results

The semantics-based approach shows advantages in object-to-object pathfinding. Graph technology makes it flexible to add semantic information. The approach can fit into **digital twin technology and integrate with augmented reality**.

## Discussion & Implications ^sec-discussion

**Highly relevant** — an IFC-Graph semantic indoor-pathfinding approach explicitly targeting DT integration. Directly informs the semantic-DT and indoor-navigation strands.

## Notes ^sec-notes

- **Screening:** Retained — IFC-Graph + semantics + indoor pathfinding + DT (strong fit).
- **Relevance:** High; cite for semantic graph pathfinding and DT-AR integration.
- **Source:** Hybrid OA; abstract-grounded, full text pending.

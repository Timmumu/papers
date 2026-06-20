---
ref: "[10]"
citekey: "Theiler2018"
title: "IFC Monitor - An IFC schema extension for modeling structural health monitoring systems"
authors: "M. Theiler, S. Smarsly, K. Dragos"
year: 2018
journal: "Advanced Engineering Informatics"
doi: "10.1016/j.aei.2018.04.011"
zotero_key: "H98THTQ4"
zotero_status: verified
last_verified: "2026-05-25"
tags: ["Semantic", "BIM-to-DT", "Verified", "source: scholar", "identification: other methods"]
---

# Theiler2018 — IFC Monitor: An IFC Schema Extension for SHM Systems

| Field | Value |
|-------|-------|
| **Ref** | [10] |
| **Authors** | M. Theiler, K. Smarsly (and K. Dragos in the LR_cc reference list) |
| **Year / Venue** | 2018 / Advanced Engineering Informatics, vol. 37, pp. 54–63 |
| **DOI** | [10.1016/j.aei.2018.04.011](https://doi.org/10.1016/j.aei.2018.04.011) |
| **Zotero** | H98THTQ4 |

## Abstract ^sec-abstract
The pervasive emergence of sensing technologies for structural health monitoring (SHM) and the digitalization ubiquitous in engineering ("Industry 4.0") increase the demand for richer civil-engineering information models. Conventional BIM captures geometry, material, and cost using current modeling standards, but "monitoring-related information" cannot yet be fully described on a well-defined, formal basis. The paper proposes a BIM-based approach that uses the open Industry Foundation Classes (IFC) schema as the formal foundation: it discusses possibilities and constraints of representing monitoring data within IFC, derives a technology-independent semantic metamodel for SHM systems, and then extends IFC into the "IFC Monitor" schema for native description of SHM systems consistent with IFC modeling capabilities. ^p1

## Introduction & Background ^sec-intro
The work is motivated by the convergence of two trends: dense, low-cost wireless sensing for SHM, and BIM as the dominant information backbone for civil assets. Although BIM standards excel at geometry, materials, classifications, and cost, they currently provide no first-class representation for the sensors, networks, channels, and measurement campaigns that drive SHM, forcing data to live in fragmented spreadsheets, vendor databases, or ad-hoc extensions. ^p1

This semantic gap blocks long-term interoperability of monitoring data across the asset lifecycle and across stakeholders (designers, operators, regulators). The authors therefore frame the problem as one of schema extension: the SHM domain should be expressible *inside* the open BIM standard, so that monitoring-related information is governed by the same versioning, exchange, and certification mechanisms as the rest of the model. ^p2

## Method ^sec-method
1. **Requirements analysis.** Enumerate the information needed to formally describe an SHM system (sensors, channels, sampling, processing chains, locations on host structures) and check what current IFC entities and property sets can or cannot express. ^p1
2. **Semantic metamodel.** Integrate the required information into a technology-independent semantic model that serves as the metamodel for any concrete schema mapping. ^p2
3. **IFC schema extension ("IFC Monitor").** Map the metamodel into IFC-compliant entities, relations, and property sets, respecting IFC modeling principles, so that SHM systems can be represented natively within IFC files. ^p3
4. **Verification & validation.** Verify the schema using the test software employed in the official IFC certification program, then validate by formally describing a prototype SHM system with IFC Monitor and checking that all monitoring-related information is precisely expressed. ^p4

## Key Findings ^sec-results
- A standards-compliant extension to IFC ("IFC Monitor") can natively represent SHM hardware, channels, and monitoring activities without breaking existing IFC tooling. ^f1
- A technology-independent SHM metamodel is a necessary intermediate artifact between domain requirements and a concrete schema, so the approach generalizes beyond a single vendor or sensor family. ^f2
- The extension passes the certified IFC test software, indicating syntactic compliance with the open BIM standard. ^f3
- Validation on a prototype SHM system demonstrates that IFC Monitor can describe a real monitoring deployment precisely, closing the BIM ↔ SHM semantic gap for the modeled sensor classes. ^f4

## Discussion & Implications ^sec-discussion
By extending IFC rather than introducing a parallel SHM database, the paper preserves a single source of truth across design, construction, and operation, which is a prerequisite for any lifecycle digital twin that wants to consume monitoring data without bespoke connectors. ^p1

The approach is, however, model-centric and schema-bound: new sensor classes or non-standard monitoring concepts require further IFC extensions, and the schema does not by itself address high-frequency data streaming, semantic reasoning, or feedback to the physical system. ^p2

## Conclusion ^sec-conclusion
IFC Monitor demonstrates that SHM systems can be embedded inside the open BIM standard with formal rigor, providing a foundation on which BIM-to-DT pipelines can build interoperable monitoring layers across the asset lifecycle. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** construction, operation
- **Cognitive capability:** perception (sensor integration), semantic interoperability
- **Why cited in LR_cc.md:** Theiler et al. is the canonical example of *model-centric* BIM-to-DT in the SLR: it shows that SHM networks can be embedded natively within standard BIM semantics, while also exemplifying the limitation that such extensions remain bound to predefined sensor types and lack closed-loop feedback.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| §3.1 / §6: "model-centric approaches treat BIM as the authoritative source and assimilate sensor data as attribute updates [1], [7], [10]" | #^sec-abstract, #^f1 |
| §3.2: "Semantic interoperability & ontologies — [10] Theiler2018" cluster entry | #^sec-intro, #^f2 |
| §3.2: "IFC Monitor extension … demonstrates how SHM networks can be embedded natively within standard BIM semantics, though limited to predefined sensor types" | #^f1, #^p2 |

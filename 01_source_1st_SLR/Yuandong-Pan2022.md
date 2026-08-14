---
ref: ""
citekey: "Yuandong-Pan2022"
title: "Enriching geometric digital twins of buildings with small objects by fusing laser scanning and AI-based image recognition"
authors: "Yuandong Pan; Alexander Braun; Ioannis Brilakis; André Borrmann"
year: 2022
journal: "Automation in Construction"
doi: "10.1016/j.autcon.2022.104375"
zotero_key: "P4H4EBXB"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Digital-Twin", "Monitoring", "Pipeline", "Point-Cloud", "Safety", "Semantic", "Structural", "Unsorted", "source: lens", "identification: databases"]
---
# Yuandong-Pan2022 — Enriching geometric digital twins of buildings with small objects by fusing laser scanning and AI-based image recognition

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Yuandong Pan; Alexander Braun; Ioannis Brilakis; André Borrmann |
| **Year / Venue** | 2022 · *Automation in Construction* |
| **DOI** | [10.1016/j.autcon.2022.104375](https://doi.org/10.1016/j.autcon.2022.104375) |
| **Zotero** | `P4H4EBXB` |
| **Screening** | V1: digital twin|digital twins \| V2: buildings|structural|pipeline \| V3: safety|semantic|monitoring|point cloud |

## Abstract ^sec-abstract

This paper addresses the challenge of enriching geometric digital twins of buildings, with a particular emphasis on capturing small but important entities from the electrical and the fire-safety domain, such as signs, sockets, switches, smoke alarms, etc. Unlike most previous research that focussed on structural elements and processed laser point clouds and images separately, we propose a novel method that fuses laser scanning and photogrammetry methods to capture the relevant objects, recognise them in 2D images and then map these to a 3D space. The considered object classes include electrical elements (light switch, light, speaker, socket, elevator button), safety elements (emergency switch, smoke alarm, fire extinguisher, escape sign), plumbing system elements (pipes), and other objects with useful information (door sign, board). Semantic information like class labels is extracted by applying AI-based image segmentation and then mapped to the 3D point cloud, segmenting the point cloud into point clusters. We subsequently fit geometric primitives to the point clusters and extract text information by AI-based text detection and recognition. The final output of our proposed method is an information-rich digital twin of buildings that contains geometric information, semantic information such as object categories and useful text information which is valuable in many aspects, like condition monitoring, facility maintenance and management. In summary, the paper presents a nearly fully-automated pipeline to enrich a geometric digital twin of buildings with details and provides a comprehensive case study.

## Introduction & Background

The paper addresses enriching **geometric digital twins** of buildings with small entities (signs, sockets, switches, smoke alarms). Proposes fusing laser scanning and photogrammetry with AI-based image segmentation mapped to 3D.

## Method

AI segmentation extracts semantic labels from 2D images → mapped to 3D point cloud → geometric primitives fitted. AI text detection extracts text info. Output: information-rich DT with geometric, semantic, and text data.

## Key Findings

A nearly fully-automated pipeline enriches geometric building DT with details valuable for condition monitoring, FM, and maintenance.

## Discussion

**Highly relevant** — an automated geometric-DT enrichment pipeline. Directly informs the scan-to-DT strand.

## Notes

- **Screening:** Retained — geometric DT + enrichment + AI segmentation (strong fit).
- **Relevance:** High; cite for automated DT enrichment pipeline.
- **Source:** Hybrid OA; abstract-grounded, full text pending (PDF in library).

---
ref: "[66]"
citekey: "Tixier2016"
title: "Automated content analysis for construction safety: A natural language processing system to extract precursors and outcomes from injury reports,"
authors: "J. P. Tixier, G. Hallowell, B. Rajagopalan, and D. Bowman"
year: 2016
doi: "10.1016/j.autcon.2015.11.001"
zotero_key: "X5U62SNQ"
zotero_status: verified
created: "2026-05-25"
tags:
  - Verified
  - source: scholar
  - identification: other methods
---

# Tixier2016 —Automated Content Analysis for Construction Safety (NLP on Injury Reports)

| Field | Value |
|-------|-------|
| **Ref** | —|
| **Authors** | Tixier, A.J.-P.; Hallowell, M.R.; Rajagopalan, B.; Bowman, D. |
| **Year / Venue** | 2016 / Automation in Construction 62, 45—6 |
| **DOI** | 10.1016/j.autcon.2015.11.001 |
| **Zotero** | X5U62SNQ |

## Abstract ^sec-abstract
In the US and globally, construction workers face higher injury rates than any other industry, motivating extensive research; yet safety improvement has decelerated and traditional programmes are saturated. Major contractors and federal agencies hold large databases of unstructured digital injury reports that could be exploited to understand, predict and prevent accidents. This paper presents a Natural Language Processing (NLP) system that automatically extracts precursors and outcomes from such unstructured reports, converting free-text narratives into structured safety attributes ready for analytics. ^p1

## Introduction & Background ^sec-intro
Manual coding of injury reports is slow, expensive and inconsistent, leaving most empirical safety knowledge locked in text. Earlier rule-based extractors handled narrow vocabularies; modern NLP can extract richer attributes at scale. ^p1

## Method ^sec-method
The pipeline uses keyword libraries, regular expressions and disambiguation rules grounded in a construction-safety attribute taxonomy (energy sources, environmental conditions, behavioural precursors, injury outcomes). Implemented in R, the system processes thousands of reports, with validation against human-coded gold standards using precision, recall and F1. ^p1

## Key Findings ^sec-results
- The NLP system extracts safety precursors and outcomes from unstructured reports with high agreement with human coders. ^f1
- Automated coding scales to entire corporate corpora that were previously unanalysable. ^f2
- Structured outputs feed downstream risk-prediction and prevention analytics. ^f3

## Discussion & Implications ^sec-discussion
The work is a foundational demonstration that NLP can transform construction safety from anecdote-driven to data-driven, enabling the "language" tier of a cognitive DT —turning narrative incident records into machine-readable evidence. ^p1

## Conclusion ^sec-conclusion
NLP-based content analysis unlocks large injury-report archives as a quantitative resource for safety research and practice. ^p1

## Relevance to Cognitive Full-Lifecycle DT SLR ^sec-relevance
- **Lifecycle stage(s):** Construction (safety analytics).
- **Cognitive capability:** Natural language understanding 鈫?structured knowledge extraction (a core cognitive function).
- **Why cited in LR_cc.md:** Canonical example of NLP enabling cognitive processing of textual site data, complementing sensor-based DT layers.

## Traceability

| Claim in LR_cc.md | Evidence anchor |
|---|---|
| NLP turns unstructured injury reports into DT-ready evidence | #^f1 |
| Cognitive DTs need a language/NLP layer for textual inputs | #^sec-discussion |

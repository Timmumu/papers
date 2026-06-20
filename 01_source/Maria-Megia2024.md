---
ref: ""
citekey: "Maria-Megia2024"
title: "Generative Adversarial Networks for Improved Model Training in the Context of the Digital Twin"
authors: "María Megía; Francisco Javier Melero; Manuel Chiachío; Juan Chiachío"
year: 2024
journal: "Structural Control and Health Monitoring"
doi: "10.1155/stc/9997872"
zotero_key: "BXDDTD8J"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Architecture", "Construction", "Digital-Twin", "Monitoring", "Quality", "Unsorted", "source: lens"]
---
# Maria-Megia2024 — Generative Adversarial Networks for Improved Model Training in the Context of the Digital Twin

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | María Megía; Francisco Javier Melero; Manuel Chiachío; Juan Chiachío |
| **Year / Venue** | 2024 · *Structural Control and Health Monitoring* |
| **DOI** | [10.1155/stc/9997872](https://doi.org/10.1155/stc/9997872) |
| **Zotero** | `BXDDTD8J` |
| **Screening** | V1: digital twin|digital twins \| V2: aeco|construction|architecture \| V3: quality|monitoring |

## Abstract ^sec-abstract

Digital twins (DTs) have revolutionised digitalisation practices across various domains, including the Architecture, Engineering, Construction and Operations (AECO) sector. However, DTs often face challenges related to data scarcity, especially in AECO, where tests are costly and difficult to scale. Historical data in this domain are often limited, unstructured and lack interoperability standards. Data scarcity directly affects the accuracy and reliability of the DT models and their decision‐making capabilities. To address these challenges, classical methods are used to produce synthetic data based on predefined statistical distributions, which are barely scalable to unpredictable scenarios and prone to overfitting. Alternately, this work presents a novel comprehensive approach that covers every aspect from synthetic data generation to training and testing of these data on the system’s models. This strategy not only delivers high‐quality data that meets the model’s requirements in terms of diversity, complexity and class balance, but also provides the diagnostic and prognostic capabilities of the DT of the system through its trained models. State‐of‐the‐art techniques including generative adversarial networks (GANs), specifically Wasserstein generative adversarial networks with gradient penalty (WGAN‐GP), and convolutional neural networks (CNNs) are employed in this novel pervasive approach, participating in the same architecture for generative, diagnostic and prognostic purposes. GANs enable data augmentation and reconstruction, while CNNs excel in spatial pattern recognition tasks. The proposed framework is demonstrated through an experimental case study on damage diagnostics and prognostics of a laboratory‐scale metallic tower, where synthetic datasets are generated to supplement limited health monitoring data. The results showcase the effectiveness of the generated data for damage detection, prognostics and operational decision‐making within the DT context. The presented method contributes to overcoming data scarcity challenges and improving the accuracy of DT models in the AECO sector. The article concludes with discussions on the application of the results and their implications for decision‐making within the DT framework.

## Introduction & Background ^sec-intro

DTs face challenges related to data scarcity in AECO where tests are costly and difficult to scale. Historical data are often limited, unstructured, and lack interoperability standards, directly affecting DT model accuracy and reliability.

## Method ^sec-method

A novel comprehensive approach from **synthetic data generation via WGAN-GP** to training and testing on system models. CNNs handle spatial pattern recognition for diagnostic and prognostic purposes. Demonstrated on a laboratory-scale metallic tower for damage diagnostics and prognostics.

## Key Findings ^sec-results

The framework delivers high-quality synthetic data meeting diversity, complexity, and class-balance requirements. Generated data proved effective for damage detection, prognostics, and operational decision-making within the DT context.

## Discussion & Implications ^sec-discussion

**Highly relevant** — a GAN-based synthetic-data framework for DT diagnostics/prognostics. Complements #208 (TTS-WGAN-GP for bridge data augmentation).

## Notes ^sec-notes

- **Screening:** Retained — GAN + synthetic data + DT + diagnostics + prognostics (strong fit).
- **Relevance:** High; cite for WGAN-GP synthetic data for DT diagnostics.
- **Source:** Gold OA; abstract-grounded, full text pending (PDF in library).

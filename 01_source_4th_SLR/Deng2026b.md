# Deng, R et al. (2026) — Vision-driven dynamic tunnel digital twin for real-time situation and emergency awareness

- **ID:** R373 | **Source:** Scopus | **DOI:** 10.1016/j.undsp.2026.05.004
- **Journal:** Underground Space (new)
- **Authors:** Deng R.; Zhu S.; Lu T.; Wang W.; Gong S.; Zhang Y.; Huang X.; Usmani A.

## Abstract summary
Effective management and safe operation of tunnel infrastructure are critically challenged by the persistent vehicle tracking across non-overlapping camera domains and the lack of real-time situational awareness for emergency incidents. This work proposes a dynamic digital twin framework to create a high-fidelity virtual representation that synchronously updates with physical tunnel environments by leveraging existing Closed-Circuit Television (CCTV) networks. The core is a novel Tunnel Re-identification Model (TRIM) that can create discriminative feature embeddings for seamless vehicle tracking and re-identification across multi-camera domains. Comparative validations unequivocally demonstrate that the TRIM significantly outperforms Convolutional Neural Networks (CNNs) and standard Vision Transformer backbones, achieving a state-of-the-art mAP@10 of 0.684. Analysis of attention heatmaps…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Vision-driven tunnel DT for situation/emergency awareness

## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Transformer / Large Language Model (LLM) | Single (one data type) | Single case study | 4 | Perception / Computer Vision |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | CCTV vision feeds both the TRIM tracking and the fire-detection module in one platform (single modality, multi-task). | High |

**Key evidence (AG):** Vision-driven dynamic tunnel digital twin (PolyU, Underground Space 2026): leverages existing CCTV networks to synchronously update a high-fidelity virtual tunnel; Tunnel Re-identification Model (TRIM, transformer-based) achieves state-of-the-art mAP@10 0.684 for cross-camera vehicle tracking, outperforming CNNs and standard ViT backbones; coupled vision fire-detection module localises and visualises emergent tunnel fires in the twin. Explicitly a data-fusion/perception layer rather than a fully automated closed-loop twin; one-way vision->situational awareness for operators; no actuation, no learning loop.

*Full-text source: browser-oa*

**AH — strength & gap filled:** Reuses existing CCTV with a transformer Re-ID (mAP@10 0.684) and vision fire detection to keep the tunnel twin synchronised, avoiding hardware redevelopment and improving operator situational judgment.

**AI — deficiencies & future work:** Perception layer only - no automated control; Re-ID validated on datasets with deployment described rather than benchmarked; fire module performance metrics partial.

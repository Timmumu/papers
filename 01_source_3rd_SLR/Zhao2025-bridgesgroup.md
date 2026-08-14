# Zhao et al. (2025) — Automatic response prediction in a digital twin framework for regional bridges group

- **ID:** 3863 | **Source:** Scopus | **DOI:** 10.1016/j.istruc.2025.109052
- **Journal:** Structures
- **Authors:** Zhao, W.; Wan, C.; Zhang, X.; Zhang, G.; Ding, Y.; Xie, L.; Peng, H.; Xue, S.

## Abstract summary
Bridges are essential components of transportation infrastructure, real-time monitoring of their structural conditions can provide valuable information for maintenance strategies. By with advanced structural health monitoring systems, stakeholders can gain critical insights into the condition and safety of bridges, thereby optimizing maintenance efforts. However, it is unrealistic to expect that every bridge within a regional network will be equipped with extensive structural health monitoring and weigh-in-motion systems. This paper therefore presents a digital twin system for bridges group aimed at achieving the working condition perception for all bridges within the regional transportation network. In physical space, collecting vehicle information and structural response data from bridges. In the corresponding digital space, numerical models are established for each bridge of a regiona…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT for regional bridges group response prediction; Transformer safety warning

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI/title match, coverage re-scan 2026-08-12)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 0 | 1 | Design for Safety (DfS) | None | Transformer / Large Language Model (LLM) | Multi (two or more data types) | Cross-project (multiple real projects) | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Digital twin system for a regional bridges group (Southeast U / Tongji): physical space collects vehicle info + structural response from bridges; digital space builds numerical models per bridge with traffic load as the linking variable; Transformer neural network predicts bridge responses (vehicle-load-based, within/cross-bridge, measured-data fusion) to enable safety warning across the regional network; validated on three concrete bridges in Jiangsu (vehicle driven over bridges; compared vs LSTM/BiLSTM/BiGRU; metrics Ta/RMAE/R²). One-way monitoring/prediction→safety warning & O&M decisions; no actuation and no self-improvement loop (offline-trained Transformer).

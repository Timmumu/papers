# Zhao et al. (2025) — Digital twin-enabled anti-collision system for smart construction sites

- **ID:** 3515 | **Source:** Scopus | **DOI:** 10.55092/sc20250022
- **Journal:** Smart Construction
- **Authors:** Zhao, S.; Yu, C.; Zhong, R. Y.

## Abstract summary
The construction industry is one of the most perilous sectors globally, with significantly higher fatality rates compared to other industries. Collision with heavy construction machines is a major cause of worker injuries and fatalities. This research proposes a digital twin-enabled anti-collision system to provide collision warnings and improve construction safety. A five-dimensional digital twin model encompassing the physical layer, digital data layer, virtual entity layer, service layer, and connection layer is established. The physical layer designs multi-sensor fusion approach to respectively collect image data, depth data, and motion data, achieving comprehensive perception of construction sites. The digital data layer designs multi-modal analysis methods to obtain on-site information such as category, position and motion status. The virtual entity layer integrates geometry model,…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT anti-collision system for smart construction sites; 96% zone prediction

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow | 0 | 1 | 0 | Design for Safety (DfS) | None | Computer Vision / CNN / object-detection | Multi (two or more data types) | Simulation | 4 | Perception / Computer Vision |

**Key evidence (AG):** Digital-twin-enabled anti-collision system for HRI safety on construction sites (5D DT: PE/DD/VE/SS/CN): multi-sensor fusion (RGB-D image+depth, IMU motion) + multi-modal analysis (YOLOv5/Faster-RCNN detection, HRNet excavator key-points) drive a Unity 3D virtual entity; rule model divides 3D site into dangerous/warning/safe zones (TTC+SO, d_danger=600 mm, d_warn=1200 mm) triggering collision warnings to smart helmets/tri-colour lights in a perception-analysis-decision-execution closed loop. Lab case study with 1:24 scaled excavator: zone warning precision 96.4%/95.3%, recall 98.8%/97.4%, delay 0.13 s. Warnings executed to humans/devices but no automated machine control; no self-improvement (manual retraining via data management).

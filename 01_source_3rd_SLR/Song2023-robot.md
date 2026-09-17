# Song et al. (2023) — Digital twin-assisted fault diagnosis system for robot joints with insufficient data

- **ID:** 3833 | **Source:** Scopus | **DOI:** 10.1002/rob.22127
- **Journal:** Journal of Field Robotics
- **Authors:** Song, Z.; Shi, H.; Bai, X.; Li, G.

## Abstract summary
The robot joint is an important component of the construction robot, and its fault diagnosis can ensure the exact execution of building jobs, stable operation, and timely prevention of probable safety mishaps. However, deep learning-based fault diagnosis needs a multitude of measured fault data, which is difficult to obtain for various reasons. To solve the problem of insufficient data, a digital twin-assisted fault diagnosis system for robot joints is proposed. First, a simplified dynamics model of the robot joint is developed to generate the virtual entity data which can be used as the X-domain data for the digital twin model. Second, a CycleGAN-based digital twin model is proposed to map the virtual entity (X-domain) data to the physical entity (Y-domain) utilizing only a small amount of measured data. In the end, a test-rig for the robot joint is built to simulate the robot's working…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT-assisted fault diagnosis of construction robot joints; safety mishaps

## Step-3 Deep-Read Coding (Prompt B) — full text verified via Endnote library (front-matter DOI match)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Single (one data type) | Simulation | 4 | Predictive analytics / decision support |

**Key evidence (AG):** Digital-twin-assisted fault diagnosis for construction-robot joints (RV reducer): gear-dynamics virtual-entity model generates faultless vibration (X-domain), CycleGAN maps virtual→physical domain using only ~400 measured samples (Y-domain), and CNN-ResNet classifies wear/crack/pitting/normal faults — accuracy raised from 32.5% (measured only) to 98.86% with 1200 simulated samples (best of GAN/transfer baselines). Validated on a lab RV-reducer test rig with acceleration/temperature sensors; DT is an offline data-augmentation/generative model for training, no live twin loop, no learning.

**Strength & gap filled (AH):** Fills the insufficient-data gap in deep-learning fault diagnosis of construction-robot joints: a gear-dynamics virtual entity generates faultless vibration data as the X-domain and a CycleGAN-based digital twin maps it to the physical Y-domain, so that with only 400 measured samples a CNN-ResNet classifier reaches 98.86 percent accuracy versus 32.5 percent without augmentation, outperforming GAN baselines on an RV reducer test rig.

**Deficiencies & future work (AI):** The digital twin is an offline simulation-to-reality data generator rather than a live synchronized model; only planetary-wheel faults of the RV reducer are considered on a laboratory test rig, and online diagnosis, model updating, or integration with an operating construction robot is not demonstrated or stated as future work.

**Fusion depth (AC1):** SINGLE

**Fusion evidence (AC2):**
- **Data streams:** about 400 measured vibration samples (X/Y domain) from an RV-reducer test rig; CycleGAN-generated data are model outputs.
- **Integration mechanism:** none - the CycleGAN maps simulated faultless vibration to the physical domain for augmentation, and CNN-ResNet classifies wear/crack/pitting/normal (98.86% with augmentation versus 32.5%).
- **Why this code:** one measured data type, so SINGLE (AC=Single).

**Confidence (AC3):** High.
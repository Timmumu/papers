# Wang, M et al. (2026) — A Partially Validated Probabilistic Framework for Urban Seismic Damage Prediction With Scenario Ensembles and Digital Twins

- **ID:** R172 | **Source:** Scopus | **DOI:** 10.1109/ACCESS.2026.3721347
- **Journal:** IEEE Access
- **Authors:** Wang M.; Sun Y.; Li H.; Mao N.

## Abstract summary
Earthquakes pose severe threats to urban safety. Traditional prediction methods fail to fully quantify seismic uncertainties and address low-probability, high-impact 'long-tail risks'. This paper proposes a partially validated probabilistic urban seismic damage prediction framework integrating large-scale scenario ensembles and digital twins. The framework is conceptually designed with four layers: data fusion, digital twin modeling, scenario ensemble simulation, and probabilistic assessment. Due to current data and computational constraints, empirical validation is limited to two core modules - the PI-GAN ground motion generation module and the probabilistic damage cloud module - using the 2021 Yangbi Ms6.4 earthquake (single event, single region). The remaining two modules (infrastructure cascading failure and social behavior modeling) are presented as conceptual designs requiring futu…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** Urban seismic damage DT framework; urban safety


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Bayesian / probabilistic | Multi (two or more data types) | Single case study | 3 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Aligned | PI-GAN ground-motion generation and the probabilistic damage-cloud module are validated separately (single event); cascading-failure and social-behaviour modules are only aligned by design, not fused or validated. | Low |

**Key evidence (AG):** Partially validated probabilistic framework for urban seismic damage prediction with scenario ensembles and DTs (IEEE Access 2026): four layers - data fusion, digital twin modelling, scenario ensemble simulation, probabilistic assessment; PI-GAN generates ground motions (<=5% PGA error, <=10% response-spectrum error); probabilistic damage-cloud module reaches 77.7% classification accuracy (79.5% recall, 87.3% precision, 83.2% F1) and 89.3% structure-damage matching, validated on the 2021 Yangbi Ms6.4 earthquake (single event, single region); cascading-failure and social-behaviour modules are conceptual only; M>=7.0 extreme scenarios and full-chain validation explicitly future work. Scenario/simulation DT - no live data loop, no actuation, no learning loop.

*Full-text source: Endnote*

**AH — strength & gap filled:** Fills the long-tail-risk gap in urban seismic damage prediction: a four-layer probabilistic framework with PI-GAN ground motions (<=5% PGA error) and a probabilistic damage-cloud module (77.7% accuracy, 89.3% matching) validated on the 2021 Yangbi Ms6.4 earthquake, while explicitly declaring which modules remain conceptual.

**AI — deficiencies & future work:** Only two of four modules validated, on a single event and region (2021 Yangbi Ms6.4); M>=7.0 extreme scenarios, cascading-failure and social-behaviour modules are conceptual; full-chain validation explicitly future work.

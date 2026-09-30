# Zhang, K.-W et al. (2026) — Digital twin-driven multi-metrics condition assessment of eccentrically loaded reinforced concrete columns

- **ID:** R330 | **Source:** Scopus | **DOI:** 10.1080/15732479.2026.2656943
- **Journal:** Structure and Infrastructure Engineering
- **Authors:** Zhang K.-W.; Xu Y.-L.; Dong Y.; Zeng Z.-C.; Cai L.-H.; Ding Y.-H.; Tian Y.-D.

## Abstract summary
It is crucial to assess the structural condition of reinforced concrete (RC) structures to ensure their functionality and safety; however, accurate condition assessment remains challenging owing to uncertainties in geometric modelling, finite element analysis and assessment criteria. This study proposes a digital twin-driven multi-metrics method for condition assessment of eccentrically loaded RC columns with cracks. Three RC columns were tested, with one column used for development and two for validation specimens. The geometric digital twin (gDT) of the RC column was constructed using point cloud data for geometry and rebar scanning for reinforcement layout, thereby reducing geometric uncertainties caused by manufacturers. Building on the gDT, a nonlinear finite element model was constructed as the virtual entity and calibrated to experimental data using an optimisation algorithm, ther…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT condition assessment of RC columns; safety


## Step-3 Deep-Read Coding (Prompt B)
| P DT-subject | Q DfS/DfQ | R codable | U Tier | V Design | W Constr | X Oper | Z DfX | AA Self-improve | AB Methodology | AC Modality | AD Validation | AE QA(0-5) | AF Cluster |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

| AC1 fusion depth | AC2 fusion evidence | AC3 confidence |
|---|---|---|
| Fused | Point-cloud geometry, rebar-scanner reinforcement layout, deflection/strain/crack-width test data and load-bearing metrics are fused through PSO-updated FE modelling and DS evidence theory into one condition level. | High |

**Key evidence (AG):** Digital twin-driven multi-metrics condition assessment of eccentrically loaded RC columns (SWJTU/PolyU, Structure and Infrastructure Engineering 2026): laser-scanned point clouds and rebar scanning build a geometric DT; ABAQUS nonlinear FE with CDP and bond-slip becomes a mechanical DT through two-stage PSO updating against deflection, concrete strain and crack-width tests; updated parameters predict two validation columns with ultimate-load errors within 5%; fuzzy DS evidence theory fuses crack, deflection and load metrics into SLS/ULS condition levels, resolving threshold conflicts for serviceability and safety. One-way inspection/test data->updated twin->condition assessment; no physical actuation.

*Full-text source: Endnote*

**AH — strength & gap filled:** Integrates as-built geometry, reinforcement layout, loading-test responses and code-level assessment metrics into a single RC-column mechanical DT: PSO-updated ABAQUS/CDP models match Column C1 ultimate load almost exactly (620.4 vs 620.3 kN) and transfer to C2/C3 with ultimate-load errors within 5%, while DS evidence fusion resolves crack/deflection/load threshold conflicts for more sensitive SLS/ULS assessment.

**AI — deficiencies & future work:** Laboratory RC-column programme only; geometry/rebar scanning may fail under occlusion or inaccessible areas; environmental degradation, wider loading conditions, additional cross-sections and in-service RC members with initial defects are left for future validation.

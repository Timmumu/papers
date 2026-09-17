# Yang et al. (2026) — Digital twin-based framework for multi-objective optimization of shield tunneling parameters

- **ID:** 3721 | **Source:** Scopus | **DOI:** 10.1016/j.tust.2026.107457
- **Journal:** Tunnelling and Underground Space Technology
- **Authors:** Yang, C.; Ding, Z.; Liu, T.; Wu, Z.; Chen, K.

## Abstract summary
Optimizing shield tunneling parameters is critical for ensuring both safety and efficiency in tunnel construction. However, existing optimization approaches often underutilize operational data and are prone to entrapment in local optima. This study proposes a digital twin (DT) -based framework for multi-objective optimization (MOO) of shield tunneling parameters. The framework integrates data acquisition, preprocessing, modeling, and optimization within a layered architecture. Key parameters are identified using the shapley additive explanations (SHAP) method, while a hybrid optimization algorithm—artificial bee colony (ABC)–non-dominated sorting genetic algorithm III (NSGA-III)—combines the strengths of both algorithms and is applied across three operational scenarios. Optimized parameters are iteratively fed back into the DT to guide parameter adjustment. The framework is validated usi…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| Yes | Yes | Yes | Yes | Yes | **Include** |

**Note:** DT multi-objective optimization of shield tunneling parameters; safety

## Step-3 Deep-Read Coding (Prompt B)

| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support |

**Key evidence (AG):** DT-based framework for multi-objective optimization of shield tunneling parameters (Shenzhen U/HUST): layered architecture (data acquisition, preprocessing, modeling, optimization); SHAP identifies key parameters; ABC-NSGA-III hybrid optimization algorithm; optimized parameters iteratively fed back into DT to guide parameter adjustment; validated on Shanghai Airport Link Line project; 32.02% overall optimization rate, shield attitude deviation reduced 2.21-17.13%. Bidirectional — optimization→feedback→guidance → Tier 3; no learning loop (optimization is algorithmic, not learning).


**Strength & gap filled (AH):** Moves shield tunneling digital twins from monitoring toward closed-loop decision support: a four-layer DT framework where SHAP identifies 16 key tunneling parameters and an ABC-NSGA-III hybrid optimizer solves six attitude objectives, achieving a 32.02% overall optimization rate and 2.21 to 17.13% attitude-deviation reduction on 100 rings of the Shanghai Airport Link Line, with optimized parameters fed back to guide operations.

**Deficiencies & future work (AI):** The closed loop is human-machine collaborative, with operators filtering algorithm outputs rather than autonomous actuation, optimization takes about 900 seconds per ring, and validation is limited to one 100-ring subsection of a single project; future work includes transfer learning across geological conditions, improved sensing, and operator training programs.
**Fusion depth (AC1):** Fused

**Fusion evidence (AC2):**
- **Data streams:** multi-parameter shield-tunnelling monitoring (100 rings, Shanghai Airport Link Line).
- **Integration mechanism:** SHAP identifies 16 key parameters, ABC-NSGA-III jointly optimises six attitude objectives (32.02% overall optimisation, 2.21-17.13% deviation reduction), and results feed back to guide operations.
- **Why this code:** the optimisation output depends on multiple monitoring channels simultaneously, so Fused; operators still filter the recommendations (Medium).

**Confidence (AC3):** Medium - the multi-objective optimisation is explicit; the loop is human-machine collaborative.
(full-text source: Endnote)

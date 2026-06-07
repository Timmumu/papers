# Research Proposal
A Self-Improving Cognitive Digital Twin for Design-for-X Forecasting

Candidate	Tim, Hu TianYu

Programme	PhD, ACE, City University of Hong Kong

Supervisor	Prof. Thomas Ng

Field	AECO — Architecture, Engineering, Construction, Operations

# 1.Background 
The Architecture, Engineering, Construction, and Operations (AECO) industry get used to the current scattered and piecemeal delivery mode by phases. The flaws are twofold. First, analysis of quality and safety are not integrated across the planning, conceptual design, and development phases. Second, valuable information is lost massively at every node crossing phases. As result, project value is reduced in the form of more defects, safety incidents and even catastrophic rework. 
Digital twin (DT) has emerged as a promising paradigm for managing built assets across their lifecycle. However, the current development of DT remains largely limited to state synchronisation by mirroring physical assets digitally and visualizing sensor streams and focusing on operation stage of built asset. None of these systems realized real DT which must be real-time, of autonomy and bi-directional communication between virtual and physical world. Due to these limitations, none has enabled the DT to iterate, reflect on past decisions to predict forward, or claim convergence properties across design, construction, and operational phases.

## 1.1 Research gap
a. This research addresses a gap that is simultaneously theoretical and practical: 
The absence of a self-improving AECO digital twin that can formally co-evolve a forward predictor for design for safety and design for quality (DfX) with an iterative cross-phase convergence loop, such that improvements in prediction tighten convergence, and convergence iterations generate new training signal that improves prediction. The closest analogues in adjacent fields — expert iteration and self-play in reinforcement learning [2], cognitive digital twin frameworks in manufacturing [3], and closed-loop BIM research [1] — either lack cross-phase scope, formal convergence characterisation, or embedded forward prediction. Their existence confirms the intellectual lineage of this work; their limitations define its contribution.

b. This research brings a rare combination of assets to this problem: active full-time employment in the AECO industry providing direct access to real cross-project data (BIM models, incident records, quality defect logs, correspondence, and site photography).

c. Traditional machine learning with feature engineering algorithms (XGBoost, CNN) fail because empirical accident reports are highly unstructured, human biased and suffer from data incompleteness. However, this Cognitive Digital Twin is proposed to bypass this limitation by leveraging LLM semantic reasoning to extract root-cause logic such as institutional inspection failures and design-construction decoupling/discontinuity, which effectively turns incomplete reports into high-value DfS design constraints.

d. To mitigate the risk that single-project safety-data scarcity stalls the convergence loop in late stage, DfX is widened beyond DfS/DfQ to include **Design-for-Sustainability** (embodied carbon, ESG governance), which is supervised by densely-labelled sources (EPDs, ICE/EC3 datasets, contractor ESG narratives) and provides a redundant, parallel training signal for objective 1 across better-instrumented targets.

# 2.Research Aims and Objectives
This research aims to build a self-improving AECO digital twin prototype comprising two tightly coupled intellectual contributions, which will be a novel decision-making paradigm.

## 2.1 Core Module 1-Forward predictor for DfX
A multi-modal, element-level DfX predictor trained on real cross-project AECO data, comprising three discipline-specific sub-models (structural, envelope, MEP) consuming IFC graph topology, text extracts from specifications and correspondence, and site photography. Each sub-model exposes **three prediction heads — defect, safety, and sustainability** — sharing the same backbone but supervised by distinct label streams (NCR registers; incident reports; element-linked embodied-carbon labels from EPD/ICE plus contractor ESG narratives). A project-phase-level safety incident risk classifier consuming Core Module 1 outputs as features constitutes a secondary target, demonstrating the framework's extensibility.

## 2.2 Core Module 2 -Self-improving convergence loop
By securing the Core Module 1 first, the research proceeds towards an iterative loop spanning design, construction, and operation phases in which Core Module 1 serves as the forward operator. The loop stores iteration history, updates design proposals using Core Module 1 predictions, and terminates under formally stated convergence conditions. 
The convergence conditions tentatively target for lowering the safety incident man-hour rate down to the regulation baseline while the performance (cost & time) throughout life cycle is optimal. Defining the convergence conditions are also the expected outcome of this research.

## 2.3 Core Module 3 - Merge the forward predictor into convergence loop
The self-improving convergence iterations loop of Core Module 2 generate new training signal that further improves the forward predictor of Core Module 1. Improved Core Module 1 subsequently accelerates the convergence. This is the central theoretical claim of the thesis.

In summary, the specific research objectives are stated in the action–artefact–method form so that each objective is independently researchable and evaluable:

**Objective O1.** To develop a **multimodal extraction model based on NLP** (LLM with structured-output prompting and source-span citation, GraphRAG over Neo4j, and CLIP photo–text alignment) that converts unstructured AECO project records (emails, letters, RFIs, specifications, inspection notes, incident reports, and site photographs) into structured, IFC-element-linked DfX risk attributes covering safety, quality and sustainability, extending the attribute-based DfS paradigm of Esmaeili & Hallowell and Tixier et al. by replacing manual attribute coding with LLM-based extraction.

**Objective O2.** To develop a **calibrated element-level DfX risk-prediction model based on graph neural networks with cross-modal attention and conformal prediction** that fuses the O1-extracted attributes with IFC geometric and topological features and outputs three coverage-guaranteed prediction heads (defect / safety / sustainability) usable as a forward operator by O3.

**Objective O3.** To develop a **cross-phase convergence algorithm based on a Lyapunov-style update rule with Chebyshev-distance termination** that consumes O2 outputs to iteratively update parametric design variants, with a formally stated monotone-decrease argument under bounded forward-operator error.

**Objective O4.** To develop a **coupled self-improving digital-twin prototype based on closed-loop re-training of O1/O2 on O3 iteration logs**, in which the improved forward operator demonstrably accelerates O3 convergence — validated on two real construction case studies plus their parametric variants, and on a cross-jurisdiction public incident corpus.

Each objective's data subset, method stack, implementation target, evaluation protocol, and falsifiability statement are detailed in §3.2 Table 2 and §3.4.

Falsifiability statements (panel-defence anchors):
- **O1** is falsified if expert-annotated extraction precision/recall on held-out documents drops below 0.70 with Cohen's κ < 0.6.
- **O2** is falsified if calibrated coverage deviates from the nominal level by > 10 percentage points, or if O1-augmented features fail to outperform a geometry-only ablation.
- **O3** is falsified if no monotone decrease of L(state) is observed across the case studies under bounded O2 error.
- **O4** is falsified if no positive correlation between checkpoint index and reduction in iterations-to-convergence is detected.

# 3. Methodology
## 3.1 Data strategy
Available data is rarely uniform. It resides in diverse formats across multiple platforms and creates silos that hinder effective analysis and prediction. Data collection, classification and pre-processing will be completed at the beginning to fine-tune the technical architecture.

Table 1 - Data Availability

| Data Modality        | Typical Sources                                                 | Processing Technology                           | Forecasting Role (Whether / When / How)                                                                                                                                |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Geometric            | BIM, CAD Drawings                                               | GNN, Model Derivative API                       | **How**: Identifies design flaws and spatial clashes.                                                                                                                  |
| Semantic             | Regulations, Specifications, Bills of Quantities                | NLP (BERT/GPT), RAG, CLIP                       | **Whether**: Contextualises the probability of risk based on materials (gas, asbestos, etc.) and methods (demolition, lifting, etc.).                                  |
| Visual               | Photos, Video, UAVs                                             | YOLOv8, Vision Transformers (ViT), EfficientNet | **Whether / How**: Detects real-time deviations from Design-for-Safety principles.                                                                                     |
| Temporal             | 4D Schedules, Progress Reports                                  | LSTM, VMD, Monte Carlo                          | **When**: Identifies high-risk phases and peak activity windows; probabilistic schedule simulation generates safety-risk heat maps for probability, time and location. |
| Environmental        | Sensor Data, Weather APIs                                       | IoT Integration, Time-series                    | **When**: Predicts weather-related hazards (rain and wind exaggerate lifting/fall risk).                                                                               |
| Relational           | Site Letters, RFIs, Emails, quality and safety incident reports | GraphRAG, Neo4j                                 | **Whether / How**: Identifies cascading risks, systemic, institutional and management failures.                                                                        |
| Sustainability / ESG | EPDs, ICE/EC3, GHG inventories, contractor ESG narratives       | Tabular ML, NLP on ESG text                     | **How / Whether**: Per-element embodied-carbon attribution and governance-risk scoring; provides dense supervision when safety labels are sparse.                      |

## 3.2 Technical Stacks
a. Core Module 1 will be implemented as three graph neural network sub-models over IFC element topology (PyTorch Geometric), one per discipline family (structural, envelope, MEP), with cross-modal attention incorporating text embeddings from specifications and CLIP-derived embeddings from site photographs. Calibration will be enforced via conformal prediction (MAPIE library), enabling coverage-guaranteed uncertainty outputs that Core Module 2 consumes as confidence weights.

b. Core Module 2 will be implemented as a Python loop calling the Core Module 1 Vertex AI Endpoint service, maintaining iteration history in BigQuery, and applying an update rule that perturbs design parameters in the direction of reduced predicted defect density. Convergence will be declared when the Chebyshev distance between successive parameter vectors falls below a calibration-derived threshold for three consecutive iterations. The Lyapunov-style argument constructs a candidate function L(state) equal to the expected future defect density under the current design; the update rule is designed to enforce L(t+1) less than or equal to L(t) given bounded Core Module 1 error, establishing expected monotone decrease.

c. Software and Hardware:
The entire stack will run on Google Cloud Platform using Vertex AI Custom Training (A2 instances with A100 GPUs), Cloud Storage for the raw and feature stores, Cloud SQL for PostgreSQL as the project registry, and Vertex AI Endpoints for Core Module 1 model serving.

Bayesian Networks and Causal Reasoning
Bayesian Networks (BNs) are probabilistic models that represent the interrelationships between safety factors and performance outcomes. A BN is constructed by identifying causal factors such as "Complex Facade Geometry," "Inadequate Edge Protection," and "High Wind Speed" and modeling their conditional dependencies. 

Using Bayesian inference, the system can quantify the probability of an accident (e.g., a fall from height) given specific design parameters. Output of Tornado Sensitivity Analysis Diagrams allows practitioners to identify the "root causes" of predicted risks. If the model predicts a high probability of a fall, the BN can trace this risk back to a specific design element, such as an unconventional or ample nos. floor opening that complicates the installation of guardrails. 

Table 2 - Candidate Algorithms and Frameworks for DfX Prediction

| Available Algorithm / Framework | Mathematical Basis                                                                                        | Application in Design-for-X                                                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Graph Neural Networks (GNN)     | $h_i^{(k+1)} = \mathrm{Agg}\big(\{h_j^{(k)} : j \in \mathcal{N}(i)\}\big)$                                | Capturing spatial and functional dependencies in BIM objects.                                                                                     |
| Bayesian Networks (BN)          | $P(A \mid B) = \dfrac{P(B \mid A)\,P(A)}{P(B)}$                                                           | Probabilistic root-cause tracing of safety / quality / sustainability outcomes; tornado sensitivity diagrams to identify dominant design drivers. |
| Monte Carlo Simulation          | $\int f(x)\,P(x)\,dx \approx \dfrac{1}{N}\sum_{i=1}^{N} f(x_i)$                                           | Modelling schedule uncertainty and spatial movement risk; propagating O2 uncertainty through O3 iterations.                                       |
| Contrastive Alignment (CLIP)    | $\mathcal{L} = -\log \dfrac{\exp(\mathrm{sim}(z_i, z_j)/\tau)}{\sum_k \exp(\mathrm{sim}(z_i, z_k)/\tau)}$ | Fusing site photos with BIM semantic data; zero-shot tagging of inspection imagery against IFC property strings / RFI text.                       |
| LSTM / GRU                      | Recurrent state gates over $\{x_t\}$                                                                      | Forecasting temporal accident trends and recovery periods.                                                                                        |
| YOLOv8-ADSC                     | Spatial Feature Fusion (ASFF)                                                                             | Real-time detection of PPE and hazards in complex site video.                                                                                     |
| Conformal Prediction (MAPIE)    | $P\big(y \in \hat{C}_\alpha(x)\big) \geq 1 - \alpha$                                                      | Distribution-free coverage-guaranteed uncertainty intervals on the O2 forward operator.                                                           |

Remarks – tentative approaches only, to be selected based on the data.

d. Per-objective method mapping (Table 3). Following standard PhD methodology presentation, each research objective is bound to a data subset, a concrete method stack, an implementation target, an evaluation protocol, and an explicit fallback. This makes the proposal independently assessable objective-by-objective and addresses the requirement to report research methods per objective.

Table 3 - Per-objective method mapping

|                     | **O1 — NLP Extraction**                                                                                                                                                                                                                  | **O2 — Forward Predictor**                                                                                                                                          | **O3 — Convergence Loop**                                                                                                                                                                                    | **O4 — Coupling**                                                                                                                                                                     |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data**            | Emails, letters, RFIs, specifications, inspection records, incident reports, site photos, contractor ESG narratives                                                                                                                      | O1 attributes + IFC graphs + CLIP photo embeddings + embodied-carbon labels (ICE/EPD)                                                                               | Parametric variants of the two case-study BIM models + O2 endpoint                                                                                                                                           | Iteration logs from O3 + checkpoint history from O1/O2                                                                                                                                |
| **Method**          | LLM with structured-output prompting (JSON schema + Chain-of-Thought, source-span citation enforced); GraphRAG over Neo4j for cross-document linkage; CLIP for photo-text alignment; Esmaeili/Tixier attribute schema as target ontology | GNN over IFC topology (PyTorch Geometric); cross-modal attention to O1 attribute embeddings; conformal prediction (MAPIE) for coverage-guaranteed intervals         | Python orchestrator calling O2 Vertex AI Endpoint; gradient-free perturbation update; Lyapunov candidate L(state) = expected defect density; Chebyshev-distance termination for three consecutive iterations | Periodic re-training of O1/O2 on (design variant, predicted defect, realised proxy) tuples generated by O3; checkpoint-vs-iterations-to-convergence regression with significance test |
| **Implementation**  | Vertex AI (Gemini / DeepSeek), Neo4j, Cloud Storage                                                                                                                                                                                      | Vertex AI Custom Training (A2 / A100), Vertex Endpoints                                                                                                             | Local Python loop, BigQuery iteration store                                                                                                                                                                  | Vertex Pipelines (scheduled), model registry                                                                                                                                          |
| **Evaluation**      | Precision / recall vs. expert-annotated constraint set on held-out documents; Cohen's κ on a 20 % re-annotated sample; cross-jurisdiction transfer test on RIDDOR / OSHA narratives                                                      | Element-level k-fold within each case project + project-2 as external validation set; calibration ECE and empirical coverage; ablation with and without O1 features | Iteration count, Pareto position (defect-density × cost) , wall-clock vs. Optuna TPE baseline and vs. the best published cognitive-DT proposal instantiable on the same case                                 | Correlation of checkpoint index ↔ iterations-to-convergence; co-improvement slope significance test; decomposed contribution analysis of O1/O2/O3                                     |
| **Risk / fallback** | LLM hallucination → reject extractions without grounded source spans; require human-in-the-loop review on a sampled subset                                                                                                               | Small-n cross-project generalisation → report element-level results as case-study evidence; release dataset and code to enable replication                          | No monotone decrease observed → report as diagnostic negative result and refine update rule                                                                                                                  | Coupling not observed → decompose and report O1/O2/O3 contributions independently                                                                                                     |

## 3.3 System Architecture
The digital twin system will be built by adopting classic 5-layer architecture (Figure 1).
 
 
 

## 3.4 Validation and evaluation
Core Module 1 forward predictor for DfX will be evaluated using project-level leave-one-project-out cross-validation. The sustainability head is evaluated via project-level embodied-carbon MAE (against EPD-derived ground truth) and ESG-narrative extraction precision/recall, providing fallback supervision when safety labels are sparse and hedging against late-stage data deadlock.
Core Module 2 self-improving convergence will be evaluated against two baselines - A gradient-free Bayesian optimiser (such as Optuna TPE sampler) applied to the same parametric design space, and the best published cognitive-DT proposal that can be instantiated on the same case study. Metrics for performance evaluation for the convergence are iteration count toward the convergence, quality of the converged solution (Pareto frontier position in defect-density / carbon / cost space), and elapsed time. Co-improvement will be measured as the correlation between iteration index and as the reduction in iterations-to-convergence between early and late model checkpoints.

Proposed validation case study:
Given a series of input i (BIM element such as a wall, beam, or MEP fitting) and design phase features (parameters, geometry, adjacency relations, logic link, code references), predict whether (binary classification) input  i will lead to incident and defects during construction and if positive, the expected number of defects  and incidents (regression) .

# 4. Significance  and Novelty
a. Existing cognitive digital twin frameworks [2] propose self-improvement conceptually but do not formalise convergence. 

b. Existing digital twin proposed 5-layersystem architecture [3] and demonstrated with case study but focus on operation only and lack feedback loop backward to design and construction phases, i.e., no life cycle analysis.

c. Existing closed-loop BIM research [4] feeds operational data back episodically without iteration and is only conceptual. 

d. Existing expert-iteration and self-play methods [5] being fed by no domain knowledge establish convergence theory in games of chess in single-phase design but have not been instantiated for cross-phase AECO with embedded forward prediction. 

This research aims to build the real system architecture in section 3.3 and occupies the intersection of these three bodies of work: formal cross-phase convergence instantiated in AECO with an embedded multi-modal predictor.

e. Methodological lineage. This work positions itself as a direct successor to the attribute-based Design-for-Safety paradigm established by Esmaeili & Hallowell and extended by Tixier et al., with two upgrades that are themselves contributions: (i) hand-engineered safety attributes are replaced by LLM-based extraction over heterogeneous project records, removing the manual-coding bottleneck that has constrained that line of work; and (ii) point-prediction risk scores are replaced by conformally calibrated likelihoods consumable by a closed-loop convergence operator, making the predictor deployable inside an autonomous iteration loop rather than as a static advisory KPI.

# 5. Conclusion and Future Work
## 5.1 Expected Contributions in stage 1 (year 1 -2)
Upon successful completion of the project in year 1-2, this research will deliver:

a. A formalised self-improving AECO digital twin architecture with proven convergence conditions, which will be the first such system in the AECO literature to characterise cross-phase convergence mathematically.

b. A trained, calibrated, multi-modal element-level DfX predictor (defect / safety / sustainability heads) validated on real cross-project data.
	
c. An open-source cross-phases digital twin prototype has potential for industry level application.

d. The thesis integrates all the theoretical, algorithmic, system-level, empirical, and prototype demonstration into a single coherent argument.

## 5.2 Future works in stage 2 (year 3 – 4)

Stage 2 pursues parallel tracks that scale, generalise, and elevate the Stage-1 framework without retracting any of its claims. Tracks (a), (b) and (e) extend the methodological depth; track (c) addresses the data-volume frontier that Stage 1 deliberately bounded to two anchor case studies; track (d) closes the operation-phase loop.

a. Dynamic Success Prediction via FRS-Calibrated Agent-Based Modelling.
The Cognitive Digital Twin (CDT) framework will transition from diagnostic risk scoring to predictive "Goal Navigation." A spatiotemporal Agent-Based Model (ABM) will be constructed to simulate autonomous worker behaviours and site dynamics. Instead of relying on rigid heuristics, the ABM's parameter thresholds will be dynamically calibrated using the conformally-calibrated risk surfaces learned in Stage 1. Operating as a "Front Running Simulation" (FRS) in the tradition adopted by NASA [6], this engine will execute thousands of forward-looking Monte Carlo scenarios, outputting real-time safety incident probability distributions and dynamic hazard heatmaps. Planners will be able to conduct proactive "what-if" scenario analyses, bridging construction realities directly back to design-stage optimisation — i.e. achieving design-for-safety in a continuous information-flow system.

b. Multimodal (Tacit-to-Explicit) Knowledge Fusion for Cognitive Safety Reasoning.
The research will pioneer an AI-native reasoning paradigm by fine-tuning a multimodal Foundation Model on the curated domain-specific AECO corpus established in Stage 1. Moving beyond tabular classification, this engine will use Chain-of-Thought (CoT) prompting to process heterogeneous project inputs simultaneously (IFC geometry, site photographs, contractual emails). It will translate unstructured text such as historical incident reports into actionable "Shift-Left" design constraints, outputting natural-language risk explanations alongside prescriptive design alternatives.

c. Industrial-scale dataset acquisition and cross-jurisdiction validation.
Stage 1 establishes the framework, methodology, and prototype on two deeply-instrumented anchor case studies sourced through the candidate's active industry role. Stage 2 will scale this evidentiary base through a structured data-acquisition campaign, exploiting the candidate's full-time position as a project manager in an engineering consultancy and the supervisor's standing industry network:

 - **(c.i)** A firm-level archive request, anonymised under an academic-use data-governance agreement, targeting 8–12 additional completed projects with full BIM, correspondence, inspection, and non-conformance (NCR) records, enabling genuine leave-one-project-out cross-validation of Core Module 2.
 - **(c.ii)** Memoranda of Understanding with two or three main-contractor partners to obtain element-level NCR registers and detailed incident investigations, providing the element-linked labels required to upgrade Core Module 2 from case-study evidence to a population-level claim.
 - **(c.iii)** Formal data-access requests to the Occupational Safety and Health Council (OSHC), the Construction Industry Council (CIC), and the Hong Kong Labour Department, targeting 50–100 additional anonymised incident narratives for supervised refinement of the Core Module 1 extractor.
 - **(c.iv)** Use of international public corpora — UK HSE RIDDOR, US OSHA 300, Safe Work Australia — as auxiliary pre-training and cross-jurisdiction transfer-testing data for the Core Module 1 LLM extractor, supporting a generalisability claim that Stage 1 alone cannot make.

The campaign is deliberately scheduled for Stage 2 because instrument readiness (the O1 extraction pipeline, the O2 calibration protocol, the O3 update rule) must be demonstrated on the anchor case studies before scaling justifies the data-governance overhead. With the Stage-1 instrument in hand, the Stage-2 dataset turns the validated framework into a peer-review-ready statistical claim and a deployable industrial artefact.

d. Operation-phase closure.
Stage 1 closes the design → construction half of the lifecycle loop. Stage 2 will close the construction → operation → design half by integrating post-handover defect-liability records, facility-management helpdesk tickets, and (where instrumented) building-management-system sensor streams from at least two completed case projects, completing the full cross-phase digital-twin loop posited in §2.

e. Human-behaviour integration (Flyvbjerg optimism bias × HRO theory).
Stage 2 will lift the unit of analysis from element to actor. Designer-side decision distortions will be modelled following Flyvbjerg's optimism-bias / reference-class forecasting paradigm to debias Core Module 1 cost/duration priors; site-side actor reliability (workers, frontline supervisors) will be modelled following Guo Wai's High-Reliability Organisation (HRO) theory, providing behavioural priors for the FRS-ABM in track (a). Together these close the human loop that the Stage-1 element-level twin deliberately bounds.

# 7. References
[1]	Alec Radford, “Learning transferable visual models from natural language supervision,” in Proceedings of Machine Learning Research, OpenAI. [Online]. Available: https://proceedings.mlr.press/v139/radford21a/radford21a.pdf

[2]	Y. Zheng, S. Yang, and H. Cheng, “An application framework of digital twin and its case study,” J. Ambient Intell. Humaniz. Comput., vol. 10, no. 3, pp. 1141–1153, Mar. 2019, doi: 10.1007/s12652-018-0911-3.

[3]	Q. Lu et al., “Developing a Digital Twin at Building and City Levels: Case Study of West Cambridge Campus,” J. Manag. Eng., vol. 36, no. 3, p. 05020004, May 2020, doi: 10.1061/(ASCE)ME.1943-5479.0000763.

[4]	E. A. Pärn, D. J. Edwards, and M. C. P. Sing, “The building information modelling trajectory in facilities management: A review,” Autom. Constr., vol. 75, pp. 45–55, Mar. 2017, doi: 10.1016/j.autcon.2016.12.003.

[5]	D. Silver et al., “Mastering chess and shogi by self-play with a general reinforcement learning algorithm,” Dec. 05, 2017, arXiv: arXiv:1712.01815. doi: https://doi.org/10.48550/arXiv.1712.01815.

[6]	M. Grieves and J. Vickers, “Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems,” pp. 85–113, 2017, doi: 10.1007/978-3-319-38756-7_4.


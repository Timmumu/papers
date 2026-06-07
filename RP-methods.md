# RP-methods — A Practitioner's Walkthrough of Table 3

> **Audience.** You are a construction PM with 10+ years on-site experience and limited prior exposure to computer-science jargon. This document explains every method, library, and abbreviation that appears in the four columns of Table 3 of `RP.md`. Each section uses a construction analogy first, then names the technical term.

---

## 0. The 30-second mental model

Think of the whole proposal as a **closed-loop project-control system**, the same way you already think about an EVM/PMI cycle:

| Construction analogy | Computer-science term in RP |
|---|---|
| Reading site letters, RFIs, NCRs to extract "what went wrong" | **O1 — NLP extraction** |
| Predicting which beam / wall / MEP riser will go wrong on the next project | **O2 — Forward predictor** |
| Iteratively tweaking the design until the predicted incident rate drops below tolerance | **O3 — Convergence loop** |
| Letting yesterday's loop outputs train tomorrow's predictor (so the system gets smarter) | **O4 — Coupling** |

Everything else in Table 3 is just the **tools, vocabulary, and quality-control checks** for those four steps.

---

## 1. Foundations you only need to learn once

### 1.1 What is a "model"?
A model is a function $f(x) = y$ that takes inputs $x$ (e.g., wall geometry, material, weather) and returns an output $y$ (e.g., probability the wall develops a defect). The function's internal numbers ("**weights / parameters**") are not designed by hand — they are *fitted* to historical data.

### 1.2 Training vs. inference
- **Training**: feeding the model a large set of historical (input, correct-answer) pairs and adjusting its weights until it predicts the correct answer most of the time. Analogous to a junior engineer reviewing 10 000 past NCR reports until they internalise the patterns.
- **Inference**: using the trained model on a *new* unseen input. Analogous to the now-experienced engineer reviewing a fresh design and pointing out likely defects.

### 1.3 Supervised learning
Training where every input has a known correct answer (a "**label**"). Almost all of Core Module 1 is supervised: the labels come from NCR registers, incident reports, EPD carbon values, etc.

### 1.4 What is "deep learning" / a "neural network"?
A model composed of many simple multiply-and-add operations arranged in **layers**. The "deep" just means *many layers*. The reason it matters: deep networks can learn from raw data (geometry, photos, text) without you hand-engineering features. That is why we use them on BIM and site photos rather than classical statistics.

---

## 2. O1 — NLP Extraction (the "intelligent clerk")

**Goal.** Read every piece of project text and image you have (RFIs, emails, NCRs, site photos) and extract structured DfX risk attributes linked back to specific IFC elements.

### 2.1 LLM — Large Language Model
The same family of model as ChatGPT / Gemini / Claude. A model trained on billions of documents that can read, summarise, and follow instructions in natural language. In this project the LLM acts as your tireless graduate engineer who reads every RFI ever issued.

### 2.2 Structured-output prompting (JSON schema)
By default an LLM writes prose. We force it to output a fixed **JSON** template (a key-value form, much like a parametric Revit family schedule) so downstream software can ingest the answer mechanically. Example output:

```json
{
  "element_guid": "3kQ9X...",
  "hazard": "fall from height",
  "evidence_quote": "no edge protection at slab edge",
  "source_doc": "RFI-024.pdf, p.2"
}
```

### 2.3 Chain-of-Thought (CoT) prompting
We instruct the LLM to **think step-by-step** before answering. Analogous to making a graduate engineer write down their reasoning on a margin note instead of just ticking yes/no. Improves accuracy on multi-step inference.

### 2.4 Source-span citation
The LLM must quote the exact sentence in the source document that justifies its answer. This is your audit trail — equivalent to demanding "cite the clause" instead of "trust me". This is the main defence against **hallucination** (the LLM making things up).

### 2.5 GraphRAG over Neo4j
- **RAG** = Retrieval-Augmented Generation. Before answering, the LLM first *retrieves* the most relevant snippets from a knowledge base. Like a junior engineer who pulls the right specification page before drafting a memo.
- **Graph** RAG: the knowledge base is a **graph** of entities (people, elements, events) and their links (e.g., RFI-024 → references Wall-W3 → cited in NCR-117). This lets the LLM see *connections across documents*.
- **Neo4j** is the database product that stores that graph.

Construction analogy: imagine a wall in your site office where every NCR, RFI, and photo is pinned and strings of yarn connect related items. GraphRAG is software that does this automatically.

### 2.6 CLIP — Contrastive Language-Image Pre-training
A model from OpenAI that places images and text in the **same vector space**. Practical effect: you can ask in plain English *"show me photos that look like inadequate edge protection"* and CLIP retrieves matching site photos without anyone having tagged them. We use CLIP to align site inspection photos with BIM property strings / RFI text.

### 2.7 Esmaeili / Tixier attribute schema
A peer-reviewed **vocabulary** of safety attributes (e.g., "working at height ≥ 6 m", "lifting near energised lines") published by construction-safety researchers. We adopt their list as our target ontology so the model's output is comparable to prior literature.

### 2.8 Vertex AI / Gemini / DeepSeek / Cloud Storage
- **Vertex AI** = Google Cloud's managed platform for training and serving AI models. Think of it as the rented "AWS-like" plant for our digital tools.
- **Gemini** = Google's flagship LLM family; **DeepSeek** = a high-performing open-source LLM from China. We may use either depending on cost / data-sovereignty constraints.
- **Cloud Storage** = the cloud equivalent of a project SharePoint / file server — but accessible to the AI training jobs at high bandwidth.

### 2.9 Evaluation metrics
- **Precision** = of the items the model flagged as risks, what fraction were really risks. (Low precision = noisy / false alarms.)
- **Recall** = of all the real risks present, what fraction did the model catch. (Low recall = missed hazards.)
- **Cohen's κ (kappa)** = a number between 0 and 1 measuring **how much two human annotators agree** beyond chance. We hire a second engineer to re-annotate 20 % of the documents; κ > 0.6 means our gold-standard labels are trustworthy. (κ = 1 perfect, κ = 0 chance-level.)
- **RIDDOR** = UK's *Reporting of Injuries, Diseases and Dangerous Occurrences Regulations* — a public incident database.
- **OSHA** = US Occupational Safety and Health Administration; OSHA 300 is its incident log dataset.
We use RIDDOR / OSHA narratives as an **out-of-jurisdiction transfer test** — does our model still work on data it has never seen, written in a different regulatory style?

---

## 3. O2 — Forward Predictor (the "experienced engineer's gut feel, quantified")

**Goal.** Given a BIM element + attributes from O1, output the probability of defect / safety incident / sustainability shortfall, **with a calibrated confidence interval**.

### 3.1 GNN — Graph Neural Network
A neural network that operates on **graphs** instead of grids (images) or sequences (text). A BIM model is naturally a graph: every wall is connected to slabs, beams, doors, MEP penetrations. A GNN "passes messages" between connected elements so that the prediction for one wall takes into account its neighbours.

Construction analogy: when judging risk on a particular column, you instinctively also look at the beams it supports, the slab above, and the formwork around it. A GNN encodes that instinct mathematically.

### 3.2 IFC topology
**IFC** = Industry Foundation Classes — the open BIM exchange standard you already know from Revit / Solibri exports. "Topology" here means *which element is connected to which*, not the geometry coordinates.

### 3.3 PyTorch Geometric
The specific software library (open source, Python) that implements GNNs on top of PyTorch (Facebook/Meta's deep-learning framework). Think of it as the AutoCAD-LISP of GNN programming — a toolbox of pre-built bricks.

### 3.4 Cross-modal attention
"**Modal**" = data type (geometry, text, photos). "**Cross-modal attention**" is the mechanism that lets the GNN selectively *pay attention* to relevant text/photo evidence when judging a particular element. Analogous to an engineer reading both the drawing **and** the spec **and** the site photo, weighting whichever is most informative for the current decision.

### 3.5 Conformal prediction & MAPIE
- **Conformal prediction** = a mathematical framework that wraps any black-box predictor and produces an interval (e.g., "defect probability is between 12 % and 28 %") with a **guaranteed coverage**: if we promise 90 % coverage, the true answer falls inside the interval at least 90 % of the time. *No assumption about the underlying data distribution is required* — hence "distribution-free".
- **MAPIE** = **M**odel-**A**gnostic **P**rediction **I**nterval **E**stimator — an open-source Python library that implements conformal prediction. We use it because Core Module 2 (the convergence loop) needs to know *how confident* each prediction is before acting; a bare point estimate is unsafe.

Construction analogy: instead of a single contractor's tender ("it will cost $5.2 M"), you get a calibrated range ("90 % chance the true cost lies between $4.8 M and $5.7 M"). The convergence loop needs the range, not just the midpoint.

### 3.6 Vertex AI Custom Training (A2 / A100) & Endpoints
- **A2 instance / A100 GPU** = a Google Cloud virtual machine class fitted with NVIDIA A100 GPUs (the same chips that power most modern AI training). High-end hardware needed because GNN training is computation-heavy.
- **Vertex Endpoint** = the published REST URL where the trained model lives, so the Core Module 2 Python loop can call it just like calling a web service.

### 3.7 Evaluation metrics
- **k-fold cross-validation** = split the data into k slices, train on k−1, test on 1, rotate, average. Standard way to avoid being fooled by lucky train/test splits.
- **Element-level k-fold** means each *element* (not each project) is a data point.
- **External validation set** = an entirely different project never seen during training — the strongest possible test.
- **ECE — Expected Calibration Error** = a number measuring whether your model's stated "70 % confidence" really comes true 70 % of the time on average. Lower is better.
- **Empirical coverage** = the *measured* hit rate of the conformal interval (target 90 %, hope to see ~90 % in practice).
- **Ablation** = remove one feature group (e.g., O1 text attributes) and re-run, to prove that feature group actually contributes.

---

## 4. O3 — Convergence Loop (the "iterative value-engineering session, automated")

**Goal.** Use the predictor (O2) inside a loop that automatically perturbs the parametric design until predicted defect / incident / carbon drops below tolerance and the iterations stabilise.

### 4.1 Python orchestrator + Vertex AI Endpoint
A short Python program that, in a loop:
1. proposes a candidate design (parametric variant);
2. POSTs it to the O2 endpoint and reads back the predicted DfX scores + intervals;
3. computes a perturbation (small change) towards a better design;
4. repeats.

Analogous to a value-engineering workshop that runs *automatically, thousands of iterations per hour*.

### 4.2 Gradient-free perturbation update
- A "**gradient**" tells you which direction reduces the loss fastest. We do not have one (the O2 model is treated as a black box), so we use a **gradient-free** method — small random perturbations + keep what improves things. Methods include Bayesian optimisation, evolutionary search, Optuna TPE.

### 4.3 Lyapunov candidate $L(\text{state})$
A piece of mathematical control theory borrowed from rocket guidance. We define a **scalar energy-like quantity** $L$ = expected future defect density under the current design. If we can prove $L(t+1) \le L(t)$ at every step (under reasonable error bounds on O2), the loop is *guaranteed* to converge — it cannot oscillate forever. Analogous to proving a pendulum will eventually settle because energy keeps dissipating.

### 4.4 Chebyshev-distance termination
Stop the loop when the **maximum** absolute change across any design parameter is below a small threshold ε for three consecutive iterations. ("Chebyshev distance" = the largest single-axis difference; in plain English: "no parameter is wobbling by more than ε any more"). Three consecutive matches guard against accidental early stops.

### 4.5 BigQuery iteration store
**BigQuery** = Google's cloud data warehouse (think: SQL database, but it scales to terabytes effortlessly). We log every iteration there for audit and later analysis. This becomes the training data for O4.

### 4.6 Baselines
- **Optuna TPE sampler** = a popular open-source Bayesian-optimisation library; TPE = "Tree-structured Parzen Estimator", a method to choose the next promising design parameter. Our loop must beat this off-the-shelf optimiser to claim novelty.
- **Pareto position** = on a 2-D plot of (defect-density vs. cost) or (carbon vs. cost), the **Pareto frontier** is the set of designs that cannot be improved on one axis without harming the other. Being *closer* to the frontier = a better trade-off.
- **Wall-clock** = real elapsed time (literally what a clock on the wall would show), not CPU time. Used so the comparison is fair to the user.

---

## 5. O4 — Coupling (the "system gets smarter from its own use")

**Goal.** Re-train O1 / O2 periodically on the new data generated by O3, and show that this *closed loop* produces faster convergence over time — the central novelty claim.

### 5.1 (design variant, predicted defect, realised proxy) tuples
Every iteration of O3 produces a triple: the design we tried, the prediction we made, and a *proxy* for what actually happened (e.g., the next-iteration consensus, or — when available — real site outcome data). These triples form a fresh training set for O1 / O2.

### 5.2 Periodic re-training
Re-run training of O1 / O2 on the enlarged dataset on a schedule (e.g., monthly). Each new version of the model is a **checkpoint**.

### 5.3 Vertex Pipelines + model registry
- **Vertex Pipelines** = a scheduled workflow orchestrator on Google Cloud (think of it as a project Gantt schedule, but for ML retraining jobs).
- **Model registry** = a versioned catalogue of trained model checkpoints (similar to a BIM model coordination folder with revisions A, B, C…). Lets you roll back to a previous model if a new training run degrades performance.

### 5.4 Evaluation: checkpoint vs. iterations-to-convergence regression
Plot the **checkpoint number (time)** on the X-axis against the **average number of O3 iterations needed to converge** on the Y-axis. If the system is genuinely self-improving, this curve should slope **downward** — later checkpoints converge faster.

### 5.5 Significance test
A statistical test (e.g., paired t-test, Spearman rank correlation with p-value) confirming the downward slope is not just noise. The proposal is *falsified* if no statistically significant downward slope is detected (see O4 falsifiability bullet in RP).

### 5.6 Decomposed contribution analysis
If coupling is observed, decompose the gain: how much came from a better O1 extractor? a better O2 predictor? a better O3 update rule? This is the diagnostic to write up in the thesis.

---

## 6. Cross-cutting concepts

| Term | What it means | Construction analogy |
|---|---|---|
| **Feature** | One input column to a model | A column in your project KPI spreadsheet |
| **Embedding** | A numerical vector representation of a complex object (text, image, BIM element) | A unique fingerprint, ~512 numbers long |
| **Loss function** | A formula quantifying how wrong the model's prediction is | The variance between forecast and actual progress |
| **Backbone** | The shared core of a neural network before it branches into task-specific "heads" | The same structural frame supporting different finishes |
| **Head** | The final layer producing one specific output (defect / safety / sustainability in our case) | The branch services off a common riser |
| **Hallucination** | An LLM confidently making up a "fact" not in the source | A contractor inventing an instruction that was never issued |
| **Hyperparameter** | A setting chosen by the engineer, not learned (e.g., learning rate, network depth) | The procurement strategy — chosen by you, not by the project |
| **Overfitting** | Model memorises training data and fails on new data | A graduate who can recite past projects verbatim but cannot judge a new site |
| **Generalisation** | The opposite of overfitting — works on unseen projects | A senior engineer's transferable judgement |

---

## 7. How to use this document

1. **First pass.** Read sections 0 and 1 — these give you the mental model.
2. **As a glossary.** Whenever an abbreviation appears in `RP.md`, jump to its section here.
3. **Before the panel defence.** Re-read sections 2–6 once; the panel will probe the methods cell of Table 3, and you should be able to answer in your own words using the analogies above.
4. **If a method seems unjustified.** Check the corresponding **falsifiability bullet** in `RP.md` §2 — it tells you what failure looks like and how we will detect it.

> Anything still unclear? Ask the supervisor or copy the question back to this assistant — happy to extend any section with worked examples.

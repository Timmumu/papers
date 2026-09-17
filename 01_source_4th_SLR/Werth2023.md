# Werth, A.W et al. (2023) — A digital twin internal to a PLC to detect malicious commands and ladder logic that potentially cause safety violations

- **ID:** R755 | **Source:** Scopus | **DOI:** 10.1080/23742917.2023.2171538
- **Journal:** Journal of Cyber Security Technology
- **Authors:** Werth A.W.; Morris T.H.

## Abstract summary
This work presents an Intrusion Prevention System (IPS) called the Embedded Process Prediction Intrusion Prevention System (EPPIPS) to detect cyber-attacks by predicting what harm the attacks could cause to the physical process in critical infrastructure. EPIPPS is a digital twin internal to a Programmable Logic Controller (PLC). EPPIPS examines incoming command packets and programs sent to the PLC. If EPPIPS predicts these packets or programs to be harmful, EPPIPS can potentially prevent or limit the harm. EPPIPS consists of a module that examines the packets that would alter settings or actuators and incorporates a model of the physical process to aid in predicting the effect of processing the command. Specifically, EPPIPS determines whether a safety violation would occur for critical variables in the physical system. Experiments were performed on virtual testbeds involving a water tan…

## Step-1 Screening (Prompt A)
| G Domain AECO | H DT core | I DfS/DfQ/PtD | J Pub-type | K English | Decision |
|---|---|---|---|---|---|
| No | Yes | Yes | Yes | Yes | **Exclude** |

**Note:** PLC-internal DT IPS; industrial security

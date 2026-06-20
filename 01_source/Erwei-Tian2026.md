---
ref: ""
citekey: "Erwei-Tian2026"
title: "Quantum Encryption Techniques for Securing Low-Voltage Communication Systems in Next-Generation Data Transmission Networks"
authors: "Erwei Tian"
year: 2026
journal: "Ingegneria Sismica"
doi: "10.65102/is20261017"
zotero_key: "QTQJQ6IW"
zotero_status: abstract-grounded
last_verified: "2026-06-15"
tags: ["Digital-Twin", "Energy", "Maintenance", "Risk", "Unsorted", "source: lens", "identification: databases"]
---
# Erwei-Tian2026 — Quantum Encryption Techniques for Securing Low-Voltage Communication Systems in Next-Generation Data Transmission Networks

| Field | Value |
|-------|-------|
| **Ref** | — |
| **Authors** | Erwei Tian |
| **Year / Venue** | 2026 · *Ingegneria Sismica* |
| **DOI** | [10.65102/is20261017](https://doi.org/10.65102/is20261017) |
| **Zotero** | `QTQJQ6IW` |
| **Screening** | V1: digital twin \| V2: structure \| V3: risk|energy|maintenance |

## Abstract ^sec-abstract

Low-voltage communication systems in next-generation data transmission networks connect smart meters, feeder controllers, EV chargers, and distributed energy resources; however, the dense topological structure they have and the limited abilities of their endpoints make the direct deployment on quantum hardware be not practical. In order to solve this restriction, this article puts forward a Hybrid Quantum Encryption Scheme for Low-Voltage Systems (HQES-LV), which keeps quantum key distribution on backbone and gateway layers, uses a post-quantum authenticated control plane, and gives lightweight session protection to edge devices by means of risk-adaptive key renewal. A literature-calibrated digital twin is constructed to simulate mixed control, telemetry, and maintenance traffic, along with replay attacks, man-in-the-middle probing, quantum channel degradation, and gateway outages. Result data indicate that in the pressure condition, the HQES-LV can cut control waiting time down to 6.1 ms, hold the possibility of secret information leakage to 0.4%, and make the time of getting back to normal shorter to 6.7 s. Under a 1.2 p.u. load, it maintains 7.3 ms latency and 98.4% session establishment success. When QBER rises to 5.5%, the proposed scheme still preserves 58.9% effective key availability and 96.7% packet delivery. These findings indicate that practical quantum security for low-voltage systems should be realized through hierarchical orchestration rather than endpoint quantumization, and that the combination of QKD backbone supply, post-quantum fallback, and the adaptive session arrangement can provide a path that is more ready for deployment for future electric power communication networks.

## Introduction & Background ^sec-intro

Low-voltage communication systems in next-generation grids connect smart meters, feeder controllers, EV chargers, and distributed energy resources, but their dense topology and limited endpoints make direct quantum-hardware deployment impractical. The paper proposes a Hybrid Quantum Encryption Scheme for Low-Voltage Systems (HQES-LV).

## Method ^sec-method

HQES-LV keeps quantum key distribution on backbone/gateway layers, uses a post-quantum authenticated control plane, and applies risk-adaptive session protection to edge devices. A **literature-calibrated digital twin** simulates mixed control/telemetry/maintenance traffic plus replay, man-in-the-middle, quantum-channel degradation, and gateway-outage attacks.

## Key Findings ^sec-results

Under stress, HQES-LV cuts control latency to 6.1 ms, holds leakage probability at 0.4%, and reduces recovery to 6.7 s; at 1.2 p.u. load it maintains 7.3 ms latency and 98.4% session success; at 5.5% QBER it preserves 58.9% key availability and 96.7% packet delivery. Hierarchical orchestration outperforms endpoint quantumisation.

## Discussion & Implications ^sec-discussion

**Off-topic / domain-adjacent** — a smart-grid cybersecurity study where DT is only a simulation testbed. Outside the AECO built-environment focus; recommend exclusion or peripheral citation on DT-as-testbed/security.

## Notes ^sec-notes

- **Screening:** Retained by keyword only — power-grid quantum security; **DT used only as simulation testbed**.
- **Relevance:** Very low (non-AECO); recommend exclusion / demotion.
- **Source:** Abstract-grounded; full text pending.

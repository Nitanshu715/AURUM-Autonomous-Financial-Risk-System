<div align="center">

<br/>

<h1>⚙️ AURUM</h1>
<h3>Autonomous Unified Risk Intelligence for Financial Systems</h3>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Prototype-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/Architecture-6--Layer_Pipeline-6A0DAD?style=flat-square)

<br/>

*A multi-layer autonomous pipeline that converts raw system signals into governed risk decisions — no human in the loop.*

<br/>

</div>

---

## What is AURUM?

AURUM is an architectural prototype demonstrating how **anomaly detection**, **predictive trend analysis**, **risk scoring**, **decision logic**, and **automated response** can be unified into a single, continuously executing intelligence pipeline.

It was built by converging two independent systems — **Helios** (anomaly detection) and **Hyperion** (prediction and decision) — under a single orchestration layer. The result is a pipeline where each stage transforms raw signals into progressively higher-level meaning, ultimately producing a governed, automated response.

The focus is not isolated model complexity. It's **reasoning flow**: signals → interpretation → projection → risk abstraction → governance decision → action.

---

## Pipeline Architecture

AURUM operates across six logically independent but sequentially connected layers:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Layer 1 ── Signal Simulation                          │
│               transaction volume · login attempts       │
│               network activity                          │
│                          │                              │
│   Layer 2 ── Detection Engine          [Helios]         │
│               threshold-based anomaly flagging          │
│                          │                              │
│   Layer 3 ── Prediction Engine         [Helios]         │
│               trend-based stress forecasting            │
│                          │                              │
│   Layer 4 ── Risk Intelligence Layer                    │
│               weighted score fusion:                    │
│               anomaly + predicted stress + intensity    │
│                          │                              │
│   Layer 5 ── Decision Engine           [Hyperion]       │
│               risk score → governance state mapping     │
│               NO_ACTION · ALERT · REMEDIATE             │
│                          │                              │
│   Layer 6 ── Action Execution                           │
│               simulated operational response            │
│               integration point for automation hooks    │
│                                                         │
└─────────────────────────────────────────────────────────┘
                           │
                           ▼
                  incident_log.json
               (structured audit trail)
```

The orchestrator (`main_orchestrator.py`) manages execution order and data passing across all layers. Each stage outputs structured data consumed by the next — detection produces anomaly flags, prediction produces stress forecasts, the risk layer fuses them, the decision layer interprets the score, and the action layer executes the outcome.

---

## Layer-by-Layer Breakdown

**Layer 1 — Signal Simulation**
Generates three runtime telemetry proxies: transaction volume, login attempts, and network activity. These simulate financial system signals without requiring live API access.

**Layer 2 — Detection Engine**
Applies threshold-based conditional rules inspired by Isolation Forest logic to flag anomalous states. A signal is marked anomalous when it exceeds predefined activity bounds.

**Layer 3 — Prediction Engine**
Applies trend-based forecasting (originally developed for CPU stress in Hyperion) reinterpreted as forward-looking system stress. Outputs a numerical stress projection consumed by the risk layer.

**Layer 4 — Risk Intelligence Layer**
Constructs a composite risk score using weighted contributions:
```
risk_score = anomaly_contribution + predicted_stress_contribution + transaction_intensity_contribution
```
This demonstrates weighted multi-signal reasoning rather than naive binary alerting.

**Layer 5 — Decision Engine**
Maps the numerical risk score to a qualitative governance state, abstracting how autonomous systems convert quantitative metrics into actionable system directives.

| Risk Score Range | Decision State |
|---|---|
| Low | `NO_ACTION` |
| Moderate | `ALERT` |
| High | `AUTONOMOUS_REMEDIATION` |

**Layer 6 — Action Execution**
Simulates operational response. Though currently output to console and `incident_log.json`, this layer is designed as a clean integration point for real automation frameworks, webhooks, or remediation APIs.

---

## Repository Structure

```
AURUM-Autonomous-Financial-Risk-System/
│
├── helios_detection_engine/          # Layers 2 & 3 — detection + prediction logic
├── hyperion_decision_engine/         # Layers 5 & 6 — decision mapping + action execution
│
├── main_orchestrator.py              # Runtime controller — manages layer execution & data flow
├── incident_log.json                 # Structured audit trail of all processed incidents
│
├── AURUM_Project_Documentation.docx  # Full system documentation
└── README.md
```

---

## Running AURUM

```bash
# Clone
git clone https://github.com/Nitanshu715/AURUM-Autonomous-Financial-Risk-System.git
cd AURUM-Autonomous-Financial-Risk-System

# Install dependencies
pip install scikit-learn pandas numpy

# Run the pipeline
python main_orchestrator.py
```

**Sample output:**

```
[SIGNAL]    transaction_volume=847 | login_attempts=23 | network_activity=HIGH
[DETECT]    Anomaly flagged — transaction_volume exceeds threshold
[PREDICT]   Projected stress index: 7.2
[RISK]      Composite score: 8.6
[DECISION]  AUTONOMOUS_REMEDIATION
[ACTION]    Executing remediation protocol...
[LOG]       Incident written → incident_log.json
```

---

## Incident Log Schema

Every cycle writes a structured record to `incident_log.json`:

```json
{
  "timestamp": "2025-03-15T14:32:01Z",
  "signals": {
    "transaction_volume": 847,
    "login_attempts": 23,
    "network_activity": "HIGH"
  },
  "anomaly_detected": true,
  "predicted_stress": 7.2,
  "risk_score": 8.6,
  "decision": "AUTONOMOUS_REMEDIATION",
  "resolved": true
}
```

This log is the foundation for post-incident forensics, decision logic backtesting, and future model training on real incident replay data.

---

## Engineering Notes

A few real integration challenges solved during development:

- **Cross-repository merging** — Helios and Hyperion had independent directory structures and import paths; these were reconciled without deep rewrites of the underlying logic
- **Consistent data passing** — each layer needed a well-defined output contract so the next stage could consume it without assumptions
- **Preserving modularity** — the architecture allows swapping the detection or prediction engine independently without touching the orchestrator or downstream layers

---

## Limitations

AURUM is a controlled simulation prototype. It does not currently interface with live financial APIs, databases, or external data streams. All signals are runtime-generated proxies. This is intentional — the project's goal is architectural demonstration, not production deployment.

---

## Potential Extensions

- Live market feed ingestion via Yahoo Finance or Alpha Vantage
- Streamlit dashboard for real-time risk monitoring and incident replay
- Reinforcement learning policy trained on `incident_log.json` for adaptive decisions
- SNS / Slack integration for operator alerts on high-severity incidents
- Terraform-based deployment for cloud-hosted continuous operation

---

## Related Projects

| Project | Contribution to AURUM |
|---|---|
| [Helios](https://github.com/Nitanshu715/Helios) | Detection & prediction engine layers |
| [Hyperion](https://github.com/Nitanshu715/Hyperion) | Decision mapping & action execution layers |

---

## Author

<div align="center">

**Nitanshu Tak**

[![GitHub](https://img.shields.io/badge/GitHub-Nitanshu715-181717?style=flat-square&logo=github)](https://github.com/Nitanshu715)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nitanshu_Tak-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/nitanshu-tak-89a1ba289/)
[![Email](https://img.shields.io/badge/Email-nitanshutak070105%40gmail.com-D14836?style=flat-square&logo=gmail)](mailto:nitanshutak070105@gmail.com)

</div>

---

<div align="center">
<sub>MIT License · Built as an architectural prototype for autonomous risk pipeline design</sub>
</div>

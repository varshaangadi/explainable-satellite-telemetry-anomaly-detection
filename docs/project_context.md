# SAT Project Context

## Project
Explainable AI-Based Satellite Telemetry Anomaly Detection and Spacecraft Health Monitoring

## Current Research Question
Can classical ML and temporal deep-learning models detect anomalous behaviour
in real spacecraft telemetry, while producing interpretable channel-level
evidence for the detected anomaly?

---

## Overall Project Status

Project start: 8 October 2026

Core target: 31 October 2026

Current stage: Day 2 — Dataset Anatomy

Current task: Task 0 completed

Next task: Task 1 — Inspect dataset.csv and segments.csv

---

## Completed Milestones

### Day 1 — 8 October 2026
- Project plan reviewed.
- Research objective established.
- One-page project map completed.
- Official RESPOND 2024 material reviewed.
- OPSSAT-AD 2025 paper reviewed.
- GitHub repository created.
- Repository structure created.
- OPSSAT-AD v2 downloaded and verified.
- Data Card completed.
- Decision Log completed.
- Python 3.12 environment configured.
- Jupyter kernel configured.
- Initial dataset inspection notebook created and run successfully.
- Day 1 documentation committed and pushed to GitHub.

### Day 2 — Dataset Anatomy
- Task 0: workspace/environment verification completed.
- Existing notebook confirmed:
  notebooks/01_dataset_inspection.ipynb
- Python 3.12 project environment confirmed.
- OPSSAT-AD source files confirmed available locally.
- No raw dataset files modified.

---

## Primary Dataset

OPSSAT-AD

Source:
https://zenodo.org/records/15108715

Primary research paper:
Ruszczak et al. (2025),
"The OPS-SAT benchmark for detecting anomalies in satellite telemetry."

Dataset characteristics already verified:
- dataset.csv: 2,123 rows × 23 columns
- segments.csv: 303,493 rows × 8 columns
- 9 source telemetry channels
- published train/test split
- raw telemetry representation plus handcrafted-feature representation

---

## Core Models

1. Statistical / threshold-based baseline
2. Isolation Forest
3. LSTM Autoencoder

These are parallel approaches.

Transformer-based approaches remain optional and must not delay the core system.

---

## Explainability Scope

The project aims to provide channel/signal-level evidence for detected anomalies.

This does NOT mean:
- proving physical spacecraft root cause
- diagnosing the exact hardware failure
- claiming operational deployment

---

## Current Day 2 Deliverables

The Friday dataset-anatomy work still to complete:

- Inspect dataset.csv and document what it represents.
- Inspect segments.csv and document what it represents.
- Identify labels.
- Identify train/test indicator.
- Identify fragment identifiers.
- Identify channel identifiers.
- Identify feature columns.
- Check data types.
- Check missing values.
- Check duplicates.
- Check class balance.
- Check fragment lengths.
- Check basic ranges.
- Create the required data dictionary.
- Plot several normal and anomalous telemetry fragments.
- Write the raw telemetry vs handcrafted-feature representation note.
- Complete the Friday learning topics.
- Complete the Friday Explain-It Check.

Saturday EDA tasks are NOT being pulled into Friday.

---

## Files Relevant to Current Work

Main notebook:
notebooks/01_dataset_inspection.ipynb

Dataset source folder:
Desktop/SAT/OPSSAT-AD

Important repository documentation:
docs/data_card.md
references/decision_log.md
docs/project_map.md

---

## Important Project Decisions

- OPSSAT-AD 2025 remains the primary research foundation.
- RESPOND is contextual ISTRAC/ISRO material, not the primary research paper.
- The core models remain the three agreed approaches.
- Explainability is limited to channel/signal-level evidence.
- No unsupported ISRO/ISTRAC affiliation claim.
- No physical root-cause claim.
- No unnecessary additional dataset or model.
- Do not skip fundamentals simply to catch up with the schedule.
- Preserve reproducibility and document important decisions.

---

## Current Next Step

Task 1:
Inspect dataset.csv and segments.csv and determine exactly what each file represents.

After every completed task:
1. Record what was completed.
2. Record important findings.
3. Record files changed.
4. Record important decisions.
5. Record the next task.
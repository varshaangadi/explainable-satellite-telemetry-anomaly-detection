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

Completed through: Task 2

Current task: Task 3 — Basic data-quality checks

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
- Task 1: documented what dataset.csv and segments.csv represent.
- Task 2: identified label/anomaly-related fields, train/test indicator,
  fragment identifiers, channel identifiers, raw telemetry fields and
  handcrafted feature fields.
- Unconfirmed label encodings, sampling semantics and telemetry units remain
  marked ⚠️ Needs verification.

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

## Current Day 2 Status

### Completed
- Task 0 — Workspace/environment verification.
- Task 1 — Documented what dataset.csv and segments.csv represent.
- Task 2 — Identified label/anomaly-related fields, train/test indicator,
  fragment identifiers, channel identifiers, raw telemetry fields and
  handcrafted feature fields.

### Remaining Today
- Check data types, missing values and duplicates.
- Check class balance.
- Check fragment lengths.
- Check basic value ranges.
- Create the data dictionary for fields that will actually be used.
- Plot several normal and anomalous telemetry fragments.
- Write the raw telemetry vs handcrafted-feature representation note.
- Complete the Friday learning topics.
- Complete the Friday Explain-It Check.

---

## Task 1 — Completed

- Documented what dataset.csv represents.
- Documented what segments.csv represents.
- Established the relationship between fragment identifiers across the two files.
- Distinguished the raw time-series telemetry representation from the
  fragment-level handcrafted-feature representation.

Files changed:
- notebooks/01_dataset_inspection.ipynb

---

## Task 2 — Completed

- Identified label/anomaly-related fields.
- Identified the train/test indicator.
- Identified fragment/segment identifiers.
- Identified channel identifiers.
- Identified raw telemetry fields.
- Identified the 18 documented handcrafted features in dataset.csv.
- Distinguished metadata/identifiers from candidate predictive features.
- Unconfirmed label encodings, sampling semantics and telemetry units remain
  marked ⚠️ Needs verification.

Files changed:
- notebooks/01_dataset_inspection.ipynb
- docs/project_context.md

---

## Current Next Step

Task 3:
Check data types, missing values, duplicates, class balance,
fragment lengths and basic ranges.

---

## Context Maintenance

After every completed task:
1. Record what was completed.
2. Record important findings.
3. Record files changed.
4. Record important decisions.
5. Record the next task.

### Task 3 — Completed

- Checked data types for dataset.csv and segments.csv.
- dataset.csv contains 13 integer, 9 floating-point and 1 string column.
- segments.csv contains 4 integer, 1 floating-point and 3 string columns.
- No explicit missing values were found in either CSV.
- No exact duplicate rows were found in either CSV.
- dataset.csv contains 434 anomaly=1 fragments (20.44%) and 1,689 anomaly=0 fragments (79.56%).
- segments.csv contains 100,264 anomaly=1 samples (33.04%) and 203,229 anomaly=0 samples (66.96%).
- The differing anomaly proportions are reported at different granularities: fragment level in dataset.csv and raw-sample level in segments.csv.
- segments.csv fragment lengths range from 8 to 1,040 samples, with mean 142.95 and median 70 samples.
- The dataset.csv len field matches the observed number of samples in segments.csv for all 2,123 fragments.
- All dataset.csv segments have corresponding raw telemetry, and all raw segments have corresponding dataset.csv records.
- Observed raw telemetry values in segments.csv range from -0.000101 to 1.5708.
- Basic numerical ranges for dataset.csv fields were checked.
- The exact semantic relationship between label and anomaly remains ⚠️ Needs verification.

Files changed:
- notebooks/01_dataset_inspection.ipynb
- docs/project_context.md

Next task:
Task 4 — Create the data dictionary for fields that will actually be used.
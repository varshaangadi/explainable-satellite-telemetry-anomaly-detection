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

Current stage: Initial data-preparation decisions frozen after Saturday EDA

Completed through: Saturday Task 5

Current task: Next task to be confirmed from the project plan

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

### Task 4 — Completed

- Created the project data dictionary for the relevant fields in dataset.csv and segments.csv.
- Documented field roles, observed data types, descriptions and project use.
- Explicitly documented the 18 handcrafted features in dataset.csv.
- Distinguished raw telemetry, identifiers, metadata, labels and split information.
- Unresolved semantic details remain marked ⚠️ Needs verification.
- The data dictionary documents current field roles but does not define the final model feature-selection or preprocessing decisions.

Files changed:
- docs/data_dictionary.md
- docs/project_context.md

Next task:
Task 5 — Plot several normal and anomalous telemetry fragments.

### Task 5 — Completed

- Plotted several representative telemetry fragments from the observed anomaly=0 and anomaly=1 categories.
- Plots use the sample-level telemetry representation in segments.csv.
- Fragments are grouped by segment and ordered by timestamp before plotting.
- Telemetry value is plotted against the ordered time/sample sequence.
- Visual inspection was used for dataset understanding only and not for physical root-cause diagnosis.
- Any unresolved anomaly-encoding semantics remain marked ⚠️ Needs verification.

Files changed:
- notebooks/01_dataset_inspection.ipynb
- docs/project_context.md

Next task:
[Update this after we confirm the remaining Friday task order.]

### Task 6 — Completed

- Added the required note distinguishing the sample-level temporal representation in segments.csv from the fragment-level handcrafted-feature representation in dataset.csv.
- Documented that segments.csv preserves the ordered telemetry samples, while dataset.csv provides derived fragment-level numerical characteristics.
- The distinction is documented without making final model-input or preprocessing decisions.

Files changed:
- notebooks/01_dataset_inspection.ipynb
- docs/project_context.md

Next:
Complete the Friday learning topics and the Explain-It Check.

## Saturday 10 Oct - Task 1: Channel Behaviour EDA

- Completed channel-level EDA for the nine observed telemetry channels using the existing OPSSAT-AD `segments.csv` data.
- No missing timestamps or telemetry values were observed within any channel, consistent with Friday's full-table check.
- Observed channel ranges vary; the overall observed range is -0.000101 to 1.5708. No telemetry units or spacecraft operating limits are inferred.
- Observed `sampling` field values are 1 and 5. Timestamp-derived median intervals within fragments vary by channel; the field's exact semantics remain marked ⚠️ Needs verification.
- Fragment lengths and value distributions vary by channel and recorded anomaly category; these comparisons are descriptive and do not establish physical faults or root causes.
- Added channel summary tables and two Matplotlib figures to the existing notebook. No raw CSV was modified.

Files changed:
- notebooks/01_dataset_inspection.ipynb
- docs/project_context.md

Next: Confirm the next Saturday task from the project plan.

### Saturday Task 2 — Completed

- Compared raw sample-level telemetry from segments.csv with the corresponding fragment-level fields in dataset.csv.
- Recomputed fragment length, mean, variance and standard deviation from the raw telemetry.
- Fragment length and mean matched up to floating-point precision.
- Initial variance and standard-deviation differences were caused by using the default sample-statistics convention (`ddof=1`).
- Recomputed variance and standard deviation using `ddof=0`; maximum absolute differences were effectively zero.
- The supplied len, mean, var and std fields are therefore consistent with the raw telemetry when the same statistical convention is used.
- Specialized handcrafted features were not reverse-engineered without needing their exact definitions.
- No final model representation, preprocessing or feature-selection decision was made.

Key findings:
- Raw `len`, `mean`, `var` and `std` are consistent with the corresponding fields in dataset.csv.
- The supplied variance and standard deviation use a convention consistent with `ddof=0`.
- The handcrafted representation is consistent for these statistics but does not preserve the complete temporal sequence.

Files changed:
- notebooks/01_dataset_inspection.ipynb
- docs/project_context.md

Next task:
Task 3 — Identify at least three data-quality challenges and document how each will be handled.

### Saturday 10 Oct — Task 3: Data-Quality Challenges

Completed identification and documentation of four data-quality/pipeline
challenges from the existing OPSSAT-AD EDA:

1. Unequal fragment lengths: 8–1,040 samples per fragment; median 70.
2. Class imbalance: 434/2,123 dataset fragments (20.44%) are anomaly-labelled.
3. Sampling/timestamp variability: observed sampling values are 1 and 5;
   timestamp-derived intervals are not uniformly regular.
4. Channel scale/range differences: observed channel value ranges differ
   substantially.

Documented observed evidence, why each issue matters, likely pipeline impact,
and proposed handling in `notebooks/01_dataset_inspection.ipynb`.

No data transformations, model training, new datasets, or final preprocessing
decisions were introduced. Uncertain semantics remain marked
⚠️ Needs verification.

Next task: Saturday 10 Oct — Task 4.
### Saturday 10 Oct — Task 4: Initial Report Figures

Completed the initial report figures required for the EDA stage.

Figures added/reused in `notebooks/01_dataset_inspection.ipynb`:
1. Representative normal telemetry fragment.
2. Representative anomalous telemetry fragment.
3. Fragment counts by observed anomaly category.
4. Basic data-quality checks for `dataset.csv` and `segments.csv`, showing explicit missing values and exact duplicate rows.
5. Fragment-level relationship between mean and standard deviation.

The figures are descriptive and intended for the initial project report. They support understanding of class distribution, basic data quality, representative telemetry behaviour, and relationships among handcrafted features.

No physical spacecraft fault, root cause, or causal relationship is inferred from these figures. The observed `anomaly` categories are treated as recorded dataset categories.

No raw CSV files were modified, and no model training or new preprocessing decisions were introduced.

Next task: Saturday 10 Oct — Task 5: Freeze initial data-preparation decisions in the README/research log.

### Saturday 10 Oct — Task 5: Initial Data-Preparation Decisions

- Recorded initial preparation decisions supported by the completed EDA in the README, decision log, and this context file.
- Preserve the raw source files and published train/test membership; retain fragment boundaries, timestamps, and channel identity during future analysis.
- Keep fragment-level `dataset.csv` features distinct from sample-level temporal `segments.csv`. The supplied `len`, `mean`, `var`, and `std` agree with raw samples when variance uses `ddof=0`; this does not establish that the temporal sequence is dispensable.
- Report anomaly-category balance with its counting unit and include per-class evaluation; observed fragment- and sample-level proportions differ.
- EDA describes unequal fragment lengths, timestamp interval variation, and differing channel ranges. It does not choose the model representation, length/window strategy, resampling or gap policy, scaling, feature selection, or training/threshold handling; these remain deferred.
- Exact `label`/`anomaly` relationship and encoding, `sampling` meaning, timestamp conventions, and physical units/limits remain ⚠️ Needs verification. Observed value ranges are not physical limits, and category plots do not establish fault causes.
- No models were trained, no data was transformed, and no raw CSV was modified.

Files changed:
- README.md
- references/decision_log.md
- docs/project_context.md

Next task: Confirm from the project plan.

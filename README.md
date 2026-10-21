# Explainable Satellite Telemetry Anomaly Detection

## Research question

How can anomaly-detection approaches identify unusual patterns in satellite telemetry from the OPSSAT-AD dataset, and what channel-level evidence can be presented to explain those detections?

## Dataset

The primary dataset is **OPSSAT-AD 2025**, using the public Zenodo v2 release (DOI: 10.5281/zenodo.15108715). The local EDA inspected `dataset.csv` (2,123 fragment rows, 23 columns) and `segments.csv` (303,493 sample rows, 8 columns), covering nine observed telemetry channels. The raw files remain outside this repository. See [the data card](docs/data_card.md) and [OPSSAT-AD research notes](references/OPSSAT_AD_notes.md).

## Three parallel approaches

The project plans to compare three independent approaches:

1. Statistical / threshold-based baseline
2. Isolation Forest
3. LSTM Autoencoder

These are **three parallel approaches**, to be evaluated and compared under a consistent protocol. They are not sequential models or stages in a model cascade.

## Context and scope

Public ISTRAC/ISRO material is research inspiration only. This is an independent project, with no ISRO or ISTRAC affiliation.

The project makes no claim of ISRO/ISTRAC affiliation, access to confidential ISRO telemetry, verified onboard deployment, verified real-time operational deployment, or verified physical root-cause diagnosis. Explanations will be framed as evidence at the telemetry-channel level, not as confirmed physical causes.

## Current status

Initial dataset inspection and Saturday EDA are complete. The EDA found no explicit missing values or exact duplicate rows in either inspected file. `dataset.csv` records 434/2,123 (20.44%) fragments as `anomaly=1`; in `segments.csv`, 100,264/303,493 (33.04%) samples are in that recorded category. These are different counting units. Fragment lengths are 8–1,040 samples (median 70), and the `len`, `mean`, `var`, and `std` fields agree with raw samples when variance uses `ddof=0`. Channel ranges and timestamp intervals vary. These observations are descriptive and do not establish physical limits or causes. Label semantics, `sampling` meaning, timestamp conventions, and telemetry units remain ⚠️ Needs verification.

## Initial data-preparation decisions

- Preserve the source files unchanged and retain the fragment boundary and timestamp information during future work.
- Keep the published train/test split; do not relabel or resplit based on the observed categories.
- Treat `dataset.csv` as fragment-level handcrafted features and `segments.csv` as sample-level temporal telemetry. Their shared fragment statistics do not make the temporal representation redundant.
- Report class balance with its unit (fragment or sample) and evaluate per class; the two file-level proportions are not interchangeable.
- Keep channel identity available in analysis and document any future comparison across channels.
- The EDA does not select a model input representation or determine length handling, resampling/gap policy, scaling, feature selection, or threshold/training strategy. Those choices are deferred until the relevant modeling/evaluation stage.
- The meanings of `label` versus `anomaly`, observed `anomaly` encodings, `sampling`, timestamp conventions, and telemetry units ⚠️ Needs verification.

## Planned pipeline

Verify the OPSSAT-AD source and documentation; inspect the data through exploratory data analysis (EDA); preserve the published train/test separation; document and apply preprocessing; develop and compare the three parallel approaches; produce anomaly scores and a documented decision rule; associate detections with channel-level evidence; and, later, present results in a dashboard. Details and learning milestones are in [the project map](docs/project_map.md).

## Repository layout

- `data/`: raw and processed data locations; data is not currently included.
- `notebooks/`: exploratory and analysis notebooks.
- `src/`: future project code, organized by responsibility.
- `models/`: location reserved for model artifacts.
- `figures/`: location reserved for generated figures.
- `dashboard/`: location reserved for a future dashboard.
- `report/`: location reserved for the project report.
- `references/`: research notes and project decision log.
- `docs/`: project map and data card template.

## Research and data integrity

Do not infer dataset contents, statistics, labels, filenames, licence terms, or research results. Record these only after checking authoritative source material. Verify the dataset licence before any public upload. See [the decision log](references/decision_log.md).

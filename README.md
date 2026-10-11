# Explainable Satellite Telemetry Anomaly Detection

## Research question

How can anomaly-detection approaches identify unusual patterns in satellite telemetry from the OPSSAT-AD dataset, and what channel-level evidence can be presented to explain those detections?

## Dataset

The planned primary dataset is **OPSSAT-AD**. Its exact version, files, labels, channels, split, representation, licence, and attribution have not yet been verified. See [the data card template](docs/data_card.md) and [OPSSAT-AD research notes](references/OPSSAT_AD_notes.md). No dataset is included in this repository at this stage.

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

**Week 1: orientation and repository setup.** The work is currently limited to organizing the repository and planning dataset and literature verification. No models or dashboard have been implemented, and no dataset has been added.

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

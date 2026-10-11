# Project map

## High-level pipeline

1. **OPSSAT-AD source and documentation** — verify provenance, version, exact files, labels, channels, representation, published split, licence, and attribution before use.
2. **EDA** — inspect the verified files and document data quality, distributions, channel behavior, labels, and split characteristics without assuming undocumented properties.
3. **Published train/test separation** — preserve the dataset's published separation. Fit data-dependent preprocessing and models using training data only; do not use test data to tune decisions.
4. **Preprocessing** — document and implement transformations appropriate to the verified data and each approach, with any fitted parameters learned from training data.
5. **Three parallel approaches** — evaluate a statistical / threshold-based baseline, Isolation Forest, and LSTM Autoencoder as independent alternatives, not a sequential chain.
6. **Anomaly scoring and decision** — define how each approach yields scores and how a decision threshold or rule is selected using an explicitly documented protocol.
7. **Channel-level evidence** — provide evidence tied to telemetry channels and observed values or features. Do not present this as confirmed physical root-cause diagnosis.
8. **Dashboard** — later, present data context, approach outputs, anomaly decisions, and channel-level evidence. Dashboard implementation is not part of Week 1 setup.

## Learning plan: Weeks 1–5

The week labels below are a learning plan, not claims that implementation has happened.

- **Week 1 — Orientation and repository setup:** clarify the research question, organize the repository, begin source and literature verification, and record decisions.
- **Week 2 — Dataset understanding and EDA:** verify the data card and published split; inspect the dataset and document findings.
- **Week 3 — Preprocessing and statistical baseline:** learn the preprocessing needed by the verified data and establish a simple threshold-based reference.
- **Week 4 — Isolation Forest and evaluation:** learn the method and anomaly-evaluation concepts; compare results under a consistent, split-respecting protocol.
- **Week 5 — LSTM Autoencoder and explanation evidence:** learn sequence-modeling and reconstruction concepts, evaluate the approach, and develop channel-level evidence for comparison.

## Optional Transformer

A Transformer is optional exploratory work only. It must not delay completion or evaluation of the three core approaches, or the core project deliverables. No Transformer is currently implemented or planned as a required approach.

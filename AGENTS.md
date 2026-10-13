# SAT Project — Codex Instructions

## Project
Explainable AI-Based Satellite Telemetry Anomaly Detection and Spacecraft Health Monitoring

## Research Question
Can classical ML and temporal deep-learning models detect anomalous behaviour
in real spacecraft telemetry, while producing interpretable channel-level
evidence for the detected anomaly?

## Primary Research Foundation
- OPSSAT-AD 2025 is the primary research dataset and benchmark.
- Use the authoritative public OPSSAT-AD release.
- Do not silently replace OPSSAT-AD with another dataset.

## ISTRAC / ISRO Context
- RESPOND material is used as contextual motivation for the project.
- Do not present RESPOND as the primary research paper.
- Do not claim ISRO or ISTRAC affiliation.
- Do not claim access to confidential ISRO/ISTRAC telemetry.
- Do not claim verified onboard deployment or operational real-time use.

## Core Approaches
Use these three core approaches:
1. Statistical / threshold-based baseline
2. Isolation Forest
3. LSTM Autoencoder

These are parallel approaches, not sequential stages of one model pipeline.

## Optional Advanced Work
- Transformer-based approaches are optional.
- They must only be considered after the core system is stable.
- An optional advanced model must never delay the core deliverables.

## Explainability Scope
- Explainability means channel/signal-level evidence associated with detected anomalies.
- Do not claim that channel-level evidence proves the physical root cause.
- Physical root-cause diagnosis is outside the core scope.

## Dataset Rules
- OPSSAT-AD is the primary dataset.
- Preserve the published benchmark representation and split where appropriate.
- Do not modify the raw source dataset.
- Keep raw dataset files outside the public GitHub repository unless explicitly required.
- Preserve dataset attribution and license requirements.

## Reproducibility
- Prefer clear, reproducible Python workflows.
- Record important preprocessing, modelling, evaluation and dataset decisions.
- Do not silently change previously agreed project decisions.

## Scope Control
- Do not add new major datasets or models without a clear project reason.
- Do not pull future-day tasks forward unnecessarily.
- Do not replace planned fundamentals with more sophisticated methods simply because newer methods exist.
- Keep the implementation aligned with the approved project plan.

## Project Context
For current progress and completed work, consult:
docs/project_context.md

Do not assume current progress from memory when the project context file is available.

## Important Safety Rule for Research Claims
Do not turn assumptions, examples, or possibilities into factual claims.
When evidence is insufficient, explicitly mark:
"⚠️ Needs verification"
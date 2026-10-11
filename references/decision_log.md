# Research Decision Log

This log records important project decisions, why they were made, and the evidence supporting them.

| Decision | Reason | Evidence / source |
|---|---|---|
| Use OPSSAT-AD as the primary dataset | It provides publicly available real satellite telemetry from ESA's OPS-SAT together with anomaly annotations and a published benchmark procedure. | OPSSAT-AD 2025 Scientific Data paper; Zenodo v2 |
| Use Zenodo v2 as the dataset source | It is the current public dataset record selected for this implementation and contains the required dataset files and licence. | Zenodo OPSSAT-AD v2, DOI 10.5281/zenodo.15108715 |
| Keep the published train/test split | The benchmark defines a published training/test separation, making model comparisons more reproducible and preventing arbitrary resplitting. | OPSSAT-AD 2025 Benchmarking Procedure |
| Use a statistical / threshold-based detector as the first baseline | A simple, transparent reference is needed before comparing more complex approaches. | Project plan |
| Use Isolation Forest as the classical ML approach | It provides a classical unsupervised anomaly-detection comparison within the agreed project scope. | Project plan |
| Use an LSTM Autoencoder as the deep-learning approach | The project requires a temporal deep-learning model capable of learning normal temporal behaviour through reconstruction. | Project plan |
| Treat the three approaches as parallel alternatives | The project compares the approaches on the same anomaly-detection task; one model is not used as the input to the next. | Project plan / research design |
| Do not add a Transformer at this stage | The Transformer is explicitly optional and must not delay the stable core pipeline. | Project plan |
| Use OPSSAT-AD raw telemetry and handcrafted-feature representations carefully | The dataset provides both forms, and the project must decide the main model representation based on evidence rather than adding features only to improve scores. | OPSSAT-AD 2025 paper; project plan |
| Respect the published benchmark representation during comparison | Changing the representation or preprocessing without documenting it would make comparisons less defensible. | OPSSAT-AD Benchmarking Procedure; project plan |
| Define explainability as channel/signal-level evidence | The project can identify evidence associated with an anomaly, but this does not establish a verified physical root cause. | Project plan |
| Do not claim physical root-cause diagnosis | Correlation or channel attribution is not equivalent to causal proof of a spacecraft fault. | Project plan |
| Treat the project as an independent implementation | The project uses public ESA telemetry and is inspired by ISTRAC-relevant research, but it is not an ISRO/ISTRAC project. | Project plan; ISRO RESPOND 2024 research context |
| Use RESPOND 2024 as ISTRAC/ISRO context rather than the primary dataset source | The official ISTRAC research proposal establishes relevance to spacecraft-health monitoring and resource-constrained onboard AI, while OPSSAT-AD is the actual dataset used here. | ISRO RESPOND Basket 2024; OPSSAT-AD 2025 |
| Keep the raw OPSSAT-AD dataset outside the public GitHub repository by default | The dataset can be obtained directly from its authoritative Zenodo source, so duplicating the raw files in the repository is unnecessary for reproducibility at this stage. | Zenodo v2; project repository design |
| Preserve the dataset licence and attribution information | The downloaded licence is MIT and requires the copyright and permission notice to be retained in copies or substantial portions. | OPSSAT-AD `LICENSE` file |
| Use Python 3.12 for the project environment | A single project-specific environment is needed for reproducibility across Pandas, NumPy, scikit-learn, Jupyter and later project dependencies. | Project environment setup |# Research Decision Log

This log records important project decisions, why they were made, and the evidence supporting them.

| Decision | Reason | Evidence / source |
|---|---|---|
| Use OPSSAT-AD as the primary dataset | It provides publicly available real satellite telemetry from ESA's OPS-SAT together with anomaly annotations and a published benchmark procedure. | OPSSAT-AD 2025 Scientific Data paper; Zenodo v2 |
| Use Zenodo v2 as the dataset source | It is the current public dataset record selected for this implementation and contains the required dataset files and licence. | Zenodo OPSSAT-AD v2, DOI 10.5281/zenodo.15108715 |
| Keep the published train/test split | The benchmark defines a published training/test separation, making model comparisons more reproducible and preventing arbitrary resplitting. | OPSSAT-AD 2025 Benchmarking Procedure |
| Use a statistical / threshold-based detector as the first baseline | A simple, transparent reference is needed before comparing more complex approaches. | Project plan |
| Use Isolation Forest as the classical ML approach | It provides a classical unsupervised anomaly-detection comparison within the agreed project scope. | Project plan |
| Use an LSTM Autoencoder as the deep-learning approach | The project requires a temporal deep-learning model capable of learning normal temporal behaviour through reconstruction. | Project plan |
| Treat the three approaches as parallel alternatives | The project compares the approaches on the same anomaly-detection task; one model is not used as the input to the next. | Project plan / research design |
| Do not add a Transformer at this stage | The Transformer is explicitly optional and must not delay the stable core pipeline. | Project plan |
| Use OPSSAT-AD raw telemetry and handcrafted-feature representations carefully | The dataset provides both forms, and the project must decide the main model representation based on evidence rather than adding features only to improve scores. | OPSSAT-AD 2025 paper; project plan |
| Respect the published benchmark representation during comparison | Changing the representation or preprocessing without documenting it would make comparisons less defensible. | OPSSAT-AD Benchmarking Procedure; project plan |
| Define explainability as channel/signal-level evidence | The project can identify evidence associated with an anomaly, but this does not establish a verified physical root cause. | Project plan |
| Do not claim physical root-cause diagnosis | Correlation or channel attribution is not equivalent to causal proof of a spacecraft fault. | Project plan |
| Treat the project as an independent implementation | The project uses public ESA telemetry and is inspired by ISTRAC-relevant research, but it is not an ISRO/ISTRAC project. | Project plan; ISRO RESPOND 2024 research context |
| Use RESPOND 2024 as ISTRAC/ISRO context rather than the primary dataset source | The official ISTRAC research proposal establishes relevance to spacecraft-health monitoring and resource-constrained onboard AI, while OPSSAT-AD is the actual dataset used here. | ISRO RESPOND Basket 2024; OPSSAT-AD 2025 |
| Keep the raw OPSSAT-AD dataset outside the public GitHub repository by default | The dataset can be obtained directly from its authoritative Zenodo source, so duplicating the raw files in the repository is unnecessary for reproducibility at this stage. | Zenodo v2; project repository design |
| Preserve the dataset licence and attribution information | The downloaded licence is MIT and requires the copyright and permission notice to be retained in copies or substantial portions. | OPSSAT-AD `LICENSE` file |
| Use Python 3.12 for the project environment | A single project-specific environment is needed for reproducibility across Pandas, NumPy, scikit-learn, Jupyter and later project dependencies. | Project environment setup |
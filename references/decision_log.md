# Initial project decision log

| Decision | Reason | Evidence/source |
|---|---|---|
| Use OPSSAT-AD as the primary dataset | Keep the project centered on the stated satellite telemetry anomaly-detection benchmark; verify its details before use. | Project scope; authoritative dataset source and documentation **Needs verification**. |
| Respect the published train/test split | Preserve the benchmark protocol and avoid information leakage. | Published dataset/benchmark procedure **Needs verification**. |
| Include a statistical / threshold-based baseline | Establish an interpretable reference point for comparison. | Initial project design; evaluation protocol to be documented. |
| Include Isolation Forest | Compare a non-sequential anomaly-detection approach alongside the baseline and sequence model. | Initial project design; method and evaluation details to be documented. |
| Include an LSTM Autoencoder | Compare a sequence reconstruction approach as a separate core approach. | Initial project design; method and evaluation details to be documented. |
| Compare the three approaches in parallel | Make results comparable without treating one model's output as another model's input. | Initial project design. |
| Keep a Transformer optional only | Protect the scope and schedule for the three core approaches. | Initial project design. |
| Report channel-level evidence rather than physical root cause | Telemetry evidence alone does not establish a verified physical diagnosis. | Project scope and non-claims; evidence protocol to be documented. |
| Describe this as an independent project with no ISRO affiliation | Avoid implying institutional affiliation or authorization. | Project scope. |
| Verify the dataset licence before public upload | Confirm the permitted use and redistribution terms before sharing data. | Dataset licence and source terms **Needs verification**. |

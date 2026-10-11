# Dataset data card (template)

Complete this card only after checking authoritative dataset documentation. Unverified fields are marked **Needs verification**. Do not infer missing details.

| Field | Record |
|---|---|
| Dataset name | OPSSAT-AD (planned primary dataset; details Needs verification) |
| Source | Needs verification |
| Provenance | Needs verification |
| Version | Needs verification |
| Exact files | Needs verification |
| Labels | Needs verification |
| Channels | Needs verification |
| Train/test split | Needs verification |
| Representation (raw telemetry, derived features, or both) | Needs verification |
| Licence | Needs verification |
| Attribution requirements | Needs verification |
| Limitations | Needs verification |

## Verification record

- Documentation consulted: Needs verification
- Date checked: Needs verification
- Notes / unresolved questions: Needs verification
-------------------------------------------------------------
# OPSSAT-AD Data Card

## Dataset name

OPSSAT-AD — OPS-SAT anomaly detection dataset for satellite telemetry.

## Primary source

Zenodo, version v2:

https://zenodo.org/records/15108715

DOI:

https://doi.org/10.5281/zenodo.15108715

## Primary research paper

Ruszczak, B., Kotowski, K., Evans, D., et al. (2025).

"The OPS-SAT benchmark for detecting anomalies in satellite telemetry."

Scientific Data, 12, 710.

https://doi.org/10.1038/s41597-025-05035-3

The paper is the primary research foundation for the dataset and benchmark. It describes the dataset, annotation process, published train/test split, benchmarking procedure and recommended evaluation metrics.

## Provenance

OPSSAT-AD contains telemetry acquired onboard ESA's OPS-SAT CubeSat mission.

The dataset was curated using telemetry selected from the OPS-SAT archive and annotated collaboratively. The paper states that the initial anomaly selection involved three ESA spacecraft operations engineers and was further curated by two machine-learning experts.

The dataset is publicly distributed through Zenodo and does not require access to the restricted ESA WebMUST platform.

## Dataset version

Version: v2

Zenodo record:
https://zenodo.org/records/15108715

## Files in the downloaded v2 package

Verified in the local downloaded package:

- `dataset.csv`
- `segments.csv`
- `LICENSE`
- `dataset_generator.ipynb`
- `modeling_examples.ipynb`
- `requirements.txt`

## Local readability verification

The downloaded CSV files were successfully loaded with Pandas in:

`notebooks/01_dataset_inspection.ipynb`

Verified local shapes:

- `dataset.csv`: 2,123 rows × 23 columns
- `segments.csv`: 303,493 rows × 8 columns

Both files loaded successfully and their columns, data types and missing-value counts were inspected.

No changes were made to the source CSV files.

## Dataset representations

The dataset is provided in two main forms:

1. Raw telemetry segments in `segments.csv`.
2. A tabular representation in `dataset.csv` containing extracted handcrafted features for the labelled telemetry segments.

The paper states that 18 handcrafted features are provided for each telemetry fragment.

## Telemetry channels

The paper identifies 9 source telemetry channels:

### Magnetometer channels

- `I_B_FB_MM_0` (CADC0872)
- `I_B_FB_MM_1` (CADC0873)
- `I_B_FB_MM_2` (CADC0874)

### Photo-diode channels

- `I_PD1_THETA` (CADC0884)
- `I_PD2_THETA` (CADC0886)
- `I_PD3_THETA` (CADC0888)
- `I_PD4_THETA` (CADC0890)
- `I_PD5_THETA` (CADC0892)
- `I_PD6_THETA` (CADC0894)

## Labels

The dataset contains anomaly annotations for the telemetry fragments.

Verified file fields include:

### `dataset.csv`

- `anomaly`
- `train`

### `segments.csv`

- `label`
- `anomaly`
- `train`

The exact semantic distinction between every label-related field will be documented further during the dataset-anatomy/EDA stage rather than inferred prematurely.

## Train / test split

The published benchmark contains:

- 1,494 training telemetry segments
- 529 test telemetry segments

The benchmark split is encoded through the `train` attribute and must be respected for reproducible evaluation.

The paper states that the split was created using stratified random sampling to preserve the original anomaly proportion in the training and test sets.

## Data quality characteristics

The paper identifies several real-world telemetry characteristics, including:

- data gaps
- signal artifacts
- changes in sampling frequency
- variations in signal amplitude
- different fragment lengths

Detailed EDA and data-quality analysis are scheduled separately in the project plan.

## Licence

The downloaded `LICENSE` file specifies the:

**MIT License for OPS-SAT Dataset**

Copyright:

**(c) 2024 KP Labs**

The licence permits use, copying, modification, publication, distribution, sublicensing and sale, subject to the conditions of the MIT License.

The copyright notice and permission notice must be included in copies or substantial portions of the dataset.

Source licence file:

https://zenodo.org/records/15108715/files/LICENSE

## Attribution

Recommended dataset attribution:

Ruszczak, B., Kotowski, K., Evans, D., Nalepa, J., et al. (2025).
"The OPS-SAT benchmark for detecting anomalies in satellite telemetry."
Scientific Data, 12, 710.
https://doi.org/10.1038/s41597-025-05035-3

Dataset:

OPSSAT-AD, Zenodo v2.
https://doi.org/10.5281/zenodo.15108715

When redistributing the dataset or substantial portions of it, retain the MIT licence copyright and permission notice.

## Repository handling

The raw OPSSAT-AD files are currently kept outside the public GitHub repository.

The GitHub repository documents the dataset source and reproducibility procedure rather than duplicating the raw dataset files.

## Known limitations

The dataset has several limitations relevant to this project:

- It contains short single-channel telemetry fragments rather than complete multivariate spacecraft telemetry.
- The dataset is based on one CubeSat mission.
- Telemetry fragments vary in length and sampling frequency.
- The dataset contains real-world data gaps and signal artefacts.
- Dataset annotations represent labelled anomalous/nominal telemetry behaviour; they should not be interpreted automatically as verified physical spacecraft fault root causes.

These limitations will be discussed further during EDA and final evaluation.

## Verification status

Verified:

- Public Zenodo source
- Dataset version
- Downloaded file names
- CSV readability
- Local CSV shapes
- Column names
- Data types
- Missing-value checks
- Nine telemetry channels from the published paper
- Published train/test split
- MIT licence

To be further examined during later EDA:

- detailed class balance
- fragment-length distribution
- signal ranges and distributions
- sampling characteristics
- anomaly-pattern differences
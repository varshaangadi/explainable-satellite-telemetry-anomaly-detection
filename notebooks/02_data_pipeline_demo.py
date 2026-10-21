"""Small runnable demonstration of the reusable OPSSAT-AD data pipeline.

Run from the repository root with the project environment:
    python notebooks/02_data_pipeline_demo.py

The source CSVs remain outside the repository. Override OPSSAT_AD_DATA_DIR if
they are stored elsewhere. The observed train flag mapping needs verification
against authoritative split documentation.
"""

import os
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from src.data.opssat_pipeline import label_counts, load_opssat_data  # noqa: E402


data_dir = Path(os.environ.get(
    "OPSSAT_AD_DATA_DIR",
    str(Path.home() / "Desktop" / "SAT" / "OPSSAT-AD"),
))
data = load_opssat_data(data_dir)

print(f"Data directory: {data_dir}")
print(f"Train fragment shape: {data.train.fragments.shape}")
print(f"Train sample shape: {data.train.samples.shape}")
print(f"Test fragment shape: {data.test.fragments.shape}")
print(f"Test sample shape: {data.test.samples.shape}")
print("Recorded anomaly counts by split and granularity:")
for split_name, counts in label_counts(data).items():
    print(f"  {split_name}: fragments={counts['fragments']}, samples={counts['samples']}")

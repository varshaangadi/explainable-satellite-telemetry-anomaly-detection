"""Load and validate the published OPSSAT-AD fragment and sample tables.

This module separates the supplied benchmark split without fitting or applying
any learned preprocessing. Sequence representation choices are intentionally
left to later project work.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


DATASET_COLUMNS = (
    "segment", "anomaly", "train", "channel", "sampling", "duration", "len",
    "mean", "var", "std", "kurtosis", "skew", "n_peaks",
    "smooth10_n_peaks", "smooth20_n_peaks", "diff_peaks", "diff2_peaks",
    "diff_var", "diff2_var", "gaps_squared", "len_weighted",
    "var_div_duration", "var_div_len",
)
SEGMENTS_COLUMNS = (
    "channel", "timestamp", "value", "label", "sampling", "anomaly",
    "segment", "train",
)
EXPECTED_SHAPES = {"dataset.csv": (2123, 23), "segments.csv": (303493, 8)}


@dataclass(frozen=True)
class DataSplit:
    """Fragment-level and sample-level rows for one published split."""

    fragments: pd.DataFrame
    samples: pd.DataFrame


@dataclass(frozen=True)
class OpssatData:
    """Validated OPSSAT-AD tables separated by the published train flag."""

    train: DataSplit
    test: DataSplit


def _read_and_validate(path: Path, filename: str, expected_columns: tuple[str, ...]) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"Required OPSSAT-AD file not found: {path}")
    frame = pd.read_csv(path)
    expected_shape = EXPECTED_SHAPES[filename]
    if frame.shape != expected_shape:
        raise ValueError(f"{filename} has shape {frame.shape}; expected {expected_shape}.")
    actual_columns = tuple(frame.columns)
    unexpected = sorted(set(actual_columns) - set(expected_columns))
    missing_columns = sorted(set(expected_columns) - set(actual_columns))
    if unexpected or missing_columns:
        raise ValueError(
            f"{filename} schema mismatch; unexpected columns={unexpected}, "
            f"missing columns={missing_columns}."
        )
    if actual_columns != expected_columns:
        raise ValueError(f"{filename} columns are not in the expected published order.")
    missing = frame.isna().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        raise ValueError(f"{filename} contains missing values: {missing.to_dict()}")
    return frame


def _count_by(frame: pd.DataFrame, column: str) -> dict:
    return {key: int(value) for key, value in frame[column].value_counts(sort=True).items()}


def validate_opssat_frames(dataset: pd.DataFrame, segments: pd.DataFrame) -> None:
    """Validate schemas, labels, split membership, IDs, channels, and lengths."""
    for name, frame, columns, shape in (
        ("dataset.csv", dataset, DATASET_COLUMNS, EXPECTED_SHAPES["dataset.csv"]),
        ("segments.csv", segments, SEGMENTS_COLUMNS, EXPECTED_SHAPES["segments.csv"]),
    ):
        if frame.shape != shape:
            raise ValueError(f"{name} has shape {frame.shape}; expected {shape}.")
        if tuple(frame.columns) != columns:
            unexpected = sorted(set(frame.columns) - set(columns))
            missing_columns = sorted(set(columns) - set(frame.columns))
            raise ValueError(
                f"{name} schema mismatch; unexpected columns={unexpected}, "
                f"missing columns={missing_columns}."
            )
        if frame.isna().any().any():
            raise ValueError(f"{name} contains missing values.")

    for name, frame in (("dataset.csv", dataset), ("segments.csv", segments)):
        if not set(frame["anomaly"].unique()).issubset({0, 1}):
            raise ValueError(f"{name} has unexpected anomaly values: {_count_by(frame, 'anomaly')}")
        if not set(frame["train"].unique()).issubset({0, 1}):
            raise ValueError(f"{name} has unexpected train values: {_count_by(frame, 'train')}")

    if dataset["segment"].duplicated().any():
        raise ValueError("dataset.csv must contain exactly one row per fragment ID.")
    if segments["segment"].isna().any():
        raise ValueError("segments.csv contains a missing fragment ID.")

    fragment_meta = dataset.set_index("segment")[["channel", "anomaly", "train", "len"]]
    sample_meta = segments.groupby("segment", sort=False).agg(
        channel_count=("channel", "nunique"),
        channel=("channel", "first"),
        anomaly_count=("anomaly", "nunique"),
        anomaly=("anomaly", "first"),
        train_count=("train", "nunique"),
        train=("train", "first"),
        sample_count=("segment", "size"),
    )
    missing_raw = fragment_meta.index.difference(sample_meta.index)
    missing_fragment = sample_meta.index.difference(fragment_meta.index)
    if len(missing_raw) or len(missing_fragment):
        raise ValueError(
            f"Fragment IDs do not align: fragments without samples={len(missing_raw)}, "
            f"samples without fragment rows={len(missing_fragment)}."
        )
    aligned = fragment_meta.join(sample_meta, how="inner", rsuffix="_sample")
    consistent = (
        aligned["channel"].eq(aligned["channel_sample"])
        & aligned["anomaly"].eq(aligned["anomaly_sample"])
        & aligned["train"].eq(aligned["train_sample"])
        & aligned["len"].eq(aligned["sample_count"])
        & aligned["channel_count"].eq(1)
        & aligned["anomaly_count"].eq(1)
        & aligned["train_count"].eq(1)
    )
    if not consistent.all():
        raise ValueError(f"Fragment/sample metadata or length mismatches: {int((~consistent).sum())}.")

    if set(dataset["anomaly"].unique()) != {0, 1}:
        raise ValueError(f"Expected observed anomaly categories 0 and 1; got {_count_by(dataset, 'anomaly')}.")
    # This validates the observed encoding only; semantic meaning remains
    # ⚠️ Needs verification.
    observed_labels = set(segments["label"].unique())
    if observed_labels != {"anomaly"}:
        raise ValueError(f"Expected observed segments.csv label value 'anomaly'; got {sorted(observed_labels)}.")


def load_opssat_data(
    data_dir: str | Path,
    *,
    train_value: int = 1,
) -> OpssatData:
    """Load both public OPSSAT-AD tables and return clean published splits.

    The observed release uses ``train=1`` for the training portion and
    ``train=0`` for the test portion. That interpretation remains subject to
    verification against authoritative split documentation.
    """
    if train_value not in (0, 1):
        raise ValueError("train_value must be 0 or 1.")
    root = Path(data_dir)
    dataset = _read_and_validate(root / "dataset.csv", "dataset.csv", DATASET_COLUMNS)
    segments = _read_and_validate(root / "segments.csv", "segments.csv", SEGMENTS_COLUMNS)
    validate_opssat_frames(dataset, segments)

    # Split using the published indicator, then remove it from returned tables
    # so it cannot accidentally be treated as a downstream feature.
    train_fragments = dataset.loc[dataset["train"].eq(train_value)].drop(columns="train").copy().reset_index(drop=True)
    test_fragments = dataset.loc[dataset["train"].ne(train_value)].drop(columns="train").copy().reset_index(drop=True)
    train_segments = segments.loc[segments["train"].eq(train_value)].drop(columns="train").copy().reset_index(drop=True)
    test_segments = segments.loc[segments["train"].ne(train_value)].drop(columns="train").copy().reset_index(drop=True)
    result = OpssatData(
        train=DataSplit(train_fragments, train_segments),
        test=DataSplit(test_fragments, test_segments),
    )

    if set(result.train.fragments["segment"]) & set(result.test.fragments["segment"]):
        raise ValueError("Train/test fragment IDs overlap.")
    if set(result.train.samples["segment"]) & set(result.test.samples["segment"]):
        raise ValueError("Train/test sample fragment IDs overlap.")
    if len(result.train.fragments) + len(result.test.fragments) != len(dataset):
        raise ValueError("Train/test fragment rows do not partition the input table.")
    if len(result.train.samples) + len(result.test.samples) != len(segments):
        raise ValueError("Train/test sample rows do not partition the input table.")
    return result


def label_counts(data: OpssatData) -> dict[str, dict[str, dict]]:
    """Return recorded anomaly counts at fragment and sample granularity."""
    return {
        name: {
            "fragments": _count_by(split.fragments, "anomaly"),
            "samples": _count_by(split.samples, "anomaly"),
        }
        for name, split in (("train", data.train), ("test", data.test))
    }

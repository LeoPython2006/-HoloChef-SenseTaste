"""Utilities for working with NIR spectrometer data."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict


def scan_spectrum_csv(path: str | Path) -> Dict[str, float]:
    """Parse a CSV file representing a scanned spectrum.

    The expected format is a header row with compound names followed by a
    single row of numerical values.

    Args:
        path: Path to a CSV file with composition data.

    Returns:
        Mapping of compound names to concentration values in the range 0-1.
    """

    with open(path, newline="") as fh:
        reader = csv.DictReader(fh)
        row = next(reader)
        return {k: float(v) for k, v in row.items()}

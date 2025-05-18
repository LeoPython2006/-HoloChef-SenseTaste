"""Simple NIR spectrometer reader.

This module mimics interaction with a real NIR spectrometer by reading a
CSV file that contains a spectrum (wavelength, intensity).  The values are
then converted to an estimated chemical composition using a few heuristic
rules.  While this is not direct hardware integration, it demonstrates the
logic one might use when processing real spectral data.
"""

from pathlib import Path
from typing import Dict, Iterable
import csv


_DATA_FILE = Path(__file__).with_name("data") / "sample_spectrum.csv"


def _load_spectrum(path: Path) -> Dict[float, float]:
    """Load a spectrum CSV file.

    The file should contain two columns: ``wavelength`` and ``intensity``.
    ``wavelength`` is expected in nanometers.
    """
    spectrum: Dict[float, float] = {}
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            spectrum[float(row["wavelength"])] = float(row["intensity"])
    return spectrum


def _average_intensity(spectrum: Dict[float, float], wavelengths: Iterable[int]) -> float:
    values = [spectrum.get(float(w), 0.0) for w in wavelengths]
    return sum(values) / len(values)


def scan_ingredient(file_path: str | None = None) -> Dict[str, float]:
    """Scan an ingredient and estimate its chemical composition.

    If ``file_path`` is not provided, a bundled sample spectrum is used.
    """
    path = Path(file_path) if file_path else _DATA_FILE
    spectrum = _load_spectrum(path)

    # Derive crude composition estimates from spectral peaks.  These mappings
    # are illustrative; real models would rely on calibration data.
    water = _average_intensity(spectrum, range(960, 980, 10))
    sugar = _average_intensity(spectrum, (940,))
    fat = _average_intensity(spectrum, (930,))
    protein = _average_intensity(spectrum, (1000,))

    total = water + sugar + fat + protein
    if total == 0:
        total = 1.0

    return {
        "water": water / total,
        "sugar": sugar / total,
        "fat": fat / total,
        "protein": protein / total,
    }

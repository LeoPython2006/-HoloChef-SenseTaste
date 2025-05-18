"""Entry point for virtual tasting application."""

from __future__ import annotations

import argparse
from pathlib import Path

from .nir_scanner import scan_spectrum_csv
from .flavor_model import FlavorModel
from .ar_visualizer import visualize


DEFAULT_DATA_DIR = Path(__file__).parent / "data"


def run(spectrum: Path | None = None, training_data: Path | None = None) -> None:
    """Run a simple demo workflow."""

    spectrum_path = spectrum or DEFAULT_DATA_DIR / "sample_spectrum.csv"
    training_path = training_data or DEFAULT_DATA_DIR / "training_data.csv"

    composition = scan_spectrum_csv(spectrum_path)
    model = FlavorModel(training_path)
    flavor_info = model.predict(composition)
    visualize(flavor_info)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Virtual tasting demo")
    parser.add_argument(
        "--spectrum",
        type=Path,
        help="Path to spectrum CSV (defaults to sample data)",
    )
    parser.add_argument(
        "--training",
        type=Path,
        help="Path to training CSV (defaults to sample data)",
    )
    args = parser.parse_args()
    run(spectrum=args.spectrum, training_data=args.training)

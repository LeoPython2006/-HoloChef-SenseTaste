"""Entry point for virtual tasting application."""

from .nir_scanner import scan_ingredient
from .flavor_model import FlavorModel
from .ar_visualizer import visualize
import argparse


def run() -> None:
    """Run a simple demo workflow."""
    parser = argparse.ArgumentParser(description="Virtual tasting demo")
    parser.add_argument(
        "--spectrum",
        metavar="FILE",
        help="Path to spectrum CSV captured by an NIR spectrometer",
    )
    args = parser.parse_args()

    composition = scan_ingredient(args.spectrum)
    model = FlavorModel()
    flavor_info = model.predict(composition)
    visualize(flavor_info)


if __name__ == "__main__":
    run()

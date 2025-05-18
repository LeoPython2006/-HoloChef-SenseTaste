"""Entry point for virtual tasting application."""

from .nir_scanner import scan_ingredient
from .flavor_model import FlavorModel
from .ar_visualizer import visualize


def run() -> None:
    """Run a simple demo workflow."""
    composition = scan_ingredient()
    model = FlavorModel()
    flavor_info = model.predict(composition)
    visualize(flavor_info)


if __name__ == "__main__":
    run()

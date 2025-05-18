"""Stub for NIR spectrometer scanning."""

from typing import Dict


def scan_ingredient() -> Dict[str, float]:
    """Simulate scanning an ingredient and returning a chemical composition.

    Returns:
        Dict[str, float]: Mapping of compound names to concentration values.
    """
    # TODO: integrate with actual NIR spectrometer hardware
    return {
        "water": 0.7,
        "sugar": 0.1,
        "fat": 0.05,
        "protein": 0.15,
    }

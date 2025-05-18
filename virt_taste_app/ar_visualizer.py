"""Simplified AR visualization utilities."""

from typing import Dict


def visualize(flavor_info: Dict[str, str]) -> None:
    """Display a simple ASCII representation of the prediction."""

    frame = (
        "+-------------------------+\n"
        f"| Flavor : {flavor_info.get('flavor','?'):>12} |\n"
        f"| Texture: {flavor_info.get('texture','?'):>12} |\n"
        "+-------------------------+"
    )
    print(frame)

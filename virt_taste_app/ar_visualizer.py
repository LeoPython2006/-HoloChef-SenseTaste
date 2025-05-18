"""Placeholder AR visualization utilities."""

from typing import Dict


def visualize(flavor_info: Dict[str, str]) -> None:
    """Visualize predicted flavor and texture in AR.

    Args:
        flavor_info (Dict[str, str]): Output from FlavorModel.predict.
    """
    # TODO: integrate with AR library/framework
    print("[AR] Predicted flavor: {flavor}, texture: {texture}".format(**flavor_info))

"""Very small AR-style visualization using ASCII art."""

from typing import Dict


def visualize(flavor_info: Dict[str, str]) -> None:
    """Visualize predicted flavor and texture in AR.

    Args:
        flavor_info (Dict[str, str]): Output from FlavorModel.predict.
    """
    flavor = flavor_info.get("flavor", "unknown").title()
    texture = flavor_info.get("texture", "unknown").title()

    art = [
        "   __________   ",
        "  /          \\",
        f" | Flavor: {flavor.center(8)} |",
        f" | Texture: {texture.center(7)} |",
        "  \\__________/",
    ]
    print("\n".join(art))

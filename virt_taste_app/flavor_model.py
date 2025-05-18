"""Model for predicting flavor and texture from chemical composition."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Tuple


class FlavorModel:
    """Nearest-centroid model trained from sample data."""

    def __init__(self, training_file: str | None = None):
        data_path = (
            Path(training_file)
            if training_file
            else Path(__file__).with_name("data") / "training_data.csv"
        )
        self.centroids = self._load_centroids(data_path)

    @staticmethod
    def _load_centroids(path: Path) -> Dict[Tuple[str, str], Dict[str, float]]:
        groups: Dict[Tuple[str, str], list[Dict[str, float]]] = {}
        with path.open(newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                label = (row["flavor"], row["texture"])
                comp = {
                    "water": float(row["water"]),
                    "sugar": float(row["sugar"]),
                    "fat": float(row["fat"]),
                    "protein": float(row["protein"]),
                }
                groups.setdefault(label, []).append(comp)

        centroids: Dict[Tuple[str, str], Dict[str, float]] = {}
        for label, samples in groups.items():
            avg = {
                k: sum(sample[k] for sample in samples) / len(samples)
                for k in samples[0]
            }
            centroids[label] = avg
        return centroids

    def predict(self, composition: Dict[str, float]) -> Dict[str, str]:
        """Predict flavor profile and texture from composition using nearest
        centroid classification."""

        def distance(a: Dict[str, float], b: Dict[str, float]) -> float:
            return sum((a[k] - b.get(k, 0.0)) ** 2 for k in a)

        best_label: Tuple[str, str] | None = None
        best_dist = float("inf")
        for label, centroid in self.centroids.items():
            d = distance(composition, centroid)
            if d < best_dist:
                best_label, best_dist = label, d

        if best_label is None:
            return {"flavor": "unknown", "texture": "unknown"}

        flavor, texture = best_label
        return {"flavor": flavor, "texture": texture}

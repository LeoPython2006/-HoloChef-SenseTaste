"""Model for predicting flavor and texture from chemical composition."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


class FlavorModel:
    """Nearest-centroid model trained from a small CSV dataset."""

    def __init__(self, data_path: str | Path) -> None:
        self.features: List[str] = []
        self.centroids: Dict[Tuple[str, str], List[float]] = {}
        self._load_training_data(Path(data_path))

    def _load_training_data(self, path: Path) -> None:
        with open(path, newline="") as fh:
            reader = csv.DictReader(fh)
            self.features = [f for f in reader.fieldnames if f not in {"flavor", "texture"}]
            sums: Dict[Tuple[str, str], List[float]] = {}
            counts: Dict[Tuple[str, str], int] = {}
            for row in reader:
                key = (row["flavor"], row["texture"])
                vector = [float(row[f]) for f in self.features]
                if key not in sums:
                    sums[key] = [0.0 for _ in self.features]
                    counts[key] = 0
                for i, val in enumerate(vector):
                    sums[key][i] += val
                counts[key] += 1
            for key in sums:
                self.centroids[key] = [v / counts[key] for v in sums[key]]

    def _distance(self, a: Iterable[float], b: Iterable[float]) -> float:
        return sum((x - y) ** 2 for x, y in zip(a, b))

    def predict(self, composition: Dict[str, float]) -> Dict[str, str]:
        """Predict flavor profile and texture from a chemical composition."""

        vector = [composition.get(f, 0.0) for f in self.features]
        best: Tuple[str, str] | None = None
        best_dist: float | None = None
        for label, centroid in self.centroids.items():
            dist = self._distance(vector, centroid)
            if best_dist is None or dist < best_dist:
                best_dist = dist
                best = label
        flavor, texture = best if best else ("unknown", "unknown")
        return {"flavor": flavor, "texture": texture}

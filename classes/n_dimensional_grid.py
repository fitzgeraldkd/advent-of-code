import math
from typing import Tuple

import numpy as np

from collections import defaultdict
from typing import Callable, TypeVar


T = TypeVar("T")


class NDimensionalGrid:
    def __init__(self, dimensions: int, default: Callable[[], T] = lambda: None):
        self._grid = defaultdict(default)
        self.dimensions = dimensions

        self.boundaries = [[math.inf, -1 * math.inf] for _ in range(dimensions)]

    def _update_bounding_box(self, *coords: int):
        for i, value in enumerate(coords):
            boundary = self.boundaries[i]
            boundary[0] = min(boundary[0], value)
            boundary[1] = max(boundary[1], value)

    def get(self, *coords: int):
        return self._grid[coords]

    def get_adjacent(self, *coords: int, include_diagonal=False):
        adjacent = {}

        coord_options = [[coord + n for n in [-1, 1]] for coord in coords]
        for adj in np.array(
            np.meshgrid(*[range(start, end + 1) for start, end in coord_options])
        ).T.reshape(-1, self.dimensions):
            if tuple(adj) == coords:
                continue
            if (
                not include_diagonal
                and sum(abs(coords[n] - adj[n]) for n in range(self.dimensions)) > 1
            ):
                continue

            adjacent[tuple(adj)] = self.get(*adj)

        return adjacent

    def set(self, value: T, *coords: int):
        self._grid[coords] = value
        self._update_bounding_box(*coords)

    def map(
        self,
        point_a: Tuple[int, ...],
        point_b: Tuple[int, ...],
        callable: Callable[..., T],
        inclusive=True,
    ):
        # TODO: Implement.
        pass

    def is_in_bounding_box(self, *coords: int):
        for n in range(self.dimensions):
            if not (self.boundaries[n][0] <= coords[n] <= self.boundaries[n][1]):
                return False
        return True

    @property
    def items(self):
        return self._grid.items()

    @property
    def values(self):
        return self._grid.values()

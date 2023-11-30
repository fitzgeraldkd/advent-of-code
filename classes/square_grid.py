import math
from collections import defaultdict
from typing import Callable, Optional, TypeVar


T = TypeVar("T")


class SquareGrid:
    def __init__(self, default: Optional[Callable[[], T]] = None):
        self._grid = defaultdict(default)

        self.min_x = math.inf
        self.max_x = math.inf * -1
        self.min_y = math.inf
        self.max_y = math.inf * -1

    def _update_bounding_box(self, x: int, y: int):
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def get(self, x: int, y: int):
        return self._grid[(x, y)]

    def set(self, x: int, y: int, value: T):
        self._grid[(x, y)] = value
        self._update_bounding_box(x, y)

    def map(
        self,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        callable: Callable[[T], T],
        inclusive=True,
    ):
        for x in range(min(x1, x2), max(x1, x2) + (1 if inclusive else 0)):
            for y in range(min(y1, y2), max(y1, y2) + (1 if inclusive else 0)):
                self._grid[(x, y)] = callable(self.get(x, y))

        self._update_bounding_box(x1, y1)
        self._update_bounding_box(x2, y2)

    def print(self):
        """
        Note: This assumes the values are strings and have a consistent length.
        """
        for y in range(self.min_y, self.max_y + 1):
            line = ""
            for x in range(self.min_x, self.max_y + 1):
                line += self.get(x, y)
            print(line)

    @property
    def values(self):
        return self._grid.values()
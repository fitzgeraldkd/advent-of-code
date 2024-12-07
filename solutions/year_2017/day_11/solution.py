from typing import Tuple

from common.pathing import move
from solutions import BaseSolution

DIRECTION_MAP = {
    "n": (0, 2),
    "ne": (1, 1),
    "se": (1, -1),
    "s": (0, -2),
    "sw": (-1, -1),
    "nw": (-1, 1),
}


class Year2017Day11(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return line.strip().split(",")

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_distance(self, position: Tuple[int, int]):
        x, y = [abs(coordinate) for coordinate in position]
        due_east_west_distance = x - y if x > y else 0
        return ((x + y + due_east_west_distance) // 2)

    def part_1(self):
        directions = self.inputs

        position = (0, 0)
        for direction in directions:
            position = move(position, DIRECTION_MAP[direction])

        return self.get_distance(position)

    def part_2(self):
        directions = self.inputs

        position = (0, 0)
        max_distance = 0
        for direction in directions:
            position = move(position, DIRECTION_MAP[direction])
            max_distance = max(max_distance, self.get_distance(position))

        return max_distance


if __name__ == "__main__":
    Year2017Day11().print_results()

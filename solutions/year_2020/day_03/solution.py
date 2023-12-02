from typing import Tuple

from classes.square_grid import SquareGrid
from solutions import BaseSolution


def count_encounters(grid: SquareGrid, slope: Tuple[int, int]) -> int:
    encounters = 0
    position = [0, 0]

    while position[1] <= grid.max_y:
        if grid.get(*position) == "#":
            encounters += 1
        position[0] = (position[0] + slope[0]) % (grid.max_x + 1)
        position[1] += slope[1]

    return encounters


class Year2020Day03(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        lines = super()._parse_inputs()
        grid = SquareGrid(default=lambda: ".")
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    grid.set(x, y, "#")

        return grid

    def part_1(self):
        return count_encounters(self.inputs, (3, 1))

    def part_2(self):
        grid = self.inputs
        product = 1
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        for slope in slopes:
            product *= count_encounters(grid, slope)

        return product


if __name__ == "__main__":
    Year2020Day03().print_results()

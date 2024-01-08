from typing import List

from classes.square_grid import SquareGrid
from solutions import BaseSolution


class Year2023Day13(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_group(self, lines: List[str]):
        lines = super()._parse_group(lines)
        grid = SquareGrid(default=lambda: ".")
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                grid.set(x, y, char)
        return grid

    def get_difference(self, first_half: List[str], last_half: List[str]) -> int:
        first_half.reverse()
        length = min(len(first_half), len(last_half))
        return sum(
            sum(True for a, b in zip(first_half[i], last_half[i]) if a != b)
            for i in range(length)
        )

    def find_reflection_line(self, grid: SquareGrid, expected_difference=0):
        cols = ["".join(grid.get(x, y) for y in grid.y_range) for x in grid.x_range]

        for x in range(grid.min_x + 1, grid.max_x + 1):
            left_half = cols[:x]
            right_half = cols[x:]
            if self.get_difference(left_half, right_half) == expected_difference:
                return x, "x"

        rows = ["".join(grid.get(x, y) for x in grid.x_range) for y in grid.y_range]

        for y in range(grid.min_y + 1, grid.max_y + 1):
            top_half = rows[:y]
            bottom_half = rows[y:]
            if self.get_difference(top_half, bottom_half) == expected_difference:
                return y, "y"

    def part_1(self):
        total = 0
        for grid in self.inputs:
            coord, axis = self.find_reflection_line(grid)
            total += coord * (1 if axis == "x" else 100)
        return total

    def part_2(self):
        total = 0
        for grid in self.inputs:
            coord, axis = self.find_reflection_line(grid, expected_difference=1)
            total += coord * (1 if axis == "x" else 100)
        return total


if __name__ == "__main__":
    Year2023Day13().print_results()

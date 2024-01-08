import math
from collections import defaultdict
from typing import Tuple

from classes.square_grid import SquareGrid
from solutions import BaseSolution


class Year2023Day14(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        grid = SquareGrid(default=lambda: "#")
        lines = super()._parse_inputs()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                grid.set(x, y, char)

        return grid

    def tilt(self, grid: SquareGrid, direction: Tuple[int, int]) -> SquareGrid:
        primary_range, secondary_range, primary_axis = (
            (grid.x_range, grid.y_range, "x")
            if direction[1] == 0
            else (grid.y_range, grid.x_range, "y")
        )
        if min(direction) == 0:
            primary_range = reversed(primary_range)

        for i in primary_range:
            for j in secondary_range:
                x, y = (i, j) if primary_axis == "x" else (j, i)
                if grid.get(x, y) == "O":
                    next = [x + direction[0], y + direction[1]]
                    while grid.get(*next) == ".":
                        grid.set(next[0] - direction[0], next[1] - direction[1], ".")
                        grid.set(next[0], next[1], "O")
                        next = [next[0] + direction[0], next[1] + direction[1]]

        return grid

    def calculate_load(self, grid: SquareGrid) -> int:
        row_counts = defaultdict(int)
        max_row = -1 * math.inf
        for x in grid.x_range:
            for y in grid.y_range:
                if grid.get(x, y) != "#":
                    max_row = max(max_row, y)
                if grid.get(x, y) == "O":
                    row_counts[y] += 1

        load = 0
        for row, count in row_counts.items():
            load += (max_row - row + 1) * count

        return load

    def get_state(self, grid: SquareGrid) -> str:
        state = ""
        for x in grid.x_range:
            for y in grid.y_range:
                state += grid.get(x, y)
        return state

    def part_1(self):
        grid = self.inputs

        grid = self.tilt(grid, (0, -1))

        return self.calculate_load(grid)

    def part_2(self):
        rounds = 1000000000
        grid = self.inputs

        state_indeces = {}
        i = 0
        while i < rounds:
            last_four_states = []
            for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                grid = self.tilt(grid, direction)
                state = self.get_state(grid)
                last_four_states.append(state)

            joined_states = " ".join(last_four_states)
            if joined_states in state_indeces:
                cycle_length = i - state_indeces[joined_states]
                remaining_cycles = math.floor((rounds - i) / cycle_length)
                i += cycle_length * remaining_cycles
            else:
                state_indeces[joined_states] = i

            i += 1

        return self.calculate_load(grid)


if __name__ == "__main__":
    Year2023Day14().print_results()

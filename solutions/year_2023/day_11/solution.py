from typing import Dict, Iterable

from classes.square_grid import SquareGrid
from solutions import BaseSolution


class Year2023Day11(BaseSolution):
    PART_2_EXPANSION_FACTOR = 1000000

    module_file = __file__

    def _parse_inputs(self):
        grid = SquareGrid(default=lambda: ".")
        lines = super()._parse_inputs()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "#":
                    grid.set(x, y, char)

        return grid

    def get_expansion_map(self, coords: Iterable[int], factor: int) -> Dict[int, int]:
        sorted_cooreds = sorted(coords)
        prev = sorted_cooreds[0]
        expansion_map = {prev: prev}
        for current in sorted_cooreds[1:]:
            expansion_map[current] = (
                expansion_map[prev]
                + (current - prev - 1) * (factor - 1)
                + (current - prev)
            )
            prev = current

        return expansion_map

    def expand(self, grid: SquareGrid, factor=2) -> SquareGrid:
        universes = [coords for coords, value in grid.items if value == "#"]
        universe_x = {universe[0] for universe in universes}
        universe_y = {universe[1] for universe in universes}

        universe_x_map = self.get_expansion_map(universe_x, factor)
        universe_y_map = self.get_expansion_map(universe_y, factor)

        expanded = SquareGrid(default=lambda: ".")
        for universe in universes:
            expanded.set(universe_x_map[universe[0]], universe_y_map[universe[1]], "#")

        return expanded

    def get_total_distance(self, grid: SquareGrid) -> int:
        total_distance = 0
        universes = [coords for coords, value in grid.items if value == "#"]
        for i in range(len(universes) - 1):
            for j in range(i + 1, len(universes)):
                total_distance += abs(universes[i][0] - universes[j][0]) + abs(
                    universes[i][1] - universes[j][1]
                )
        return total_distance

    def part_1(self):
        grid = self.inputs
        expanded = self.expand(grid)
        return self.get_total_distance(expanded)

    def part_2(self):
        grid = self.inputs
        expanded = self.expand(grid, factor=self.PART_2_EXPANSION_FACTOR)
        return self.get_total_distance(expanded)


if __name__ == "__main__":
    Year2023Day11().print_results()

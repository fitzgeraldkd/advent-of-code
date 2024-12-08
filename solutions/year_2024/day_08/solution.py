from itertools import combinations
from collections import defaultdict

from classes.square_grid import SquareGrid
from common.pathing import move
from solutions import BaseSolution


class Year2024Day08(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        rows = super()._parse_inputs()
        antennas = defaultdict(list)
        for y, row in enumerate(rows):
            for x, char in enumerate(row):
                if char != ".":
                    antennas[char].append((x, y))
        
        size = (len(rows[0]) - 1, len(rows) - 1)
        return antennas, size

    def part_1(self):
        antennas, size = self.inputs
        antinodes = SquareGrid(default=lambda: ".")
        antinodes._update_bounding_box(0, 0)
        antinodes._update_bounding_box(*size)
        for char, coords in antennas.items():
            if len(coords) == 1:
                continue
            
            pairs = combinations(coords, 2)
            for pair in pairs:
                difference = move(pair[0], pair[1], magnitude=-1)
                antinode_a = move(pair[0], difference)
                antinode_b = move(pair[1], difference, magnitude=-1)
                if antinodes.is_in_bounding_box(*antinode_a):
                    antinodes.set(*antinode_a, "#")
                if antinodes.is_in_bounding_box(*antinode_b):
                    antinodes.set(*antinode_b, "#")

        return len([v for v in antinodes.values if v == "#"])

    def part_2(self):
        antennas, size = self.inputs
        antinodes = SquareGrid(default=lambda: ".")
        antinodes._update_bounding_box(0, 0)
        antinodes._update_bounding_box(*size)
        for char, coords in antennas.items():
            if len(coords) == 1:
                continue
            
            pairs = combinations(coords, 2)
            for pair in pairs:
                difference = move(pair[0], pair[1], magnitude=-1)

                antinode_a = pair[0]
                while antinodes.is_in_bounding_box(*antinode_a):
                    antinodes.set(*antinode_a, "#")
                    antinode_a = move(antinode_a, difference)
                
                antinode_b = pair[1]
                while antinodes.is_in_bounding_box(*antinode_b):
                    antinodes.set(*antinode_b, "#")
                    antinode_b = move(antinode_b, difference, magnitude=-1)

        return len([v for v in antinodes.values if v == "#"])


if __name__ == "__main__":
    Year2024Day08().print_results()

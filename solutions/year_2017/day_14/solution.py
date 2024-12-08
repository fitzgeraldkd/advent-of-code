from common.numbers import get_padded_binary
from common.pathing import get_adjacent
from solutions import BaseSolution
from solutions.year_2017.day_10.solution import Year2017Day10

class Year2017Day10WithOverride(Year2017Day10):
    def __init__(self, override_inputs):
        self.override_inputs = override_inputs

    def _parse_inputs(self):
        return self.override_inputs

class Year2017Day14(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def knot_hash(self, value: str):
        return Year2017Day10WithOverride(value).part_2()

    def get_grid(self, key: str):
        grid = []
        for i in range(128):
            hash = self.knot_hash(f'{key}-{i}')
            grid.append(''.join(get_padded_binary(char, 4, 16) for char in hash))
        return grid

    def part_1(self):
        key = self.inputs

        grid = self.get_grid(key)

        return sum(row.count('1') for row in grid)

    def part_2(self):
        key = self.inputs

        grid = self.get_grid(key)
        groups = 0
        coords_to_check = set()

        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char == '1':
                    coords_to_check.add((x, y))

        while len(coords_to_check) > 0:
            groups += 1
            coord_to_check = coords_to_check.pop()
            checked_neighbors = set()
            neighbors_to_check = set()

            for neighbor in get_adjacent(coord_to_check):
                if neighbor in coords_to_check:
                    neighbors_to_check.add(neighbor)

            while len(neighbors_to_check) > 0:
                neighbor = neighbors_to_check.pop()
                checked_neighbors.add(neighbor)
                if neighbor in coords_to_check:
                    coords_to_check.remove(neighbor)
                    for next_neighbor in get_adjacent(neighbor):
                        if next_neighbor not in checked_neighbors:
                            neighbors_to_check.add(next_neighbor)

        return groups


if __name__ == "__main__":
    Year2017Day14().print_results()

from typing import Tuple

from classes.square_grid import SquareGrid
from solutions import BaseSolution


class Year2023Day16(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        grid = SquareGrid()
        lines = super()._parse_inputs()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                grid.set(x, y, char)
        return grid

    def calculate_energized(
        self, grid: SquareGrid, starting_beam: Tuple[Tuple[int, int], Tuple[int, int]]
    ):
        visited = {
            (1, 0): set(),
            (0, 1): set(),
            (-1, 0): set(),
            (0, -1): set(),
        }

        beams = [starting_beam]
        while beams:
            coords, direction = beams.pop()

            while grid.is_in_bounding_box(*coords):
                if coords in visited[direction]:
                    break

                next_tile = grid.get(*coords)
                visited[direction].add(coords)

                if next_tile == "-" and direction[0] == 0:
                    direction = (1, 0)
                    beams.append(((coords[0], coords[1]), (-1, 0)))
                elif next_tile == "|" and direction[1] == 0:
                    direction = (0, 1)
                    beams.append(((coords[0], coords[1]), (0, -1)))
                elif next_tile == "\\":
                    direction = (direction[1], direction[0])
                elif next_tile == "/":
                    direction = (-1 * direction[1], -1 * direction[0])

                coords = (coords[0] + direction[0], coords[1] + direction[1])

        return len(
            visited[(1, 0)]
            .union(visited[(0, 1)])
            .union(visited[(-1, 0)])
            .union(visited[(0, -1)])
        )

    def part_1(self):
        return self.calculate_energized(self.inputs, ((0, 0), (1, 0)))

    def part_2(self):
        grid = self.inputs
        max_energized = 0

        starting_beams = []
        for x in grid.x_range:
            starting_beams.append(((x, 0), (0, 1)))
            starting_beams.append(((x, grid.max_y), (0, -1)))
        for y in grid.y_range:
            starting_beams.append(((0, y), (1, 0)))
            starting_beams.append(((grid.max_x, y), (-1, 0)))

        for starting_beam in starting_beams:
            max_energized = max(
                max_energized, self.calculate_energized(grid, starting_beam)
            )

        return max_energized


if __name__ == "__main__":
    Year2023Day16().print_results()

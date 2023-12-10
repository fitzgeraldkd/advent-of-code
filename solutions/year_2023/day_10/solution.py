from collections import OrderedDict

from classes.square_grid import SquareGrid
from solutions import BaseSolution


DIFFERENCES = {
    (1, 0): {"-", "7", "J"},  # Right.
    (-1, 0): {"-", "F", "L"},  # Left.
    (0, 1): {"|", "J", "L"},  # Down.
    (0, -1): {"|", "7", "F"},  # Up.
}


class Year2023Day10(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        grid = SquareGrid(default=lambda: ".")
        lines = super()._parse_inputs()
        start = None
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                grid.set(x, y, char)
                if char == "S":
                    start = (x, y)

        start_connections = [
            coords
            for coords, value in grid.get_adjacent(
                *start, include_diagonal=False
            ).items()
            if value in DIFFERENCES[(coords[0] - start[0], coords[1] - start[1])]
        ]
        start_differences = [
            (start[0] - coords[0], start[1] - coords[1]) for coords in start_connections
        ]
        start_shape = list(
            DIFFERENCES[start_differences[0]].intersection(
                DIFFERENCES[start_differences[1]]
            )
        )[0]
        grid.set(*start, start_shape)

        return grid, start

    def get_chain(self, grid, start):
        chain = OrderedDict()
        next_pipe = start

        while next_pipe not in chain:
            chain[next_pipe] = True

            try:
                shape = grid.get(*next_pipe)
                next_pipe = next(
                    coords
                    for coords in grid.get_adjacent(
                        *next_pipe, include_diagonal=False
                    ).keys()
                    if shape
                    in DIFFERENCES[(next_pipe[0] - coords[0], next_pipe[1] - coords[1])]
                    and coords not in chain
                )
            except StopIteration:
                break

        return chain

    def part_1(self):
        return int(len(self.get_chain(*self.inputs)) / 2)

    def part_2(self):
        grid, start = self.inputs
        chain = self.get_chain(grid, start)
        contained = 0

        for y in range(grid.min_y, grid.max_y + 1):
            depth = 0
            for x in range(grid.min_x, grid.max_x + 1):
                char = grid.get(x, y)
                if (x, y) in chain:
                    if char in {"|", "L", "J"}:
                        depth += 1
                elif depth % 2 == 1:
                    contained += 1

        return contained


if __name__ == "__main__":
    Year2023Day10().print_results()

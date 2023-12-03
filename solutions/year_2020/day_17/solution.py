from classes.n_dimensional_grid import NDimensionalGrid
from solutions import BaseSolution


class Year2020Day17(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        lines = super()._parse_inputs()
        cube_grid = NDimensionalGrid(dimensions=3, default=lambda: ".")
        hypercube_grid = NDimensionalGrid(dimensions=4, default=lambda: ".")
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                cube_grid.set(char, x, y, 0)
                hypercube_grid.set(char, x, y, 0, 0)
        return cube_grid, hypercube_grid

    def part_1(self):
        grid, _ = self.inputs

        for _ in range(6):
            changes = []

            for x in range(grid.boundaries[0][0] - 1, grid.boundaries[0][1] + 2):
                for y in range(grid.boundaries[1][0] - 1, grid.boundaries[1][1] + 2):
                    for z in range(
                        grid.boundaries[2][0] - 1, grid.boundaries[2][1] + 2
                    ):
                        current = grid.get(x, y, z)
                        adjacent = grid.get_adjacent(x, y, z, include_diagonal=True)
                        active_adjacent = len(
                            [v for v in adjacent.values() if v == "#"]
                        )

                        if current == "#" and active_adjacent not in {2, 3}:
                            changes.append(((x, y, z), "."))
                        elif current == "." and active_adjacent == 3:
                            changes.append(((x, y, z), "#"))

            for coords, value in changes:
                grid.set(value, *coords)

        return len([v for v in grid.values if v == "#"])

    def part_2(self):
        """
        Possible optimization: keep a set of coordinates that tracks where all the
        active cells are. When going through a new iteration, the only cells that need
        to be examined are the cells in that set and their adjacent cells. All other
        cells are inactive and will remain inactive.
        """
        _, grid = self.inputs

        for _ in range(6):
            changes = []

            for x in range(grid.boundaries[0][0] - 1, grid.boundaries[0][1] + 2):
                for y in range(grid.boundaries[1][0] - 1, grid.boundaries[1][1] + 2):
                    for z in range(
                        grid.boundaries[2][0] - 1, grid.boundaries[2][1] + 2
                    ):
                        for w in range(
                            grid.boundaries[3][0] - 1, grid.boundaries[3][1] + 2
                        ):
                            current = grid.get(x, y, z, w)
                            adjacent = grid.get_adjacent(
                                x, y, z, w, include_diagonal=True
                            )
                            active_adjacent = len(
                                [v for v in adjacent.values() if v == "#"]
                            )

                            if current == "#" and active_adjacent not in {2, 3}:
                                changes.append(((x, y, z, w), "."))
                            elif current == "." and active_adjacent == 3:
                                changes.append(((x, y, z, w), "#"))

            for coords, value in changes:
                grid.set(value, *coords)

        return len([v for v in grid.values if v == "#"])


if __name__ == "__main__":
    Year2020Day17().print_results()

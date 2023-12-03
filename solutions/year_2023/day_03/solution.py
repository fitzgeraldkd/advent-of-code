from collections import defaultdict

from classes.square_grid import SquareGrid

from solutions import BaseSolution

NUMBERS = set("0123456789")
NON_SYMBOLS = set("0123456789.")


class Year2023Day03(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        grid = SquareGrid(default=lambda: ".")
        for y, line in enumerate(super()._parse_inputs()):
            for x, char in enumerate(line):
                grid.set(x, y, char)
        return grid

    def part_1(self):
        grid = self.inputs
        total = 0

        for y in range(grid.min_y, grid.max_y + 1):
            number = ""
            is_part_number = False

            for x in range(grid.min_x, grid.max_x + 1):
                char = grid.get(x, y)

                if char in NUMBERS:
                    number += char
                    adjacent = grid.get_adjacent(x, y, include_diagonal=True)
                    is_part_number |= any(
                        value not in NON_SYMBOLS for value in adjacent.values()
                    )

                if char not in NUMBERS or x == grid.max_x:
                    total += int(number) if is_part_number else 0
                    number = ""
                    is_part_number = False

        return total

    def part_2(self):
        grid = self.inputs
        gears = defaultdict(list)

        for y in range(grid.min_y, grid.max_y + 1):
            number = ""
            is_part_number = False
            this_gears = set()
            for x in range(grid.min_x, grid.max_x + 1):
                char = grid.get(x, y)

                if char in NUMBERS:
                    number += char
                    adjacent = grid.get_adjacent(x, y, include_diagonal=True)
                    is_part_number |= any(
                        value not in NON_SYMBOLS for value in adjacent.values()
                    )
                    for coords, value in adjacent.items():
                        if value == "*":
                            this_gears.add(coords)

                if char not in NUMBERS or x == grid.max_x:
                    if is_part_number:
                        for gear in this_gears:
                            gears[gear].append(int(number))
                    number = ""
                    is_part_number = False
                    this_gears = set()

        total = 0
        for parts in gears.values():
            if len(parts) == 2:
                total += parts[0] * parts[1]
        return total


if __name__ == "__main__":
    Year2023Day03().print_results()

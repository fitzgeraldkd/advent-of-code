from classes.square_grid import SquareGrid
from solutions import BaseSolution


DIRECTIONS = [
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
]


def get_visible_seats(grid: SquareGrid, x: int, y: int):
    occupied_count = 0
    for direction in DIRECTIONS:
        adjacent = [x, y]
        seat = None
        while seat not in {"L", "#"} and grid.is_in_bounding_box(*adjacent):
            adjacent[0] += direction[0]
            adjacent[1] += direction[1]
            seat = grid.get(*adjacent)

        if seat == "#":
            occupied_count += 1

    return occupied_count


class Year2020Day11(BaseSolution):
    def _parse_inputs(self):
        lines = super()._parse_inputs()
        grid = SquareGrid(default=lambda: ".")
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "L":
                    grid.set(x, y, "L")
        return grid

    def part_1(self):
        grid = self.inputs

        changes = []
        changed = True
        while changed:
            for x, y, state in changes:
                grid.set(x, y, state)
            changes = []

            seats = grid.items
            empty_seats = [seat[0] for seat in seats if seat[1] == "L"]
            occupied_seats = [seat[0] for seat in seats if seat[1] == "#"]

            for empty_seat in empty_seats:
                adjacent = grid.get_adjacent(
                    empty_seat[0], empty_seat[1], include_diagonal=True
                )
                if list(adjacent.values()).count("#") == 0:
                    changes.append((empty_seat[0], empty_seat[1], "#"))

            for occupied_seat in occupied_seats:
                adjacent = grid.get_adjacent(
                    occupied_seat[0], occupied_seat[1], include_diagonal=True
                )
                if list(adjacent.values()).count("#") >= 4:
                    changes.append((occupied_seat[0], occupied_seat[1], "L"))

            changed = bool(changes)

        return list(grid.values).count("#")

    def part_2(self):
        grid = self.inputs

        changes = []
        changed = True
        while changed:
            for x, y, state in changes:
                grid.set(x, y, state)
            changes = []

            seats = grid.items
            empty_seats = [seat[0] for seat in seats if seat[1] == "L"]
            occupied_seats = [seat[0] for seat in seats if seat[1] == "#"]

            for empty_seat in empty_seats:
                occupied_count = get_visible_seats(grid, *empty_seat)
                if occupied_count == 0:
                    changes.append((empty_seat[0], empty_seat[1], "#"))

            for occupied_seat in occupied_seats:
                occupied_count = get_visible_seats(grid, *occupied_seat)
                if occupied_count >= 5:
                    changes.append((occupied_seat[0], occupied_seat[1], "L"))

            changed = bool(changes)

        return list(grid.values).count("#")


if __name__ == "__main__":
    Year2020Day11(__file__).print_results()

import re

from classes.square_grid import SquareGrid
from solutions import BaseSolution


class Year2015Day06(BaseSolution):
    def _parse_line(self, line: str):
        split_line = re.split(r"(turn on|turn off|toggle)", line.strip())
        coordinates = [
            [int(val) for val in coordinate.split(",")]
            for coordinate in split_line[2].split(" through ")
        ]

        return (
            split_line[1],
            {
                "x1": coordinates[0][0],
                "x2": coordinates[1][0],
                "y1": coordinates[0][1],
                "y2": coordinates[1][1],
            },
        )

    def part_1(self):
        lights = SquareGrid(default=lambda: False)

        for command, coords in self.inputs:
            if command == "turn on":
                lights.map(callable=lambda _: True, **coords)
            elif command == "turn off":
                lights.map(callable=lambda _: False, **coords)
            else:
                lights.map(callable=lambda current: not current, **coords)

        return len([on for on in lights.values if on])

    def part_2(self):
        lights = SquareGrid(default=lambda: 0)

        for command, coords in self.inputs:
            if command == "turn on":
                lights.map(callable=lambda current: current + 1, **coords)
            elif command == "turn off":
                lights.map(callable=lambda current: max(0, current - 1), **coords)
            else:
                lights.map(callable=lambda current: current + 2, **coords)

        return sum(lights.values)


if __name__ == "__main__":
    Year2015Day06(__file__).print_results()

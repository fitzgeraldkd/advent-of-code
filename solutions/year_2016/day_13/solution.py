import operator

from common.pathing import DIRECTIONS, a_star
from solutions import BaseSolution


class Year2016Day13(BaseSolution):
    module_file = __file__

    TARGET = (31, 39)

    def _parse_line(self, line: str):
        return int(line.strip())

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_is_wall(self, location: tuple, **kwargs):
        x, y = location
        if min(x, y) < 0:
            return True
        foo = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + self.inputs
        binary = "{0:b}".format(foo)
        return binary.count("1") % 2 == 1

    def get_heuristic(self, location: tuple, goal: tuple):
        return abs(location[0] - goal[0]) + abs(location[1] - goal[1])

    def print_map(self, size: int):
        for y in range(size):
            row = []
            for x in range(size):
                is_wall = self.get_is_wall((x, y))
                row.append("#" if is_wall else ".")
            print("".join(row))

    def part_1(self):
        path = a_star((1, 1), self.TARGET, self.get_is_wall, self.get_heuristic)
        return len(path) - 1

    def part_2(self):
        locations = {(1, 1)}
        nodes = {(1, 1)}
        for _ in range(50):
            neighbors = set()
            for current in nodes:
                for neighbor in [
                    tuple(map(operator.add, current, direction))
                    for direction in DIRECTIONS
                ]:
                    if not self.get_is_wall(neighbor):
                        locations.add(neighbor)
                        neighbors.add(neighbor)
            nodes = neighbors

        return len(locations)


if __name__ == "__main__":
    Year2016Day13().print_results()

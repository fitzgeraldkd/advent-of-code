import itertools
import operator
import re

from common.pathing import DIRECTIONS
from solutions import BaseSolution


class Year2016Day22(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        if not line.startswith("/"):
            return None, None

        x, y, size, used, avail, percent = [
            int(x) for x in re.findall(r"\d+", line.strip())
        ]
        return (x, y), {
            "size": size,
            "used": used,
            "avail": avail,
            "use%": percent,
        }

    def _parse_inputs(self):
        parsed_lines = super()._parse_inputs()
        nodes = {}
        for coords, details in parsed_lines:
            if coords is not None:
                nodes[coords] = details

        return nodes

    def is_viable(self, node_a: dict, node_b: dict):
        if node_a["used"] == 0:
            return False
        if node_b["avail"] < node_a["used"]:
            return False

        return True

    def get_adjacent(position: tuple, max_x: int, max_y: int):
        adjacent = []
        for direction in DIRECTIONS:
            neighbor = tuple(map(operator.add, position, direction))
            if min(neighbor) >= 0 and neighbor[0] <= max_x and neighbor[1] <= max_y:
                adjacent.append(neighbor)
        return adjacent

    def part_1(self):
        nodes = self.inputs
        permutations = list(itertools.permutations(nodes.keys(), 2))

        viable_count = 0
        for position_a, position_b in permutations:
            if self.is_viable(nodes[position_a], nodes[position_b]):
                viable_count += 1

        return viable_count

    def part_2(self):
        nodes = self.inputs
        max_x = 0
        max_y = 0

        for position in nodes:
            max_x = max(max_x, position[0])
            max_y = max(max_y, position[1])

        return None


if __name__ == "__main__":
    Year2016Day22().print_results()

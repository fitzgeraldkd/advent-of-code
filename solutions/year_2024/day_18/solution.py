from common.pathing import a_star, get_manhattan_distance
from solutions import BaseSolution


class Year2024Day18(BaseSolution):
    module_file = __file__
    PART_1_BYTES = 1024
    END = (70, 70)

    def _parse_line(self, line):
        return tuple(int(v) for v in super()._parse_line(line).split(","))

    def is_out_of_bounds(self, coords):
        return (
            coords[0] < 0 or
            coords[1] < 0 or
            coords[0] > self.END[0] or
            coords[1] > self.END[1]
        )

    def part_1(self):
        walls = set(self.inputs[:self.PART_1_BYTES])

        def get_is_wall(coords, current):
            return self.is_out_of_bounds(coords) or coords in walls

        def get_heuristic(current, goal):
            return get_manhattan_distance(current, goal)

        path = a_star((0, 0), self.END, get_is_wall, get_heuristic)
        return len(path) - 1

    def part_2(self):
        walls = set(self.inputs[:self.PART_1_BYTES])
        remaining = self.inputs[self.PART_1_BYTES:]

        def get_is_wall(coords, current):
            return self.is_out_of_bounds(coords) or coords in walls

        def get_heuristic(current, goal):
            return get_manhattan_distance(current, goal)

        path = a_star((0, 0), self.END, get_is_wall, get_heuristic)

        for new_wall in remaining:
            walls.add(new_wall)
            if new_wall in path:
                path = a_star((0, 0), self.END, get_is_wall, get_heuristic)
                if path is None:
                    return ",".join([str(v) for v in new_wall])


if __name__ == "__main__":
    Year2024Day18().print_results()

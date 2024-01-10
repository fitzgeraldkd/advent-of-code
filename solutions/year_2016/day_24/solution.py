import itertools
import math

from common.pathing import a_star
from solutions import BaseSolution


class Year2016Day24(BaseSolution):
    module_file = __file__

    def get_locations(self, layout):
        locations = {}
        for y, row in enumerate(layout):
            for x, tile in enumerate(row):
                if tile not in ".#":
                    locations[tile] = (x, y)
        return locations

    def part_1(self):
        layout = self.inputs
        locations = self.get_locations(layout)
        pairings = list(itertools.combinations(locations, 2))

        def get_is_wall(coords: tuple, **kwargs):
            return layout[coords[1]][coords[0]] == "#"

        def get_heuristic(start: tuple, goal: tuple):
            return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

        distances = {}
        for pairing in pairings:
            distance = (
                len(
                    a_star(
                        locations[pairing[0]],
                        locations[pairing[1]],
                        get_is_wall,
                        get_heuristic,
                    )
                )
                - 1
            )
            if pairing[0] in distances:
                distances[pairing[0]][pairing[1]] = distance
            else:
                distances[pairing[0]] = {pairing[1]: distance}
            if pairing[1] in distances:
                distances[pairing[1]][pairing[0]] = distance
            else:
                distances[pairing[1]] = {pairing[0]: distance}

        start = locations.pop("0")
        routes = list(itertools.permutations(locations))

        min_route = ""
        min_distance = math.inf
        for route in routes:
            current = "0"
            distance = 0
            for node in route:
                distance += distances[current][node]
                current = node
            min_distance = min(distance, min_distance)
            min_route = route

        return min_distance

    def part_2(self):
        layout = self.inputs
        locations = self.get_locations(layout)
        pairings = list(itertools.combinations(locations, 2))

        def get_is_wall(coords: tuple, **kwargs):
            return layout[coords[1]][coords[0]] == "#"

        def get_heuristic(start: tuple, goal: tuple):
            return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

        distances = {}
        for pairing in pairings:
            distance = (
                len(
                    a_star(
                        locations[pairing[0]],
                        locations[pairing[1]],
                        get_is_wall,
                        get_heuristic,
                    )
                )
                - 1
            )
            if pairing[0] in distances:
                distances[pairing[0]][pairing[1]] = distance
            else:
                distances[pairing[0]] = {pairing[1]: distance}
            if pairing[1] in distances:
                distances[pairing[1]][pairing[0]] = distance
            else:
                distances[pairing[1]] = {pairing[0]: distance}

        start = locations.pop("0")
        routes = list(itertools.permutations(locations))

        min_route = ""
        min_distance = math.inf
        for route in routes:
            current = "0"
            distance = 0
            for node in route:
                distance += distances[current][node]
                current = node
            distance += distances[current]["0"]
            min_distance = min(distance, min_distance)
            min_route = route

        return min_distance


if __name__ == "__main__":
    Year2016Day24().print_results()

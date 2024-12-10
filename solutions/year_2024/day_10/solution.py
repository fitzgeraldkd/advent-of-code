from classes.square_grid import SquareGrid
from common.pathing import get_adjacent
from solutions import BaseSolution


class Year2024Day10(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return [int(v) for v in super()._parse_line(line)]

    def analyze_map(self):
        inputs = self.inputs
        grid = SquareGrid(default=lambda: None)

        for y, row in enumerate(inputs):
            for x, value in enumerate(row):
                score = 1 if value == 9 else 0
                unique_peaks = set([(x, y)]) if value == 9 else set()
                grid.set(x, y, { "elevation": value, "score": score, "unique_peaks": unique_peaks })

        for elevation in range(9, 0, -1):
            for y in grid.y_range:
                for x in grid.x_range:
                    details = grid.get(x, y)
                    if details["elevation"] != elevation:
                        continue
                    adjacent_tiles = get_adjacent((x, y))
                    for tile in adjacent_tiles:
                        if not grid.is_in_bounding_box(*tile):
                            continue
                        adjacent_details = grid.get(*tile)
                        if adjacent_details["elevation"] != elevation - 1:
                            continue
                        adjacent_details["score"] += details["score"]
                        adjacent_details["unique_peaks"].update(details["unique_peaks"])

        return grid

    def part_1(self):
        grid = self.analyze_map()
        results = 0

        for value in grid.values:
            if value["elevation"] == 0:
                results += len(value["unique_peaks"])

        return results

    def part_2(self):
        grid = self.analyze_map()
        results = 0

        for value in grid.values:
            if value["elevation"] == 0:
                results += value["score"]

        return results


if __name__ == "__main__":
    Year2024Day10().print_results()

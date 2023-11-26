import math
from collections import Counter

from solutions import BaseSolution

PART_2_TARGET_DISTANCE = 10000


def get_bounding_box(coordinates):
    min_x = min(coordinates, key=lambda coordinate: coordinate[0])[0]
    max_x = max(coordinates, key=lambda coordinate: coordinate[0])[0]
    min_y = min(coordinates, key=lambda coordinate: coordinate[1])[1]
    max_y = max(coordinates, key=lambda coordinate: coordinate[1])[1]
    return min_x, max_x, min_y, max_y


class Year2018Day06(BaseSolution):
    def _parse_line(self, line: str):
        return tuple(int(coordinate) for coordinate in line.strip().split(", "))

    def part_1(self):
        coordinates = self.inputs

        min_x, max_x, min_y, max_y = get_bounding_box(coordinates)

        board = {}
        infinite_regions = set()

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                closest_distance = math.inf
                closest_coordinate = None
                for coordinate in coordinates:
                    distance = abs(coordinate[0] - x) + abs(coordinate[1] - y)
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_coordinate = coordinate
                    elif distance == closest_distance:
                        closest_coordinate = None
                board[(x, y)] = closest_coordinate
                if closest_coordinate is not None and (
                    x in [min_x, max_x] or y in [min_y, max_y]
                ):
                    infinite_regions.add(closest_coordinate)

        counted_board = Counter(board.values())
        for coordinate in infinite_regions:
            del counted_board[coordinate]

        return counted_board.most_common(1)[0][1]

    def part_2(self):
        coordinates = self.inputs

        min_x, max_x, min_y, max_y = get_bounding_box(coordinates)

        region_size = 0

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                total_distance = sum(
                    abs(coordinate[0] - x) + abs(coordinate[1] - y)
                    for coordinate in coordinates
                )
                region_size += 1 if total_distance < PART_2_TARGET_DISTANCE else 0

        return region_size


if __name__ == "__main__":
    Year2018Day06(__file__).print_results()

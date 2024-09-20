import math

from classes.n_dimensional_grid import NDimensionalGrid
from common.pathing import move, rotate
from solutions import BaseSolution


class Year2017Day03(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line)
    
    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        tile = self.inputs

        next_root = math.ceil(math.sqrt(tile))
        prev_root = next_root - 1
        prev_square = prev_root ** 2
        next_square = next_root ** 2
        corner = int((next_square + (prev_square + 1)) / 2)
        distance = math.ceil((next_root - 1) / 2)

        if tile == corner:
            distance *= 2
        elif tile < corner:
            midpoint = int((corner + prev_square + 1) / 2)
            distance += abs(midpoint - tile)
        elif tile > corner:
            midpoint = int((corner + next_square + 1) / 2)
            distance += abs(midpoint - tile)

        return distance

    def part_2(self):
        value = self.inputs

        grid = NDimensionalGrid(dimensions=2, default=lambda: 0)
        grid.set(1, 0, 0)

        position = (1, 0)
        direction = (0, -1)

        while True:
            new_value = sum(grid.get_adjacent(*position, include_diagonal=True).values())

            if new_value > value:
                return new_value
            
            grid.set(new_value, *position)
            position = move(position, direction)
            
            if not grid.is_in_bounding_box(*position):
                direction = rotate(direction, 'L')


if __name__ == "__main__":
    Year2017Day03().print_results()

import math

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

        grid = { 0: { 0: 1 } }

        x, y, max_x, min_x, max_y, min_y = 1, 0, 1, 0, 0, 0
        direction = 'up'

        while True:
            new_value = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_value += grid.get(y+dy, {}).get(x+dx, 0)

            if new_value > value:
                return new_value
            if y in grid:
                grid[y][x] = new_value
            else:
                grid[y] = { x: new_value }

            if direction == 'right':
                x += 1
                if x > max_x:
                    max_x = x
                    direction = 'up'
            elif direction == 'up':
                y -= 1
                if y < min_y:
                    min_y = y
                    direction = 'left'
            elif direction == 'left':
                x -= 1
                if x < min_x:
                    min_x = x
                    direction = 'down'
            else:
                y += 1
                if y > max_y:
                    max_y = y
                    direction = 'right'


if __name__ == "__main__":
    Year2017Day03().print_results()

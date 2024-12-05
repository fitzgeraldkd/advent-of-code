from solutions import BaseSolution
from common.pathing import move

DIRECTIONS = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
]


class Year2024Day04(BaseSolution):
    module_file = __file__

    def part_1(self):
        inputs = self.inputs
        results = 0
        target_string = 'XMAS'

        for y, row in enumerate(self.inputs):
            for x, value in enumerate(row):
                if value != "X":
                    continue
                for direction in DIRECTIONS:
                    string = value
                    for i in range(3):
                        adj_x, adj_y = move((x, y), direction, i+1)
                        if adj_x < 0 or adj_x >= len(inputs[0]) or adj_y < 0 or adj_y >= len(inputs):
                            break
                        next_char = inputs[adj_y][adj_x]
                        if next_char != target_string[len(string)]:
                            continue
                        string += next_char

                    if string == target_string:
                        results += 1        
        
        return results

    def part_2(self):
        inputs = self.inputs
        results = 0
        for y, row in enumerate(self.inputs):
            for x, value in enumerate(row):
                if value != "A":
                    continue
                success = True
                for direction in [(1, 1), (1, -1)]:
                    adjacent_chars = []
                    for i in [-1, 1]:
                        adj_x, adj_y = move((x, y), direction, i)
                        if adj_x < 0 or adj_x >= len(inputs[0]) or adj_y < 0 or adj_y >= len(inputs):
                            break
                        next_char = inputs[adj_y][adj_x]
                        if next_char not in ['M', 'S']:
                            continue
                        adjacent_chars.append(next_char)
                    if 'M' not in adjacent_chars or 'S' not in adjacent_chars or len(adjacent_chars) != 2:
                        success = False
                        break
                if success:
                    results += 1        
        
        return results


if __name__ == "__main__":
    Year2024Day04().print_results()

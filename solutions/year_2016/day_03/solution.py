import re

from solutions import BaseSolution


class Year2016Day03(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return [int(x) for x in re.findall(r"\d+", line.strip())]

    def part_1(self):
        inputs = self.inputs

        possible_triangles = 0
        for input in inputs:
            [x, y, z] = sorted(input)
            if x + y > z:
                possible_triangles += 1

        return possible_triangles

    def part_2(self):
        inputs = self.inputs

        possible_triangles = 0
        starting_row = 0
        while starting_row < len(inputs) - 1:
            for i in range(3):
                sides = []
                for j in range(3):
                    sides.append(inputs[starting_row + j][i])
                [x, y, z] = sorted(sides)
                if x + y > z:
                    possible_triangles += 1
            starting_row += 3

        return possible_triangles


if __name__ == "__main__":
    Year2016Day03().print_results()

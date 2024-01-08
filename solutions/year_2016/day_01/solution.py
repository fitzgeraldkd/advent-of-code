from solutions import BaseSolution
from common.pathing import get_manhattan_distance, move, rotate


class Year2016Day01(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return line.strip().split(', ')
    
    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        inputs = self.inputs

        direction = (0, 1)
        position = (0, 0)

        for input in inputs:
            direction = rotate(direction, input[0])
            position = move(position, direction, magnitude=int(input[1:]))

        return get_manhattan_distance(position, (0, 0))

    def part_2(self):
        inputs = self.inputs

        direction = (0, 1)
        position = (0, 0)
        visited = set()

        for input in inputs:
            direction = rotate(direction, input[0])
            distance = int(input[1:])

            for _ in range(distance):
                position = move(position, direction)
                if position in visited:
                    return get_manhattan_distance(position, (0, 0))
                else:
                    visited.add(position)


if __name__ == "__main__":
    Year2016Day01().print_results()

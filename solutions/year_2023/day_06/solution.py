import math
import re

from solutions import BaseSolution


class Year2023Day06(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return [int(v) for v in re.findall(r"\d+", line.strip())]

    def _parse_inputs(self):
        parsed_lines = super()._parse_inputs()
        races = []
        for i in range(len(parsed_lines[0])):
            races.append((parsed_lines[0][i], parsed_lines[1][i]))
        return races

    def get_winning_possibilities(self, duration, distance):
        """
        0 = -1 * t ** 2 + t * duration - distance
        """
        a = -1
        b = duration
        c = -1 * distance
        return (
            math.ceil(((-1 * b) - math.sqrt((b**2) - 4 * a * c)) / (2 * a))
            - math.floor(((-1 * b) + math.sqrt((b**2) - 4 * a * c)) / (2 * a))
            - 1
        )

    def part_1(self):
        result = 1
        for duration, distance in self.inputs:
            result *= self.get_winning_possibilities(duration, distance)
        return result

    def part_2(self):
        t, d = [int("".join([str(v) for v in l])) for l in list(zip(*(self.inputs)))]
        return self.get_winning_possibilities(t, d)


if __name__ == "__main__":
    Year2023Day06().print_results()

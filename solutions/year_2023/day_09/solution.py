import re

from solutions import BaseSolution


class Year2023Day09(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return [int(v) for v in re.findall(r"\-?\d+", line.strip())]

    def get_history(self, line, is_part_1=True):
        next_sequence = [(line[i + 1] - line[i]) for i in range(len(line) - 1)]
        if all([v == 0 for v in next_sequence]):
            return line[0]
        elif is_part_1:
            return line[-1] + self.get_history(next_sequence, is_part_1)
        else:
            return line[0] - self.get_history(next_sequence, is_part_1)

    def part_1(self):
        return sum([self.get_history(line) for line in self.inputs])

    def part_2(self):
        return sum([self.get_history(line, is_part_1=False) for line in self.inputs])


if __name__ == "__main__":
    Year2023Day09().print_results()

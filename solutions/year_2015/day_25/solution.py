import re

from solutions import BaseSolution


class Year2015Day25(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return [int(value) for value in re.findall(r"\d{1,}", line.strip())][::-1]

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_index(self, x, y):
        index = 1
        for i in range(x - 1):
            index += i + 2

        for i in range(y - 1):
            index += x + i

        return index

    def part_1(self):
        x, y = self.inputs
        code = 20151125

        for _ in range(self.get_index(x, y) - 1):
            code = (code * 252533) % 33554393

        return code

    def part_2(self):
        return None


if __name__ == "__main__":
    Year2015Day25().print_results()

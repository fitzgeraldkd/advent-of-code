import re
from typing import List

from solutions import BaseSolution


class Year2017Day02(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return [int(cell) for cell in re.split(r'\s+', line.strip())]

    def part_1(self):
        spreadsheet = self.inputs
        total = 0

        for row in spreadsheet:
            total += max(row) - min(row)

        return total

    def part_2_row_result(self, row: List[int]):
        sorted_row = sorted(row)
        while len(sorted_row) > 0:
            dividend = sorted_row.pop()
            for divisor in sorted_row:
                if dividend % divisor == 0:
                    return int(dividend / divisor)
                if divisor > dividend / 2:
                    break

    def part_2(self):
        spreadsheet = self.inputs
        total = 0

        for row in spreadsheet:
            total += self.part_2_row_result(row)

        return total


if __name__ == "__main__":
    Year2017Day02().print_results()

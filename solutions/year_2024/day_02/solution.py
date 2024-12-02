from solutions import BaseSolution
from typing import List
from itertools import combinations


class Year2024Day02(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        line = super()._parse_line(line)
        return [int(v) for v in line.split(' ')]
    
    def is_safe(self, row: List[int]):
        if row[1] > row[0]:
            direction = 'inc'
        elif row[1] < row[0]:
            direction = 'dec'
        else:
            return False
        
        prev = row[0]
        for v in row[1:]:
            if direction == 'inc' and v < prev:
                return False
            elif direction == 'dec' and v > prev:
                return False
            elif abs(v - prev) > 3 or abs(v - prev) == 0:
                return False
            prev = v
        
        return True


    def part_1(self):
        safe_rows = 0

        for row in self.inputs:
            if self.is_safe(row):
                safe_rows += 1

        return safe_rows

    def part_2(self):
        safe_rows = 0

        for row in self.inputs:
            if self.is_safe(row):
                safe_rows += 1
            else:
                row_combinations = combinations(row, len(row) - 1)
                for combo in row_combinations:
                    if self.is_safe(combo):
                        safe_rows += 1
                        break

        return safe_rows


if __name__ == "__main__":
    Year2024Day02().print_results()

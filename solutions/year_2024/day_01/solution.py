import re
from collections import Counter
from solutions import BaseSolution


class Year2024Day01(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        rows = super()._parse_inputs()
        left_list = []
        right_list = []
        for row in rows:
            left_list.append(row[0])
            right_list.append(row[1])
        return [left_list, right_list]

    def _parse_line(self, line):
        return [int(v) for v in re.findall(r'\d+', line)]

    def part_1(self):
        left_list, right_list = self.inputs
        left_list = sorted(left_list)
        right_list = sorted(right_list)
        distance = 0
        for i in range(len(left_list)):
            distance += abs(left_list[i] - right_list[i])
        
        return distance

    def part_2(self):
        left_list, right_list = self.inputs
        counted_left_list = Counter(left_list)
        counted_right_list = Counter(right_list)

        distance = 0
        for v in counted_left_list:

            distance += v * counted_left_list[v] * counted_right_list[v]        
        
        return distance


if __name__ == "__main__":
    Year2024Day01().print_results()

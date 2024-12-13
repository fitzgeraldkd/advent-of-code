import re
from common.pathing import move
from solutions import BaseSolution


class Year2024Day13(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_group(self, lines):
        results = []
        for line in lines:
            x = int(re.search(r'X[\+\=]\d+', line).group()[2:])
            y = int(re.search(r'Y[\+\=]\d+', line).group()[2:])
            results.append((x, y))
        return results

    def get_cheapest_win(self, a, b, target):
        i, k = a
        j, l = b
        x, y = target
        b_presses = x / ( ((x * l / y - j) / (i - x * k / y)) * i + j)
        if round(b_presses, 3) != round(b_presses):
            return 0
        a_presses = ( (x * l / y - j) / (i - x * k / y) ) * b_presses
        if round(a_presses, 3) != round(a_presses):
            return 0

        return round(a_presses * 3 + b_presses)

    def part_1(self):
        results = 0

        for a, b, target in self.inputs:
            results += self.get_cheapest_win(a, b, target)

        return results

    def part_2(self):
        results = 0
        offset = 10000000000000

        for a, b, target in self.inputs:
            offset_target = move(target, (1, 1), offset)
            results += self.get_cheapest_win(a, b, offset_target)

        return results


if __name__ == "__main__":
    Year2024Day13().print_results()

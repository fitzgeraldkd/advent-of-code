from typing import List, Tuple

from solutions import BaseSolution


def find_pair(expenses: List[int], target: int) -> Tuple[int, int]:
    expenses_set = set(expenses)

    for expense in expenses_set:
        if (target - expense) in expenses_set:
            return expense, (target - expense)


class Year2020Day01(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def part_1(self):
        pair = find_pair(self.inputs, target=2020)
        return pair[0] * pair[1]

    def part_2(self):
        expenses = self.inputs
        for index, expense in enumerate(expenses):
            pair = find_pair(expenses[index + 1 :], target=2020 - expense)
            if pair is not None:
                return expense * pair[0] * pair[1]


if __name__ == "__main__":
    Year2020Day01().print_results()

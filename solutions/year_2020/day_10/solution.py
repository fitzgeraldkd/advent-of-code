from itertools import combinations
from typing import List, Tuple

from solutions import BaseSolution


def is_valid(adapters: List[int]) -> bool:
    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] > 3:
            return False
    return True


def test_permutations(adapters: List[int], index_range: Tuple[int, int]):
    test_cases = []
    for i in range(1, 2 + index_range[1] - index_range[0]):
        test_cases.extend(combinations(range(index_range[0], index_range[1] + 1), i))

    valid_permutations = 1
    for test_case in test_cases:
        test_adapters = [*adapters]
        for i in sorted(test_case, reverse=True):
            test_adapters.pop(i)
        if is_valid(test_adapters):
            valid_permutations += 1

    return valid_permutations


class Year2020Day10(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def _parse_inputs(self):
        adapters = [0, *sorted(super()._parse_inputs())]
        adapters.append(max(adapters) + 3)
        return adapters

    def part_1(self):
        adapters = sorted(self.inputs)
        jump_counts = {1: 0, 2: 0, 3: 0}

        for i in range(len(adapters) - 1):
            jump_counts[adapters[i + 1] - adapters[i]] += 1

        return jump_counts[1] * jump_counts[3]

    def part_2(self):
        adapters = self.inputs

        # The outlet and the device cannot be removed.
        locked_indeces = {0, len(adapters) - 1}

        # If removing an adapter would create a jolt differences greater than 3, then it is required.
        for i, adapter in enumerate(adapters):
            if i in {0, len(adapters) - 1}:
                continue

            if adapter - adapters[i - 1] == 3:
                locked_indeces.add(i - 1)
                locked_indeces.add(i)
            elif adapters[i + 1] - adapter == 3:
                locked_indeces.add(i)
                locked_indeces.add(i + 1)
            elif adapter - adapters[i - 1] == 2 and adapters[i + 1] - adapter == 2:
                locked_indeces.add(i)

        # Identify groups of consecutive, unlocked indeces. Any permutation can be tested within individual groups
        # without affecting other groups' checks.
        unlocked_indeces = set(range(len(adapters))) - locked_indeces
        unlocked_index_ranges = []
        next_range = None
        for i in sorted(unlocked_indeces):
            if next_range is None:
                next_range = [i, i]
            elif i - next_range[1] == 1:
                next_range[1] = i
            else:
                unlocked_index_ranges.append((*next_range,))
                next_range = [i, i]

        unlocked_index_ranges.append((*next_range,))

        valid_combinations = 1
        for index_range in unlocked_index_ranges:
            valid_combinations *= test_permutations(adapters, index_range)

        return valid_combinations


if __name__ == "__main__":
    Year2020Day10().print_results()

import re
from typing import List

from solutions import BaseSolution


class Year2017Day06(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return [int(value) for value in re.split(r'\s+', line.strip())]

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def stringify_banks(self, banks: List[int]):
        return ','.join(str(value) for value in banks)

    def part_1(self):
        banks = self.inputs

        checked_states = set()

        cycles = 0
        while self.stringify_banks(banks) not in checked_states:
            checked_states.add(self.stringify_banks(banks))

            max_index = max(range(len(banks)), key=banks.__getitem__)
            amount_to_add = banks[max_index] // len(banks)
            extra = banks[max_index] % len(banks)
            banks[max_index] = 0
            for i in range(len(banks)):
                index = (max_index + i + 1) % len(banks)
                banks[index] += amount_to_add + (1 if i < extra else 0)

            cycles += 1

        return cycles

    def part_2(self):
        banks = self.inputs

        checked_states = {}

        cycles = 0
        while self.stringify_banks(banks) not in checked_states:
            checked_states[self.stringify_banks(banks)] = cycles

            max_index = max(range(len(banks)), key=banks.__getitem__)
            amount_to_add = banks[max_index] // len(banks)
            extra = banks[max_index] % len(banks)
            banks[max_index] = 0
            for i in range(len(banks)):
                index = (max_index + i + 1) % len(banks)
                banks[index] += amount_to_add + (1 if i < extra else 0)

            cycles += 1

        return cycles - checked_states[self.stringify_banks(banks)]


if __name__ == "__main__":
    Year2017Day06().print_results()

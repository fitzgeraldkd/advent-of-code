from typing import List
from solutions import BaseSolution


class Year2017Day10(BaseSolution):
    module_file = __file__

    LENGTH = 256

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_starting_list(self):
        return [i for i in range(self.LENGTH)]

    def process_rounds(self, knot_list: List[int], lengths: List[int], number_of_rounds: int = 1):
        position = 0
        skip_size = 0

        for _ in range(number_of_rounds):
            for length in lengths:
                sub_list = []

                for i in range(length):
                    index = (position + i) % self.LENGTH
                    sub_list.append(knot_list[index])
                sub_list.reverse()

                for i in range(length):
                    index = (position + i) % self.LENGTH
                    knot_list[index] = sub_list[i]

                position = (position + length + skip_size) % self.LENGTH
                skip_size += 1

    def part_1(self):
        lengths = [int(length) for length in self.inputs.strip().split(',')]

        knot_list = self.get_starting_list()
        self.process_rounds(knot_list, lengths)

        return knot_list[0] * knot_list[1]

    def part_2(self):
        lengths = [ord(char) for char in self.inputs.strip()]
        lengths.extend([17, 31, 73, 47, 23])

        knot_list = self.get_starting_list()

        self.process_rounds(knot_list, lengths, number_of_rounds=64)

        dense_hash = []
        for group in range(16):
            new_value = 0
            for sub_index in range(16):
                index = group * 16 + sub_index
                new_value = new_value ^ knot_list[index]

            hex_value = hex(new_value)[2:]
            dense_hash.append(f'{"0" if len(hex_value) == 1 else ""}{hex_value}')

        return ''.join(dense_hash)


if __name__ == "__main__":
    Year2017Day10().print_results()

from typing import Tuple

from solutions import BaseSolution


class Year2017Day15(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return int(line.strip().rsplit(' ', 1)[-1])

    def generator_a(self, value: int):
        return value * 16807 % 2147483647

    def generator_b(self, value: int):
        return value * 48271 % 2147483647

    def next_values(self, generators: Tuple[int, int]):
        return (
            self.generator_a(generators[0]),
            self.generator_b(generators[1])
        )

    def next_round(self, generators: Tuple[int, int]):
        values = []
        for _ in range(5):
            generators = self.next_values(generators)
            values.append(generators)
        return generators, values

    def part_1(self):
        generators = self.inputs

        mask = 2 ** 16 - 1
        matches = 0
        for _ in range(40000000):
            generators = self.next_values(generators)
            if generators[0] & mask == generators[1] & mask:
                matches += 1

        return matches

    def part_2(self):
        generator_a_value, generator_b_value = self.inputs

        NUMBER_OF_PAIRS = 5000000

        generator_a_values = []
        generator_b_values = []

        while len(generator_a_values) < NUMBER_OF_PAIRS:
            generator_a_value = self.generator_a(generator_a_value)
            if generator_a_value % 4 == 0:
                generator_a_values.append(generator_a_value)

        while len(generator_b_values) < NUMBER_OF_PAIRS:
            generator_b_value = self.generator_b(generator_b_value)
            if generator_b_value % 8 == 0:
                generator_b_values.append(generator_b_value)

        mask = 2 ** 16 - 1
        matches = 0
        for i in range(NUMBER_OF_PAIRS):
            if generator_a_values[i] & mask == generator_b_values[i] & mask:
                matches += 1

        return matches


if __name__ == "__main__":
    Year2017Day15().print_results()

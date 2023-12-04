import math

from solutions import BaseSolution


class Year2015Day20(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        target = self.inputs
        factor_map = {}

        def get_factors(number):
            if number not in factor_map:
                factor_map[number] = set()
                for i in range(math.floor(number**0.5)):
                    if number % (i + 1) == 0:
                        factor_map[number].add(i + 1)
                        factor_map[number].add(number / (i + 1))
            return factor_map[number]

        def calculate_presents(house):
            return sum(get_factors(house)) * 10

        house = 1
        while calculate_presents(house) < target:
            house += 1

        return house

    def part_2(self):
        target = self.inputs
        factor_map = {}
        elves = {}

        def get_factors(number):
            if number not in factor_map:
                factor_map[number] = set()
                for i in range(math.floor(number**0.5)):
                    if number % (i + 1) == 0:
                        for factor in [i + 1, number / (i + 1)]:
                            if factor in elves:
                                if elves[factor] < 50:
                                    elves[factor] += 1
                                    factor_map[number].add(factor)
                            else:
                                elves[factor] = 1
                                factor_map[number].add(factor)
            return factor_map[number]

        def calculate_presents(house):
            return sum(get_factors(house)) * 11

        house = 1
        while calculate_presents(house) < target:
            house += 1

        return house


if __name__ == "__main__":
    Year2015Day20().print_results()

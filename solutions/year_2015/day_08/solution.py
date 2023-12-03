import re

from solutions import BaseSolution


class Year2015Day08(BaseSolution):
    module_file = __file__

    def part_1(self):
        return sum(2 + len(re.findall(r'(\\\\|\\\")', input)) + 3 * len(re.findall(r'\\x[0-9a-f]{2}', input))
                for input in self.inputs)

    def part_2(self):
        return sum(2 + len(re.findall(r'(\\|\")', input)) for input in self.inputs)


if __name__ == "__main__":
    Year2015Day08().print_results()

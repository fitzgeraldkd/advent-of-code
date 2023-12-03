import json
import re

from solutions import BaseSolution


class Year2015Day12(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def sum_children(self, data):
        total = 0

        def read_child(child):
            if type(child) is int:
                return child
            elif type(child) is dict or type(child) is list:
                return self.sum_children(child)
            return 0

        if type(data) is dict:
            if any([value == "red" for value in data.values()]):
                return total

            for value in data.values():
                total += read_child(value)

        elif type(data) is list:
            for value in data:
                total += read_child(value)

        return total

    def part_1(self):
        numbers = re.findall(r"\-?\d+", self.inputs)
        total = sum([int(number) for number in numbers])

        return total

    def part_2(self):
        parsed_input = json.loads(self.inputs)
        return self.sum_children(parsed_input)


if __name__ == "__main__":
    Year2015Day12().print_results()

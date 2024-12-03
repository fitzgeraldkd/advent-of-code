import re
from solutions import BaseSolution


class Year2024Day03(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        inputs = super()._parse_inputs()
        return ''.join(inputs)


    def run_instructions(self, row: str, always_enabled=False):
        matches = re.findall(r'(mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\))', row)
        total = 0
        enabled = True

        for match in matches:
            if match == 'do()':
                enabled = True
            elif match == 'don\'t()':
                enabled = False
            elif enabled or always_enabled:
                values = re.findall(r'\d+', match)
                values = [int(v) for v in values]
                total += values[0] * values[1]

        return total


    def part_1(self):
        return self.run_instructions(self.inputs, always_enabled=True)


    def part_2(self):
        return self.run_instructions(self.inputs)


if __name__ == "__main__":
    Year2024Day03().print_results()

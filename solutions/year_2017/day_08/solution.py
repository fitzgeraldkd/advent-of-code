from collections import defaultdict
from solutions import BaseSolution


class Year2017Day08(BaseSolution):
    module_file = __file__

    def _parse_line(self, input: str):
        register, direction, amount, _, condition_a, comparator, condition_b = input.strip().split(' ')
        return {
            'register': register,
            'amount': int(amount) * (1 if direction == 'inc' else -1),
            'condition': {
                'arguments': [condition_a, int(condition_b)],
                'comparator': comparator
            }
        }

    def check_condition(self, registers, condition):
        comparator = condition['comparator']
        if comparator == '>':
            return registers[condition['arguments'][0]] > condition['arguments'][1]
        elif comparator == '<':
            return registers[condition['arguments'][0]] < condition['arguments'][1]
        elif comparator == '>=':
            return registers[condition['arguments'][0]] >= condition['arguments'][1]
        elif comparator == '<=':
            return registers[condition['arguments'][0]] <= condition['arguments'][1]
        elif comparator == '==':
            return registers[condition['arguments'][0]] == condition['arguments'][1]
        elif comparator == '!=':
            return registers[condition['arguments'][0]] != condition['arguments'][1]

    def part_1(self):
        commands = self.inputs

        registers = defaultdict(int)

        for command in commands:
            if self.check_condition(registers, command['condition']):
                registers[command['register']] += command['amount']

        return max(registers.values())

    def part_2(self):
        commands = self.inputs

        registers = defaultdict(int)
        highest_value = 0

        for command in commands:
            if self.check_condition(registers, command['condition']):
                registers[command['register']] += command['amount']
                highest_value = max(highest_value, registers[command['register']])

        return highest_value


if __name__ == "__main__":
    Year2017Day08().print_results()

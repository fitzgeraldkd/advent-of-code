from itertools import product
from solutions import BaseSolution


class Year2024Day07(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        target, values = line.strip().split(": ")
        return [int(target), [int(v) for v in values.split(" ")]]

    def can_validate(self, target, values):
        operator_count = len(values) - 1
        operator_combinations = product(["+", "*"], repeat=operator_count)

        # print(list(operator_combinations))
        for combination in operator_combinations:
            result, *remaining = values
            for operator in combination:
                operand, *remaining = remaining
                if operator == "+":
                    result += operand
                else:
                    result *= operand
                if result > target:
                    break
            if result == target:
                return True
        return False

    def can_validate_part_2(self, target, values):
        operator_count = len(values) - 1
        operator_combinations = product(["+", "*", "||"], repeat=operator_count)

        checked_combinations = set()

        for combination in operator_combinations:
            result, *remaining = values
            applied_operations = ""
            for operator in combination:
                applied_operations += operator
                if applied_operations in checked_combinations:
                    break
                operand, *remaining = remaining
                if operator == "+":
                    result += operand
                elif operator == "||":
                    result = int(f"{result}{operand}")
                else:
                    result *= operand
                if result > target:
                    checked_combinations.add(applied_operations)
                    break
            if result == target:
                return True
        return False


    def part_1(self):
        results = 0
        for target, values in self.inputs:
            if self.can_validate(target, values):
                results += target
        return results

    def part_2(self):
        results = 0
        for target, values in self.inputs:
            if self.can_validate_part_2(target, values):
                results += target
        return results


if __name__ == "__main__":
    Year2024Day07().print_results()

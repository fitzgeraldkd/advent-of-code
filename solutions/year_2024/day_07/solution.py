from solutions import BaseSolution

class Year2024Day07(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        target, values = line.strip().split(": ")
        return [int(target), [int(v) for v in values.split(" ")]]

    def check_operations(self, target, values, include_concat=False):
        operators = ["+", "*"]
        if include_concat:
            operators.append("||")

        for operator in operators:
            a, b, *remaining = values

            if operator == "+":
                total = a + b
            elif operator == "||":
                total = int(f"{a}{b}")
            else:
                total = a * b

            # Assumes there are no 0s in the values.
            if total > target:
                continue

            if len(remaining) == 0:
                if total == target:
                    return True
                else:
                    continue

            passed = self.check_operations(target, [total, *remaining], include_concat)
            if passed:
                return True

        return False

    def part_1(self):
        results = 0
        for target, values in self.inputs:
            if self.check_operations(target, values):
                results += target
        return results

    def part_2(self):
        results = 0
        for target, values in self.inputs:
            if self.check_operations(target, values, include_concat=True):
                results += target
        return results


if __name__ == "__main__":
    Year2024Day07().print_results()

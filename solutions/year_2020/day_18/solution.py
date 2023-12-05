import re

from solutions import BaseSolution


class Year2020Day18(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        expression = re.split(r"(\d+|\+|\*|\(|\))", line.strip().replace(" ", ""))
        nested_expression = []
        indeces = []

        for e in expression:
            if e == "":
                continue

            group = nested_expression
            for index in indeces:
                group = group[index]

            if e == "(":
                group.append([])
                indeces.append(len(group) - 1)
            elif e == ")":
                indeces.pop()
            else:
                try:
                    group.append(int(e))
                except ValueError:
                    group.append(e)

        return nested_expression

    def evaluate_part_1(self, expression: list):
        result = None
        operator = None

        for value in expression:
            if value == "+" or value == "*":
                operator = value
            else:
                parsed_value = value
                if isinstance(value, list):
                    parsed_value = self.evaluate_part_1(value)

                if operator == "+":
                    result += parsed_value
                elif operator == "*":
                    result *= parsed_value
                elif operator is None:
                    result = parsed_value

        return result

    def evaluate_part_2(self, expression: list):
        for i, value in enumerate(expression):
            if isinstance(value, list):
                expression[i] = self.evaluate_part_2(value)

        for i in range(len(expression)):
            if expression[i] == "+":
                expression[i + 1] += expression[i - 1]
                expression[i - 1] = 1
                expression[i] = "*"

        return self.evaluate_part_1(expression)

    def part_1(self):
        return sum(self.evaluate_part_1(expression) for expression in self.inputs)

    def part_2(self):
        return sum(self.evaluate_part_2(expression) for expression in self.inputs)


if __name__ == "__main__":
    Year2020Day18().print_results()

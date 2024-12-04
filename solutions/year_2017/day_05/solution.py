from solutions import BaseSolution


class Year2017Day05(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return int(super()._parse_line(line))

    def part_1(self):
        inputs = self.inputs
        index = 0
        steps = 0

        while index >= 0 and index < len(inputs):
            jump = inputs[index]
            inputs[index] += 1
            index += jump
            steps += 1

        return steps

    def part_2(self):
        inputs = self.inputs
        index = 0
        steps = 0

        while index >= 0 and index < len(inputs):
            jump = inputs[index]
            inputs[index] += 1 if jump < 3 else -1
            index += jump
            steps += 1

        return steps


if __name__ == "__main__":
    Year2017Day05().print_results()

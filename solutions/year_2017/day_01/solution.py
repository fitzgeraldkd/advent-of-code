from solutions import BaseSolution


class Year2017Day01(BaseSolution):
    module_file = __file__


    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        sequence = self.inputs
        sequence = f'{sequence}{sequence[0]}'
        total = 0
        for index in range(len(sequence) - 1):
            if sequence[index] == sequence[index + 1]:
                total += int(sequence[index])
        return total

    def part_2(self):
        sequence = self.inputs
        total = 0

        for index in range(len(sequence)):
            opposite_index = int(index + len(sequence) / 2) % len(sequence)
            if sequence[index] == sequence[opposite_index]:
                total += int(sequence[index])

        return total


if __name__ == "__main__":
    Year2017Day01().print_results()

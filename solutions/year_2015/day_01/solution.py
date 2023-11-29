from solutions import BaseSolution


class Year2015Day01(BaseSolution):
    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        current_floor = 0
        for direction in self.inputs:
            current_floor += 1 if direction == "(" else -1
        return current_floor

    def part_2(self):
        current_floor = 0
        for index, direction in enumerate(self.inputs):
            current_floor += 1 if direction == "(" else -1
            if current_floor < 0:
                return index + 1


if __name__ == "__main__":
    Year2015Day01(__file__).print_results()

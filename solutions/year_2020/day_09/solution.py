from solutions import BaseSolution


class Year2020Day09(BaseSolution):
    PREAMBLE = 25
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def part_1(self):
        xmas = self.inputs
        for i in range(self.PREAMBLE, len(xmas)):
            target = xmas[i]
            sub_xmas = xmas[i - self.PREAMBLE : i]
            values = set(sub_xmas)
            value = next((value for value in values if target - value in values), None)
            if not value or (value * 2 == target and sub_xmas.count(value) == 1):
                return target

    def part_2(self):
        xmas = self.inputs
        target = self.part_1()
        start, end = 0, 1

        while True:
            sub_xmas = xmas[start:end]
            aggregate = sum(sub_xmas)
            if aggregate < target:
                end += 1
            elif aggregate > target:
                start += 1
            else:
                return min(sub_xmas) + max(sub_xmas)


if __name__ == "__main__":
    Year2020Day09().print_results()

from solutions import BaseSolution


class Year2018Day01(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def part_1(self):
        return sum(self.inputs)

    def part_2(self):
        changes = self.inputs

        frequency = 0
        previous = {0}
        index = 0

        while True:
            frequency += changes[index]
            if frequency in previous:
                return frequency
            else:
                previous.add(frequency)
            index = (index + 1) % len(changes)


if __name__ == "__main__":
    Year2018Day01().print_results()

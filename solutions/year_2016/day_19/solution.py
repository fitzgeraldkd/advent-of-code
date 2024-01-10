from solutions import BaseSolution


class Year2016Day19(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        elves = list(range(self.inputs))

        while len(elves) > 1:
            start = 0 if len(elves) % 2 == 0 else 2
            elves = elves[start::2]

        return elves[0] + 1

    def part_2(self):
        elves = list(range(self.inputs))

        index = len(elves) // 2
        while len(elves) > 1:
            elves.pop(index)
            if len(elves) % 2 == 0:
                index += 1
            index = index % len(elves)

        return elves[0] + 1


if __name__ == "__main__":
    Year2016Day19().print_results()

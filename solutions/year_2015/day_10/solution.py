from solutions import BaseSolution


class Year2015Day10(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def look_and_say(self, input: str):
        count = 0
        previous = None
        output = ""

        for char in input:
            if previous is None or char == previous:
                previous = char
                count += 1
            else:
                output += str(count) + previous
                previous = char
                count = 1

        output += str(count) + previous

        return output

    def part_1(self):
        result = self.inputs
        for _ in range(40):
            result = self.look_and_say(result)
        return len(result)

    def part_2(self):
        result = self.inputs
        for _ in range(50):
            result = self.look_and_say(result)
        return len(result)


if __name__ == "__main__":
    Year2015Day10().print_results()

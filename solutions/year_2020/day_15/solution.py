from solutions import BaseSolution


class Year2020Day15(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return [int(value) for value in line.strip().split(",")]

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_nth_number(self, n: int):
        start_numbers = self.inputs
        last_number = start_numbers[-1]
        last_index_map = {value: i + 1 for i, value in enumerate(start_numbers[:-1])}

        for i in range(len(start_numbers), n):
            new_number = (
                i - last_index_map[last_number] if last_number in last_index_map else 0
            )
            last_index_map[last_number] = i
            last_number = new_number

        return last_number

    def part_1(self):
        return self.get_nth_number(2020)

    def part_2(self):
        return self.get_nth_number(30000000)


if __name__ == "__main__":
    Year2020Day15().print_results()

from solutions import BaseSolution


class Year2015Day02(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return [int(dimension) for dimension in line.strip().split("x")]

    def part_1(self):
        total_area = 0

        for l, w, h in self.inputs:
            area = 2 * l * w + 2 * w * h + 2 * h * l
            slack = int(l * w * h / max(l, w, h))
            total_area += area + slack

        return total_area

    def part_2(self):
        total_length = 0

        for l, w, h in self.inputs:
            ribbon = 2 * (l + w + h - max(l, w, h))
            bow = l * w * h
            total_length += ribbon + bow

        return total_length


if __name__ == "__main__":
    Year2015Day02().print_results()

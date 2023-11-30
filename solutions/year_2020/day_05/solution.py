from solutions import BaseSolution


def binary_search(min: int, max: int, characters: str):
    amount_to_reduce = int((1 + max - min) / 2)
    if characters[0] in {"F", "L"}:
        max -= amount_to_reduce
    else:
        min += amount_to_reduce

    if len(characters) > 1:
        return binary_search(min, max, characters[1:])
    else:
        return min


class Year2020Day05(BaseSolution):
    def _parse_line(self, line: str):
        row = binary_search(0, 127, line[:7])
        col = binary_search(0, 7, line[7:])
        return row * 8 + col

    def part_1(self):
        return max(self.inputs)

    def part_2(self):
        sorted_seats = sorted(self.inputs)

        for i, id in enumerate(sorted_seats):
            if (sorted_seats[i + 1] - id) > 1:
                return id + 1
        return None


if __name__ == "__main__":
    Year2020Day05(__file__).print_results()

import re

from solutions import BaseSolution


class Year2023Day04(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        _, numbers = line.strip().split(": ")
        winning_numbers, card_numbers = [
            {int(v) for v in re.findall(r"\d+", n)} for n in numbers.split(" | ")
        ]
        return len(winning_numbers.intersection(card_numbers))

    def part_1(self):
        return sum(0 if wins == 0 else (2 ** (wins - 1)) for wins in self.inputs)

    def part_2(self):
        cards = self.inputs
        card_counts = [1 for _ in range(len(cards))]

        for i, wins in enumerate(cards):
            for j in range(i + 1, i + 1 + wins):
                card_counts[j] += card_counts[i]

        return sum(card_counts)


if __name__ == "__main__":
    Year2023Day04().print_results()

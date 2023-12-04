import re
from typing import Set

from solutions import BaseSolution


class Year2023Day04(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        _, numbers = line.strip().split(": ")
        winning_numbers, card_numbers = numbers.split(" | ")
        return (
            {int(n) for n in re.findall(r"\d+", winning_numbers)},
            {int(n) for n in re.findall(r"\d+", card_numbers)},
        )

    def get_card_wins(self, winning_numbers: Set[int], card_numbers: Set[int]) -> int:
        return len(winning_numbers.intersection(card_numbers))

    def part_1(self):
        score = 0

        for winning_numbers, card_numbers in self.inputs:
            card_wins = self.get_card_wins(winning_numbers, card_numbers)
            if card_wins > 0:
                score += 2 ** (card_wins - 1)

        return score

    def part_2(self):
        cards = self.inputs
        card_counts = [1 for _ in range(len(cards))]

        for i, (winning_numbers, card_numbers) in enumerate(cards):
            card_wins = self.get_card_wins(winning_numbers, card_numbers)

            if card_counts[i] == 1 and card_counts == 0:
                break

            for j in range(i + 1, i + 1 + card_wins):
                card_counts[j] += card_counts[i]

        return sum(card_counts)


if __name__ == "__main__":
    Year2023Day04().print_results()

from typing import List
from solutions import BaseSolution


MAX_COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class Year2023Day02(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        game_id, rounds = line.strip().split(": ")
        rounds = [
            [marbles.split(" ") for marbles in round.split(", ")]
            for round in rounds.split("; ")
        ]
        for round in rounds:
            for marble in round:
                marble[0] = int(marble[0])

        return int(game_id.split(" ")[-1]), rounds

    def part_1(self):
        id_sum = 0

        for id, game in self.inputs:
            if not any(
                any(count > MAX_COLORS[color] for count, color in round)
                for round in game
            ):
                id_sum += id

        return id_sum

    def part_2(self):
        product_total = 0
        for _, game in self.inputs:
            marbles = {"red": 0, "green": 0, "blue": 0}
            for round in game:
                for count, color in round:
                    marbles[color] = max(marbles[color], int(count))

            product_total += marbles["red"] * marbles["green"] * marbles["blue"]

        return product_total


if __name__ == "__main__":
    Year2023Day02().print_results()

from collections import Counter
from solutions import BaseSolution

CARD_TO_VALUE = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

CARD_TO_VALUE_PART_2 = {**CARD_TO_VALUE, "J": 0}


class Year2023Day07(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        split_line = line.strip().split(" ")
        return {
            "hand": split_line[0],
            "bid": int(split_line[1]),
            "type": None,
            "part_1_sort": [CARD_TO_VALUE[card] for card in split_line[0]],
            "part_2_sort": [CARD_TO_VALUE_PART_2[card] for card in split_line[0]],
        }

    def part_1(self):
        rounds = self.inputs

        for round in rounds:
            counted = Counter(round["hand"])

            for _, this_count in counted.most_common():
                if this_count == 5:
                    round["type"] = 6
                elif this_count == 4:
                    round["type"] = 5
                elif this_count == 3:
                    round["type"] = 3
                elif this_count == 2:
                    if round["type"] == 3:
                        round["type"] = 4
                    elif round["type"] == 1:
                        round["type"] = 2
                    else:
                        round["type"] = 1
                elif round["type"] is None:
                    round["type"] = 0

        rounds.sort(key=lambda round: (round["type"], round["part_1_sort"]))
        return sum([(i + 1) * round["bid"] for i, round in enumerate(rounds)])

    def part_2(self):
        rounds = self.inputs

        for round in rounds:
            counted = Counter(round["hand"])
            joker_count = counted["J"]
            if joker_count == 5:
                round["type"] = 6
                continue
            del counted["J"]

            first = True
            for _, count in counted.most_common():
                this_count = count + joker_count if first else count
                joker_count = 0

                if this_count == 5:
                    round["type"] = 6
                elif this_count == 4:
                    round["type"] = 5
                elif this_count == 3:
                    round["type"] = 3
                elif this_count == 2:
                    if round["type"] == 3:
                        round["type"] = 4
                    elif round["type"] == 1:
                        round["type"] = 2
                    else:
                        round["type"] = 1
                elif round["type"] is None:
                    round["type"] = 0

        rounds.sort(key=lambda round: (round["type"], round["part_2_sort"]))
        return sum([(i + 1) * round["bid"] for i, round in enumerate(rounds)])


if __name__ == "__main__":
    Year2023Day07().print_results()

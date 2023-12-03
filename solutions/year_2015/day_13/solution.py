import itertools
import re

from solutions import BaseSolution


class Year2015Day13(BaseSolution):
    module_file = __file__

    def get_happiness_map(self, inputs):
        happiness_map = {}

        for input in inputs:
            guest = input.split(" ")[0]

            if guest not in happiness_map.keys():
                happiness_map[guest] = {}

            neighbor = input.split(" ")[-1][:-1]
            value = int(re.search(r"\d+", input)[0]) * (1 if "gain" in input else -1)
            happiness_map[guest][neighbor] = value

        return happiness_map

    def get_delta_happiness(self, happiness_map, arrangement, is_round=True):
        happiness = 0

        for index, guest in enumerate(arrangement):
            if index == 0:
                happiness += (
                    happiness_map[guest][arrangement[len(arrangement) - 1]]
                    if is_round
                    else 0
                )
                happiness += happiness_map[guest][arrangement[index + 1]]
            elif index == len(arrangement) - 1:
                happiness += happiness_map[guest][arrangement[index - 1]]
                happiness += happiness_map[guest][arrangement[0]] if is_round else 0
            else:
                happiness += happiness_map[guest][arrangement[index - 1]]
                happiness += happiness_map[guest][arrangement[index + 1]]

        return happiness

    def part_1(self):
        happiness_map = self.get_happiness_map(self.inputs)
        guests = happiness_map.keys()
        arrangements = itertools.permutations(guests)
        happinesses = [
            self.get_delta_happiness(happiness_map, arrangement)
            for arrangement in arrangements
        ]

        return max(happinesses)

    def part_2(self):
        happiness_map = self.get_happiness_map(self.inputs)
        guests = happiness_map.keys()
        arrangements = itertools.permutations(guests)
        happinesses = [
            self.get_delta_happiness(happiness_map, arrangement, is_round=False)
            for arrangement in arrangements
        ]

        return max(happinesses)


if __name__ == "__main__":
    Year2015Day13().print_results()

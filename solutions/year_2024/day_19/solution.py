from collections import defaultdict
import re
from solutions import BaseSolution


class Year2024Day19(BaseSolution):
    module_file = __file__
    group_delimiter = "\n"

    def _parse_inputs(self):
        towels, patterns = super()._parse_inputs()
        towels = towels[0].split(", ")
        return towels, patterns

    def get_combinations(self, towels_by_initial, pattern: str, points_lookup: dict):
        towels_by_length = towels_by_initial[pattern[0]]
        combinations = 0

        if pattern in points_lookup:
            return points_lookup[pattern]

        for length, towels in towels_by_length.items():
            if length > len(pattern):
                break
            if pattern[:length] in towels:
                if length == len(pattern):
                    combinations += 1
                else:
                    combinations += self.get_combinations(
                        towels_by_initial,
                        pattern[length:],
                        points_lookup
                    )

        points_lookup[pattern] = combinations
        return combinations

    def part_1(self):
        towels, patterns = self.inputs
        regex_pattern = fr'^({r"|".join(towels)})+$'

        results = 0
        for pattern in patterns:
            if re.match(regex_pattern, pattern):
                results += 1
        return results

    def part_2(self):
        towels, patterns = self.inputs
        towels = sorted(towels, key=lambda towel: (len(towel), towel))
        towels_by_initial = defaultdict(lambda: defaultdict(set))
        for towel in towels:
            towels_by_initial[towel[0]][len(towel)].add(towel)

        points_lookup = {}
        results = 0
        for pattern in patterns:
            results += self.get_combinations(towels_by_initial, pattern, points_lookup)
        return results


if __name__ == "__main__":
    Year2024Day19().print_results()

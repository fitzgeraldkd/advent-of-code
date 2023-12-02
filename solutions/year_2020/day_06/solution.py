from collections import defaultdict

from solutions import BaseSolution


class Year2020Day06(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_group(self, lines):
        affirmatives = defaultdict(int)
        for line in lines:
            for question in line.strip():
                affirmatives[question] += 1
        return affirmatives, len(lines)

    def part_1(self):
        return sum([len(affirmatives.keys()) for affirmatives, _ in self.inputs])

    def part_2(self):
        return sum(
            [
                len([q for q in affirmatives.keys() if affirmatives[q] == size])
                for affirmatives, size in self.inputs
            ]
        )


if __name__ == "__main__":
    Year2020Day06().print_results()

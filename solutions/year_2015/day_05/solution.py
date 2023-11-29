import re

from solutions import BaseSolution


class Year2015Day05(BaseSolution):
    def part_1(self):
        nice_string_count = 0

        for string in self.inputs:
            if re.search(r"(ab|cd|pq|xy)", string):
                continue
            if len(re.findall(r"[aeiou]", string)) < 3:
                continue
            if re.search(r"([a-z])\1", string) is None:
                continue

            nice_string_count += 1

        return nice_string_count

    def part_2(self):
        nice_string_count = 0
        for string in self.inputs:
            has_two_pairs = False
            for index in range(len(string) - 3):
                pair = string[index : index + 2]
                if re.search(pair, string[index + 2 :]):
                    has_two_pairs = True
                    break
            if not has_two_pairs:
                continue

            if re.search(r"([a-z])[a-z]\1", string) is None:
                continue

            nice_string_count += 1

        return nice_string_count


if __name__ == "__main__":
    Year2015Day05(__file__).print_results()

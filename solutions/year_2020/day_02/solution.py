from collections import Counter

from solutions import BaseSolution


class Year2020Day02(BaseSolution):
    def _parse_line(self, line: str):
        args, char, password = line.strip().split(" ")
        arg_a, arg_b = [int(arg) for arg in args.split("-")]
        return arg_a, arg_b, char[0], password

    def part_1(self):
        valid_password_count = 0

        for min_count, max_count, char, password in self.inputs:
            if min_count <= Counter(password)[char] <= max_count:
                valid_password_count += 1

        return valid_password_count

    def part_2(self):
        valid_password_count = 0

        for index_a, index_b, char, password in self.inputs:
            if (password[index_a - 1] == char) != (password[index_b - 1] == char):
                valid_password_count += 1

        return valid_password_count


if __name__ == "__main__":
    Year2020Day02(__file__).print_results()

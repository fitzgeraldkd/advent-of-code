from solutions import BaseSolution

TEXT_TO_INT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}


class Year2023Day01(BaseSolution):
    def part_1(self):
        total = 0

        for line in self.inputs:
            filtered_line = "".join([char for char in line if char in "1234567890"])
            total += int(filtered_line[0] + filtered_line[-1])

        return total

    def part_2(self):
        total = 0

        for line in self.inputs:
            first_digit = None
            last_digit = None
            for key, value in TEXT_TO_INT.items():
                first_index = line.find(key)
                if first_index != -1 and (
                    first_digit is None or first_digit[0] > first_index
                ):
                    first_digit = (first_index, value)

                last_index = line.rfind(key)
                if last_index != -1 and (
                    last_digit is None or last_digit[0] < last_index
                ):
                    last_digit = (last_index, value)

            total += first_digit[1] * 10 + last_digit[1]

        return total


if __name__ == "__main__":
    Year2023Day01(__file__).print_results()

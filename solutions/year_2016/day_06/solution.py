import math

from solutions import BaseSolution


class Year2016Day06(BaseSolution):
    module_file = __file__

    def part_1(self):
        inputs = self.inputs

        letter_counts = [{} for _ in range(len(inputs[0]))]

        for input in inputs:
            for index, letter in enumerate(input):
                if letter in letter_counts[index]:
                    letter_counts[index][letter] += 1
                else:
                    letter_counts[index][letter] = 1

        message = []
        for letter_count in letter_counts:
            next_letter = None
            count = 0
            for letter in letter_count:
                if letter_count[letter] > count:
                    next_letter = letter
                    count = letter_count[letter]
            message.append(next_letter)

        return "".join(message)

    def part_2(self):
        inputs = self.inputs

        letter_counts = [{} for _ in range(len(inputs[0]))]

        for input in inputs:
            for index, letter in enumerate(input):
                if letter in letter_counts[index]:
                    letter_counts[index][letter] += 1
                else:
                    letter_counts[index][letter] = 1

        message = []
        for letter_count in letter_counts:
            next_letter = None
            count = math.inf
            for letter in letter_count:
                if letter_count[letter] < count:
                    next_letter = letter
                    count = letter_count[letter]
            message.append(next_letter)

        return "".join(message)


if __name__ == "__main__":
    Year2016Day06().print_results()

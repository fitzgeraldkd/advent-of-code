import re

from solutions import BaseSolution


class Year2015Day11(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def replace_illegal_characters(self, input):
        output = re.sub("i", "j", input)
        output = re.sub("l", "m", output)
        output = re.sub("o", "p", output)
        return output

    def increment_character(self, input):
        output = chr((ord(input) - ord("a") + 1) % 26 + ord("a"))
        output = self.replace_illegal_characters(output)
        return (output, output == "a")

    def increment_password(self, password):
        password_list = list(password)
        index = len(password_list) - 1
        while index >= 0:
            new_character, wrapped = self.increment_character(password_list[index])
            password_list[index] = new_character
            index -= 1
            if not wrapped:
                break
        return "".join(password_list)

    def passes_rules(self, input):
        if re.search(r"[ilo]", input):
            return False

        if len(set(re.findall(r"([a-z])\1", input))) < 2:
            return False

        previous_char = input[0]
        streak = 0
        for char in input[1:]:
            if ord(char) - ord(previous_char) == 1:
                streak += 1
            else:
                streak = 0

            if streak == 2:
                return True

            previous_char = char

        return False

    def part_1(self):
        password = self.increment_password(self.inputs)

        while not self.passes_rules(password):
            password = self.increment_password(password)

        return password

    def part_2(self):
        password = self.increment_password(self.part_1())

        while not self.passes_rules(password):
            password = self.increment_password(password)

        return password


if __name__ == "__main__":
    Year2015Day11().print_results()

from solutions import BaseSolution


class Year2016Day21(BaseSolution):
    module_file = __file__

    def swap_positions(self, password: list, x: int, y: int):
        password[x], password[y] = password[y], password[x]

    def swap_letters(self, password: list, x: str, y: str):
        for index, letter in enumerate(password):
            if letter == x:
                password[index] = y
            elif letter == y:
                password[index] = x

    def rotate(self, password: list, amount: int):
        # Positive rotates to the right.
        amount = -1 * amount
        return [*password[amount:], *password[:amount]]

    def reverse(self, password: list, x: int, y: int):
        reversed = password[x : y + 1]
        reversed.reverse()
        for i in range(x, y + 1):
            password[i] = reversed[i - x]

    def move(self, password: list, x: int, y: int):
        letter = password.pop(x)
        password.insert(y, letter)

    def parse_operation(self, operation: str, password: list, reversed=False):
        parts = operation.split(" ")
        if parts[0] == "swap":
            if parts[1] == "position":
                self.swap_positions(password, int(parts[2]), int(parts[5]))
            else:
                self.swap_letters(password, parts[2], parts[5])
        elif parts[0] == "rotate":
            if parts[1] in ["left", "right"]:
                rotations = (int(parts[2]) % len(password)) * (-1 if reversed else 1)
                password = self.rotate(
                    password, rotations * (1 if parts[1] == "right" else -1)
                )
            else:
                index = password.index(parts[6])
                if reversed:
                    original = [*password]
                    while original != self.parse_operation(operation, password):
                        password = self.rotate(password, 1)
                else:
                    rotations = (1 + index + (1 if index >= 4 else 0)) % len(password)
                    password = self.rotate(password, rotations)
        elif parts[0] == "reverse":
            self.reverse(password, int(parts[2]), int(parts[4]))
        elif parts[0] == "move":
            x, y = int(parts[2]), int(parts[5])
            if reversed:
                x, y = y, x
            self.move(password, x, y)

        return password

    def part_1(self, unscrambled="abcdefgh"):
        operations = self.inputs
        password = list(unscrambled)

        for operation in operations:
            password = self.parse_operation(operation, password)

        return "".join(password)

    def part_2(self, scrambled="fbgdceah"):
        operations = self.inputs
        operations.reverse()
        password = list(scrambled)

        for operation in operations:
            password = self.parse_operation(operation, password, reversed=True)

        return "".join(password)


if __name__ == "__main__":
    Year2016Day21().print_results()

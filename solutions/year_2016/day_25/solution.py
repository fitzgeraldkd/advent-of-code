from solutions import BaseSolution


class Interpreter:
    def __init__(self, instructions: list, initial: int):
        self.registers = {"a": initial, "b": 0, "c": 0, "d": 0}
        self.instructions = []
        for instruction in instructions:
            command, arguments = instruction.split(" ", 1)
            arguments = [
                arg if arg in "abcd" else int(arg) for arg in arguments.split(" ")
            ]
            self.instructions.append(
                {"command": command, "arguments": arguments, "toggled": False}
            )
        self.index = 0
        self.sequence = []
        self.failed = False

    def copy(self, x, y):
        if y in self.registers:
            self.registers[y] = self.registers.get(x, x)
        self.index += 1

    def increment(self, x):
        self.registers[x] += 1
        self.index += 1

    def decrement(self, x):
        self.registers[x] -= 1
        self.index += 1

    def jump_if_not_zero(self, x, y):
        if self.registers.get(x, x) != 0:
            self.index += self.registers.get(y, y)
        else:
            self.index += 1

    def out(self, x):
        value = self.registers.get(x, x)
        if len(self.sequence) == 0 and value == 0:
            self.sequence.append(value)
        elif len(self.sequence) > 0:
            if value in [0, 1] and value != self.sequence[-1]:
                self.sequence.append(value)
            else:
                self.failed = True
        else:
            self.failed = True
        self.index += 1

    def run_command(self):
        COMMANDS = {
            "cpy": self.copy,
            "inc": self.increment,
            "dec": self.decrement,
            "jnz": self.jump_if_not_zero,
            "out": self.out,
        }
        instruction = self.instructions[self.index]
        COMMANDS[instruction["command"]](*instruction["arguments"])

    def execute(self):
        while (
            not self.failed
            and self.index < len(self.instructions)
            and len(self.sequence) < 1000
        ):
            self.run_command()
        return self.sequence == [i % 2 for i in range(1000)]
        return self.registers["a"]


class Year2016Day25(BaseSolution):
    module_file = __file__

    def part_1(self):
        instructions = self.inputs
        initial = 196
        while True:
            interpreter = Interpreter(instructions, initial)
            success = interpreter.execute()
            if success:
                return initial
            else:
                initial += 1

    def part_2(self):
        return None


if __name__ == "__main__":
    Year2016Day25().print_results()

from solutions import BaseSolution


class Year2015Day23(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        action, arguments = line.strip().split(" ", 1)
        return action, arguments.split(", ")

    def get_actions(self):
        def _parse_offset(offset):
            return int(offset[1:]) if offset[0] == "+" else -1 * int(offset[1:])

        def half(registers, arguments):
            registers[arguments[0]] = int(registers[arguments[0]] / 2)
            return 1

        def triple(registers, arguments):
            registers[arguments[0]] *= 3
            return 1

        def increment(registers, arguments):
            registers[arguments[0]] += 1
            return 1

        def jump(registers, arguments):
            return _parse_offset(arguments[0])

        def jump_if_even(registers, arguments):
            if registers[arguments[0]] % 2 == 0:
                return _parse_offset(arguments[1])
            else:
                return 1

        def jump_if_one(registers, arguments):
            if registers[arguments[0]] == 1:
                return _parse_offset(arguments[1])
            else:
                return 1

        return {
            "hlf": half,
            "tpl": triple,
            "inc": increment,
            "jmp": jump,
            "jie": jump_if_even,
            "jio": jump_if_one,
        }

    def part_1(self):
        inputs = self.inputs
        actions = self.get_actions()

        registers = {"a": 0, "b": 0}
        index = 0
        while index < len(inputs):
            action, arguments = inputs[index]
            index += actions[action](registers, arguments)

        return registers["b"]

    def part_2(self):
        inputs = self.inputs
        actions = self.get_actions()

        registers = {"a": 1, "b": 0}
        index = 0
        while index < len(inputs):
            action, arguments = inputs[index]
            index += actions[action](registers, arguments)

        return registers["b"]


if __name__ == "__main__":
    Year2015Day23().print_results()

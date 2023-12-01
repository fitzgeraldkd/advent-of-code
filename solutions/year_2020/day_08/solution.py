from copy import deepcopy

from solutions import BaseSolution


def run_program(commands):
    accumulator = 0
    index = 0
    visited_indeces = set()
    completed = False

    while index not in visited_indeces:
        visited_indeces.add(index)
        command, value = commands[index]

        if command == "acc":
            accumulator += value

        if index == len(commands) - 1:
            completed = True
            break
        elif command == "jmp":
            index += value
        else:
            index += 1

    return accumulator, completed


class Year2020Day08(BaseSolution):
    def _parse_line(self, line: str):
        command, value = line.strip().split(" ")
        return [command, int(value)]

    def part_1(self):
        commands = self.inputs
        return run_program(commands)[0]

    def part_2(self):
        commands = self.inputs

        for i, corrupt_command in enumerate(commands):
            fixed_commands = deepcopy(commands)
            if (
                corrupt_command[0] == "nop"
                and corrupt_command[1] != 0
                and (0 <= corrupt_command[1] + i < len(fixed_commands))
            ):
                fixed_commands[i][0] = "jmp"
            elif corrupt_command[0] == "jmp":
                fixed_commands[i][0] = "nop"
            else:
                continue

            accumulator, completed = run_program(fixed_commands)
            if completed:
                return accumulator


if __name__ == "__main__":
    Year2020Day08(__file__).print_results()

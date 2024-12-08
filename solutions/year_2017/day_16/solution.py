from typing import List

from solutions import BaseSolution


class Year2017Day16(BaseSolution):
    module_file = __file__
    STARTING_LINE = 'abcdefghijklmnop'

    def _parse_line(self, line):
        return super()._parse_line(line).split(",")

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def move(self, line: List[str], instruction: str):
        if instruction[0] == 's':
            amount = -1 * int(instruction[1:])
            return line[amount:] + line[:amount]
        elif instruction[0] == 'x':
            a, b = [int(position) for position in instruction[1:].split('/')]
            # line[a], line[b] = line[a], line[b]
        elif instruction[0] == 'p':
            a, b = instruction[1:].split('/')
            a = line.index(a)
            b = line.index(b)
        line[a], line[b] = line[b], line[a]
        return line

    def part_1(self):
        instructions = self.inputs

        line = list(self.STARTING_LINE)
        for instruction in instructions:
            line = self.move(line, instruction)

        return ''.join(line)

    def part_2(self):
        instructions = self.inputs

        line = list(self.STARTING_LINE)
        checked_lines = { ''.join(line): 0 }

        number_of_dances = 1000000000

        current_dance_number = 0
        is_last_cycle = False
        while current_dance_number < number_of_dances:
            for instruction in instructions:
                line = self.move(line, instruction)
            line_string = ''.join(line)
            current_dance_number += 1

            if not is_last_cycle:
                if line_string in checked_lines:
                    first_occurrence = checked_lines[line_string]
                    cycle_length = current_dance_number - first_occurrence
                    cycles_to_skip = (number_of_dances - current_dance_number) // cycle_length
                    current_dance_number += (cycle_length * cycles_to_skip)
                    is_last_cycle = True
                else:
                    checked_lines[line_string] = current_dance_number

        return ''.join(line)


if __name__ == "__main__":
    Year2017Day16().print_results()

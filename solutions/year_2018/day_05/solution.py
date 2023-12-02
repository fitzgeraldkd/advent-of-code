from solutions import BaseSolution


def react(polymer: str):
    remaining_units = []

    for char in polymer:
        if char.swapcase() == (remaining_units[-1] if remaining_units else None):
            remaining_units.pop()
        else:
            remaining_units.append(char)

    return remaining_units


class Year2018Day05(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        polymer = self.inputs
        return len(react(polymer))

    def part_2(self):
        polymer = "".join(react(self.inputs))

        units = set(polymer.lower())

        shortest_length = len(polymer)
        for unit in units:
            trimmed_polymer = polymer.replace(unit, "").replace(unit.upper(), "")
            shortest_length = min(shortest_length, len(react(trimmed_polymer)))

        return shortest_length


if __name__ == "__main__":
    Year2018Day05().print_results()

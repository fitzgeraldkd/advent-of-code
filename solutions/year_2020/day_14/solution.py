import re

from solutions import BaseSolution


class Year2020Day14(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        operation, value = line.strip().split(" = ")
        address = re.search(r"\d+", operation)
        if address:
            return int(address.group()), int(value)
        else:
            return None, value

    def part_1(self):
        memory = {}
        or_mask, and_mask = None, None

        for address, value in self.inputs:
            if address is None:
                or_mask = int("".join("1" if char == "1" else "0" for char in value), 2)
                and_mask = int(
                    "".join("0" if char == "0" else "1" for char in value), 2
                )
            else:
                memory[address] = (value | or_mask) & and_mask

        return sum(memory.values())

    def part_2(self):
        memory = {}
        float_adders = []
        or_mask, and_mask = None, None

        for address, value in self.inputs:
            if address is None:
                or_mask = int("".join("1" if char == "1" else "0" for char in value), 2)
                and_mask = int(
                    "".join("0" if char == "X" else "1" for char in value), 2
                )
                float_adders = [0]
                for i, char in enumerate(value):
                    if char == "X":
                        float_adders.extend(
                            [
                                adder + 2 ** (len(value) - i - 1)
                                for adder in float_adders
                            ]
                        )
            else:
                decoded_address = (address | or_mask) & and_mask
                for float_adder in float_adders:
                    memory[decoded_address + float_adder] = value

        return sum(memory.values())


if __name__ == "__main__":
    Year2020Day14().print_results()

from solutions import BaseSolution


class Year2016Day12(BaseSolution):
    module_file = __file__

    def part_1(self):
        instructions = self.inputs

        registers = {"a": 0, "b": 0, "c": 0, "d": 0}

        index = 0
        while index < len(instructions):
            instruction = instructions[index]
            if instruction.startswith("cpy"):
                _, src, rec = instruction.split(" ")
                registers[rec] = registers[src] if src in registers else int(src)
            elif instruction.startswith("inc"):
                registers[instruction[-1]] += 1
            elif instruction.startswith("dec"):
                registers[instruction[-1]] -= 1
            elif instruction.startswith("jnz"):
                _, val, amt = instruction.split(" ")
                val = registers[val] if val in registers else int(val)
                if val != 0:
                    index += int(amt)
                    continue
            index += 1

        return registers["a"]

    def part_2(self):
        instructions = self.inputs

        registers = {"a": 0, "b": 0, "c": 1, "d": 0}

        index = 0
        while index < len(instructions):
            instruction = instructions[index]
            if instruction.startswith("cpy"):
                _, src, rec = instruction.split(" ")
                registers[rec] = registers[src] if src in registers else int(src)
            elif instruction.startswith("inc"):
                registers[instruction[-1]] += 1
            elif instruction.startswith("dec"):
                registers[instruction[-1]] -= 1
            elif instruction.startswith("jnz"):
                _, val, amt = instruction.split(" ")
                val = registers[val] if val in registers else int(val)
                if val != 0:
                    index += int(amt)
                    continue
            index += 1

        return registers["a"]


if __name__ == "__main__":
    Year2016Day12().print_results()

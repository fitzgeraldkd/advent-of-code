from solutions import BaseSolution


class Year2024Day25(BaseSolution):
    module_file = __file__
    group_delimiter = "\n"

    def _parse_inputs(self):
        groups = super()._parse_inputs()
        locks = []
        keys = []
        for schematic in groups:
            height = len(schematic)
            width = len(schematic[0])
            if schematic[0][0] == ".":
                # Key
                key = [
                    next(height - y - 1 for y in range(height) if schematic[y][x] == "#")
                    for x in range(width)
                ]
                keys.append(key)
            else:
                # Lock
                lock = [
                    next(y - 1 for y in range(height) if schematic[y][x] == ".")
                    for x in range(width)
                ]
                locks.append(lock)
        return locks, keys

    def part_1(self):
        locks, keys = self.inputs
        results = 0

        for lock in locks:
            for key in keys:
                if all(lock[x] + key[x] <= 5 for x in range(len(lock))):
                    results += 1

        return results

    def part_2(self):
        return None


if __name__ == "__main__":
    Year2024Day25().print_results()

import re

import numpy as np

from solutions import BaseSolution


class Year2016Day15(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        row, num_positions, _, start = [int(x) for x in re.findall(r"\d+", line)]
        return {"row": row, "num_positions": num_positions, "start": start}

    def is_clear(self, disc: dict, time: int):
        return (time + disc["row"] + disc["start"]) % disc["num_positions"] == 0

    def get_increment(self, discs, time):
        positions = []
        for disc in discs:
            if self.is_clear(disc, time):
                positions.append(disc["num_positions"])
        return np.lcm.reduce(positions)

    def part_1(self):
        discs = self.inputs

        time = 0
        while any([not self.is_clear(disc, time) for disc in discs]):
            time += self.get_increment(discs, time)

        return time

    def part_2(self):
        discs = self.inputs
        discs.append({"row": len(discs) + 1, "num_positions": 11, "start": 0})

        time = 0
        while any([not self.is_clear(disc, time) for disc in discs]):
            time += self.get_increment(discs, time)

        return time


if __name__ == "__main__":
    Year2016Day15().print_results()

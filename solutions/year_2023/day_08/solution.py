import re
from typing import Set

import numpy as np

from solutions import BaseSolution


class Year2023Day08(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_inputs(self):
        steps, network = super()._parse_inputs()
        parsed_network = {}
        for connection in network:
            source, left, right = re.findall(r"[A-Z0-9]+", connection)
            parsed_network[source] = [left, right]
        return steps[0], parsed_network

    def count_steps(self, current: str, targets: Set[str]):
        count = 0
        steps, network = self.inputs
        while current not in targets:
            direction = steps[count % len(steps)]
            current = network[current][0 if direction == "L" else 1]
            count += 1
        return count

    def part_1(self):
        return self.count_steps("AAA", {"ZZZ"})

    def part_2(self):
        _, network = self.inputs
        starts = [node for node in network.keys() if node.endswith("A")]
        targets = {node for node in network.keys() if node.endswith("Z")}

        counts = [self.count_steps(start, targets) for start in starts]

        return np.lcm.reduce(counts)


if __name__ == "__main__":
    Year2023Day08().print_results()

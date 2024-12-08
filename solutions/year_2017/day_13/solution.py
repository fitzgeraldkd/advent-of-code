from typing import List, Tuple

from solutions import BaseSolution


class Year2017Day13(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return tuple(int(value) for value in line.strip().split(': '))

    def get_scanner_position(self, fw_range: int, time: int):
        cycle_duration = fw_range * 2 - 2
        time_in_cycle = time % cycle_duration
        return time_in_cycle if time_in_cycle < fw_range else cycle_duration - time_in_cycle

    def check_if_caught(self, layers: List[Tuple[int, int]], delay: int):
        for layer in layers:
            depth, fw_range = layer
            if self.get_scanner_position(fw_range, depth + delay) == 0:
                return True
        return False

    def part_1(self):
        layers = self.inputs

        severity = 0

        for layer in layers:
            depth, fw_range = layer
            if self.get_scanner_position(fw_range, depth) == 0:
                severity += depth * fw_range

        return severity

    def part_2(self):
        layers = self.inputs

        start = 0
        step = 1

        for layer in layers:
            _, fw_range = layer
            if fw_range == 2:
                odds_only = self.check_if_caught([layer], 0)
                start = 1 if odds_only else 0
                step = 2

        for delay in range(start, 10000000, step):
            if not self.check_if_caught(layers, delay):
                break

        return delay


if __name__ == "__main__":
    Year2017Day13().print_results()

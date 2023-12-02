import numpy

from solutions import BaseSolution


class Year2020Day13(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        lines = super()._parse_inputs()
        return int(lines[0]), [int(n) if n != "x" else n for n in lines[1].split(",")]

    def part_1(self):
        timestamp, buses = self.inputs

        delays = [(bus, (-1 * timestamp) % bus) for bus in buses if bus != "x"]
        first_bus = min(delays, key=lambda delay: delay[1])
        return first_bus[0] * first_bus[1]

    def part_2(self):
        _, buses = self.inputs

        timestamp = 0
        for l in range(1, len(buses)):
            subset = buses[: l + 1]
            lcm = numpy.lcm.reduce(list(filter(lambda bus: bus != "x", subset[:-1])))

            while True:
                valid = True
                for i, bus in enumerate(subset):
                    if bus == "x":
                        continue

                    if 0 != (-1 * (timestamp + i)) % bus:
                        valid = False
                        break

                if valid:
                    break

                timestamp += lcm

        return timestamp


if __name__ == "__main__":
    Year2020Day13().print_results()

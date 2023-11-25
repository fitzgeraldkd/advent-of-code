from collections import defaultdict

from solutions import BaseSolution


class Year2018Day03(BaseSolution):
    def _parse_line(self, line):
        id, _, coords, size = line.strip().split()
        return {
            "id": int(id[1:]),
            "coords": tuple(int(coord) for coord in coords[:-1].split(",")),
            "size": tuple(int(dimension) for dimension in size.split("x")),
        }

    def part_1(self):
        claims = self.inputs

        fabric = defaultdict(int)
        for claim in claims:
            for x in range(claim["size"][0]):
                for y in range(claim["size"][1]):
                    fabric[(claim["coords"][0] + x, claim["coords"][1] + y)] += 1

        return len([square for square in fabric.values() if square > 1])

    def part_2(self):
        claims = self.inputs
        non_overlapping = set(claim["id"] for claim in claims)

        fabric = {}
        for claim in claims:
            for x in range(claim["size"][0]):
                for y in range(claim["size"][1]):
                    coord = (claim["coords"][0] + x, claim["coords"][1] + y)
                    if coord in fabric:
                        non_overlapping.discard(claim["id"])
                        non_overlapping.discard(fabric[coord])
                    else:
                        fabric[coord] = claim["id"]

        return non_overlapping.pop()


if __name__ == "__main__":
    Year2018Day03(__file__).print_results()

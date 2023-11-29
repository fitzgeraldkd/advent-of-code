from solutions import BaseSolution


DIRECTION_MAP = {
    "^": [0, 1],
    "v": [0, -1],
    ">": [1, 0],
    "<": [-1, 0],
}


class Year2015Day03(BaseSolution):
    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        houses = {(0, 0)}
        santa = [0, 0]

        for direction in self.inputs:
            dx, dy = DIRECTION_MAP[direction]
            santa[0] += dx
            santa[1] += dy
            houses.add(tuple(santa))

        return len(houses)

    def part_2(self):
        houses = {(0, 0)}
        real_santa = [0, 0]
        robo_santa = [0, 0]

        moving_santa = real_santa
        for direction in self.inputs:
            dx, dy = DIRECTION_MAP[direction]
            moving_santa[0] += dx
            moving_santa[1] += dy
            houses.add(tuple(moving_santa))
            moving_santa = robo_santa if moving_santa is real_santa else real_santa

        return len(houses)


if __name__ == "__main__":
    Year2015Day03(__file__).print_results()

from collections import defaultdict

from classes.square_grid import SquareGrid
from common.pathing import move
from solutions import BaseSolution
import time


class Year2024Day14(BaseSolution):
    module_file = __file__
    WIDTH = 101
    HEIGHT = 103

    def _parse_line(self, line):
        p, v = super()._parse_line(line).split(" ")
        return [
            tuple(int(value) for value in p[2:].split(",")),
            tuple(int(value) for value in v[2:].split(",")),
        ]

    def move_robot(self, position, velocity, seconds):
        x = (position[0] + velocity[0] * seconds) % self.WIDTH
        y = (position[1] + velocity[1] * seconds) % self.HEIGHT
        return (x, y)

    def part_1(self):
        print(self.inputs)
        quadrants = {
            "TL": 0,
            "TR": 0,
            "BL": 0,
            "BR": 0,
        }
        seconds = 100
        midpoint = (self.WIDTH // 2, self.HEIGHT // 2)

        for p, v in self.inputs:
            end_position = self.move_robot(p, v, seconds)
            if end_position[0] == midpoint[0] or end_position[1] == midpoint[1]:
                continue
            if end_position[0] < midpoint[0]:
                if end_position[1] < midpoint[1]:
                    quadrants["TL"] += 1
                else:
                    quadrants["BL"] += 1
            else:
                if end_position[1] < midpoint[1]:
                    quadrants["TR"] += 1
                else:
                    quadrants["BR"] += 1

        return quadrants["TL"] * quadrants["TR"] * quadrants["BL"] * quadrants["BR"]

    def test_print(self):
        print(self.inputs)
        quadrants = {
            "TL": 0,
            "TR": 0,
            "BL": 0,
            "BR": 0,
        }
        seconds = 7673
        midpoint = (self.WIDTH // 2, self.HEIGHT // 2)

        for p, v in self.inputs:
            end_position = self.move_robot(p, v, seconds)
            if end_position[0] == midpoint[0] or end_position[1] == midpoint[1]:
                continue
            if end_position[0] < midpoint[0]:
                if end_position[1] < midpoint[1]:
                    quadrants["TL"] += 1
                else:
                    quadrants["BL"] += 1
            else:
                if end_position[1] < midpoint[1]:
                    quadrants["TR"] += 1
                else:
                    quadrants["BR"] += 1

        return quadrants["TL"] * quadrants["TR"] * quadrants["BL"] * quadrants["BR"]

    def part_2(self):
        answer = 7672
        grid = SquareGrid(default=lambda: " ")
        for p, v in self.inputs:
            new_p = self.move_robot(p, v, answer)
            grid.set(new_p[0], new_p[1], "X")

        grid.print()

        # Steps to solve:
        # Run the script below.
        # Notice that the robots cluster in a horizontal arrangement at t=50 and repeat
        # every 103 seconds.
        # The robots cluster in a vertical arrangement at t=97 and repeat every 101
        # seconds.
        # These clusters occur simultaneously at t=7672, which is when the Christmas
        # tree pattern is revealed.

        # robots = []
        # start_offset = 7670
        # for p, v in self.inputs:
        #     new_p = self.move_robot(p, v, start_offset)
        #     robots.append([new_p, v])


        # # start_offset = 0
        # # robots = self.inputs

        # seconds = start_offset + 1
        # while True:
        #     grid = SquareGrid(default=lambda: " ")
        #     new_robots = []
        #     for p, v in robots:
        #         new_p = self.move_robot(p, v, 1)
        #         new_robots.append([new_p, v])
        #         grid.set(new_p[0], new_p[1], "X")
        #     robots = new_robots

        #     seconds += 1
        #     print(seconds)
        #     grid.print()
        #     time.sleep(0.2)
        #     # -
        #     # 51
        #     # 154

        #     # |
        #     # 98
        #     # 199
        # return None


if __name__ == "__main__":
    Year2024Day14().print_results()

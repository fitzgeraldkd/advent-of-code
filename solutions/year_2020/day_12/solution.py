from solutions import BaseSolution


CLOCKWISE_DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


class Year2020Day12(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return line[0], int(line[1:].strip())

    def part_1(self):
        facing = 1
        position = [0, 0]

        for action, amount in self.inputs:
            direction = CLOCKWISE_DIRECTIONS[facing]
            if action == "N":
                position[1] += amount
            elif action == "E":
                position[0] += amount
            elif action == "S":
                position[1] -= amount
            elif action == "W":
                position[0] -= amount
            elif action == "F":
                position[0] += direction[0] * amount
                position[1] += direction[1] * amount
            elif action == "L":
                facing = int(facing - amount / 90) % 4
            elif action == "R":
                facing = int(facing + amount / 90) % 4

        return abs(position[0]) + abs(position[1])

    def part_2(self):
        ship = [0, 0]
        waypoint = [10, 1]

        for action, amount in self.inputs:
            if action == "N":
                waypoint[1] += amount
            elif action == "E":
                waypoint[0] += amount
            elif action == "S":
                waypoint[1] -= amount
            elif action == "W":
                waypoint[0] -= amount
            elif action == "F":
                distance = [
                    (waypoint[0] - ship[0]) * amount,
                    (waypoint[1] - ship[1]) * amount,
                ]
                ship[0] += distance[0]
                ship[1] += distance[1]
                waypoint[0] += distance[0]
                waypoint[1] += distance[1]
            elif action == "L":
                for _ in range(int(amount / 90)):
                    waypoint = [
                        ship[0] + ship[1] - waypoint[1],
                        ship[1] + waypoint[0] - ship[0],
                    ]
            elif action == "R":
                for _ in range(int(amount / 90)):
                    waypoint = [
                        ship[0] + waypoint[1] - ship[1],
                        ship[1] + ship[0] - waypoint[0],
                    ]

        return abs(ship[0]) + abs(ship[1])


if __name__ == "__main__":
    Year2020Day12().print_results()

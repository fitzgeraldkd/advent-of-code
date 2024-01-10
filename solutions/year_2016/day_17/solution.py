import hashlib

from classes.priority_queue import PriorityQueue
from solutions import BaseSolution

OPEN_DOOR = {"b", "c", "d", "e", "f"}
DIRECTIONS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


class Year2016Day17(BaseSolution):
    module_file = __file__
    passcode = ""

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_hash(self, path: str):
        return hashlib.md5(f"{self.passcode}{path}".encode("utf-8")).hexdigest()

    def get_neighbors(self, path: str, location):
        neighbors = []
        hash = self.get_hash(path)
        if hash[0] in OPEN_DOOR and location[1] > 0:
            neighbors.append((f"{path}U", (location[0], location[1] - 1)))
        if hash[1] in OPEN_DOOR and location[1] < 3:
            neighbors.append((f"{path}D", (location[0], location[1] + 1)))
        if hash[2] in OPEN_DOOR and location[0] > 0:
            neighbors.append((f"{path}L", (location[0] - 1, location[1])))
        if hash[3] in OPEN_DOOR and location[0] < 3:
            neighbors.append((f"{path}R", (location[0] + 1, location[1])))
        return neighbors

    def get_distance(self, location: tuple):
        return 6 - location[0] - location[1]

    def part_1(self):
        self.passcode = self.inputs
        queue = PriorityQueue()
        queue.add_item(("", (0, 0)), 6)
        while not queue.is_empty():
            path, location = queue.pop()
            if location == (3, 3):
                return path
            neighbors = self.get_neighbors(path, location)
            for neighbor in neighbors:
                queue.add_item(
                    neighbor, len(neighbor[0]) + self.get_distance(neighbor[1])
                )

    def part_2(self):
        self.passcode = self.inputs
        queue = PriorityQueue()
        queue.add_item(("", (0, 0)), 6)
        longest = 0
        while not queue.is_empty():
            path, location = queue.pop()
            if location == (3, 3):
                longest = max(longest, len(path))
                continue
            neighbors = self.get_neighbors(path, location)
            for neighbor in neighbors:
                queue.add_item(
                    neighbor, -1 * (len(neighbor[0]) + self.get_distance(neighbor[1]))
                )
        return longest


if __name__ == "__main__":
    Year2016Day17().print_results()

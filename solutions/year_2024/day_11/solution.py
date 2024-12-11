from collections import defaultdict

from solutions import BaseSolution


class Year2024Day11(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return [int(v) for v in super()._parse_line(line).split(" ")]

    def _parse_inputs(self):
        stones = super()._parse_inputs()[0]
        stone_dict = defaultdict(int)
        for stone in stones:
            stone_dict[stone] += 1
        return stone_dict

    def blink(self, stones):
        new_dict = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                new_dict[1] += count
            elif len(f"{stone}") % 2 == 0:
                stone_str = f"{stone}"
                half_index = len(stone_str) // 2
                left_stone = int(stone_str[:half_index])
                right_stone = int(stone_str[half_index:])
                new_dict[left_stone] += count
                new_dict[right_stone] += count
            else:
                new_dict[stone * 2024] += count

        return new_dict

    def part_1(self):
        stones = self.inputs

        for _ in range(25):
            stones = self.blink(stones)

        return sum(stones.values())

    def part_2(self):
        stones = self.inputs

        for _ in range(75):
            stones = self.blink(stones)

        return sum(stones.values())


if __name__ == "__main__":
    Year2024Day11().print_results()

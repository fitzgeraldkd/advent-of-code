from solutions import BaseSolution


class Year2015Day18(BaseSolution):
    STEPS = 100
    module_file = __file__

    def _parse_line(self, line: str):
        return [item == "#" for item in line.strip()]

    def count_neighbors(self, grid):
        neighbors = []
        for y, row in enumerate(grid):
            neighbors.append([])
            for x, cell in enumerate(row):
                delta_x = [0]
                delta_y = [0]

                if y == 0:
                    delta_y.append(1)
                elif y == len(grid) - 1:
                    delta_y.append(-1)
                else:
                    delta_y.extend([1, -1])

                if x == 0:
                    delta_x.append(1)
                elif x == len(row) - 1:
                    delta_x.append(-1)
                else:
                    delta_x.extend([1, -1])

                count = 0
                for dx in delta_x:
                    for dy in delta_y:
                        if dx == 0 and dy == 0:
                            continue
                        count += grid[y + dy][x + dx]

                neighbors[y].append(count)

        return neighbors

    def count_lights(self, grid):
        return sum(len(list(filter(None, row))) for row in grid)

    def part_1(self):
        grid = self.inputs

        for _ in range(self.STEPS):
            neighbors = self.count_neighbors(grid)
            for y, row in enumerate(grid):
                for x, _ in enumerate(row):
                    grid[y][x] = (
                        (neighbors[y][x] in [2, 3])
                        if grid[y][x]
                        else (neighbors[y][x] == 3)
                    )

        return self.count_lights(grid)

    def part_2(self):
        grid = self.inputs

        grid[0][0] = True
        grid[0][len(grid[0]) - 1] = True
        grid[len(grid) - 1][0] = True
        grid[len(grid) - 1][len(grid[0]) - 1] = True

        for _ in range(self.STEPS):
            neighbors = self.count_neighbors(grid)
            for y, row in enumerate(grid):
                for x, _ in enumerate(row):
                    if x in [0, len(grid[0]) - 1] and y in [0, len(grid) - 1]:
                        continue
                    grid[y][x] = (
                        (neighbors[y][x] in [2, 3])
                        if grid[y][x]
                        else (neighbors[y][x] == 3)
                    )

        return self.count_lights(grid)


if __name__ == "__main__":
    Year2015Day18().print_results()

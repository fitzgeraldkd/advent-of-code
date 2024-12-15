from classes.square_grid import SquareGrid
from common.pathing import move
from solutions import BaseSolution

DIRECTIONS = {
    "<": (-1, 0),
    "v": (0, 1),
    ">": (1, 0),
    "^": (0, -1),
}


class Year2024Day15(BaseSolution):
    module_file = __file__
    group_delimiter = "\n"

    def _parse_inputs(self):
        tiles, instructions = super()._parse_inputs()
        robot = None
        grid = SquareGrid(default=lambda: ".")
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                grid.set(x, y, tile)
                if tile == "@":
                    robot = (x, y)

        joined_instructions = "".join(instructions)
        return grid, robot, joined_instructions

    def move(self, grid: SquareGrid, robot, direction):
        destination = move(robot, direction)
        end_point = destination
        moving_boxes = False
        while True:
            if grid.get(*end_point) == "#":
                return robot

            if grid.get(*end_point) == ".":
                if moving_boxes:
                    grid.set(*end_point, "O")
                grid.set(*destination, "@")
                grid.set(*robot, ".")
                return destination

            if grid.get(*end_point) == "O":
                moving_boxes = True
                end_point = move(end_point, direction)
            else:
                break

    def part_1(self):
        grid, robot, instructions = self.inputs
        for instruction in instructions:
            direction = DIRECTIONS[instruction]
            robot = self.move(grid, robot, direction)

        results = 0

        for x in grid.x_range:
            for y in grid.y_range:
                value = grid.get(x, y)
                if value == "O":
                    results += y * 100 + x

        return results

    def can_move_wide_box(self, grid, first_half, direction):
        value = grid.get(*first_half)
        if value not in "[]":
            raise Exception

        other_half = (
            (first_half[0] + 1, first_half[1])
            if value == "["
            else (first_half[0] - 1, first_half[1])
        )

        if direction[0] == 0:
            first_half_adj = move(first_half, direction)
            other_half_adj = move(other_half, direction)
            first_half_value = grid.get(*first_half_adj)
            other_half_value = grid.get(*other_half_adj)

            if first_half_value == "#" or other_half_value == "#":
                return False

            if first_half_value in "[]" and not self.can_move_wide_box(grid, first_half_adj, direction):
                return False

            if other_half_value in "[]" and not self.can_move_wide_box(grid, other_half_adj, direction):
                return False

            return True
        else:
            adj = move(first_half, direction, magnitude=2)
            adj_value = grid.get(*adj)

            if adj_value == "#":
                return False
            if adj_value in"[]":
                return self.can_move_wide_box(grid, adj, direction)

            return True

    def move_wide_box(self, grid, first_half, direction):
        value = grid.get(*first_half)
        if value not in "[]":
            raise Exception

        is_left_half = value == "["
        if is_left_half:
            left_half = first_half
            right_half = move(left_half, (1, 0))
        else:
            right_half = first_half
            left_half = move(right_half, (-1, 0))

        if direction[0] == 0:
            left_half_adj = move(left_half, direction)
            right_half_adj = move(right_half, direction)
            left_half_value = grid.get(*left_half_adj)
            right_half_value = grid.get(*right_half_adj)

            if left_half_value in "[]":
                self.move_wide_box(grid, left_half_adj, direction)

            if right_half_value == "[":
                self.move_wide_box(grid, right_half_adj, direction)

            grid.set(*left_half_adj, "[")
            grid.set(*right_half_adj, "]")
            grid.set(*left_half, ".")
            grid.set(*right_half, ".")
        else:
            adj = move(first_half, direction, magnitude=2)
            adj_value = grid.get(*adj)

            if adj_value in "[]":
                self.move_wide_box(grid, adj, direction)

            other_half = move(first_half, direction)
            grid.set(*adj, grid.get(*other_half))
            grid.set(*other_half, value)
            grid.set(*first_half, ".")

    def move_part_2(self, grid, robot, direction):
        adj = move(robot, direction)
        adj_value = grid.get(*adj)
        if adj_value in "[]":
            if self.can_move_wide_box(grid, adj, direction):
                self.move_wide_box(grid, adj, direction)
                grid.set(*adj, "@")
                grid.set(*robot, ".")
                return adj
            else:
                return robot
        elif adj_value == "#":
            return robot
        elif adj_value == ".":
            grid.set(*adj, "@")
            grid.set(*robot, ".")
            return adj

    def part_2(self):
        initial_grid, robot, instructions = self.inputs

        grid = SquareGrid(default=lambda: ".")

        for x in initial_grid.x_range:
            for y in initial_grid.y_range:
                value = initial_grid.get(x, y)
                if value == "@":
                    grid.set(x * 2, y, "@")
                    robot = (x * 2, y)
                elif value == "#":
                    grid.set(x * 2, y, "#")
                    grid.set(x * 2 + 1, y, "#")
                elif value == "O":
                    grid.set(x * 2, y, "[")
                    grid.set(x * 2 + 1, y, "]")

        for instruction in instructions:
            direction = DIRECTIONS[instruction]
            robot = self.move_part_2(grid, robot, direction)

        results = 0

        for x in grid.x_range:
            for y in grid.y_range:
                value = grid.get(x, y)
                if value == "[":
                    results += y * 100 + x

        return results


if __name__ == "__main__":
    Year2024Day15().print_results()

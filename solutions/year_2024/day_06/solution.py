from classes.square_grid import SquareGrid
from solutions import BaseSolution
from common.pathing import move, rotate



class Year2024Day06(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        lines = super()._parse_inputs()
        grid = SquareGrid(default=lambda: '.')
        for y, row in enumerate(lines):
            for x, value in enumerate(row):
                if value == '#':
                    grid.set(x, y, '#')
                elif value != '.':
                    coords = (x, y)
                    facing = value
                else:
                    grid.set(x, y, '.')
        return grid, coords, facing

    def part_1(self):
        print(self.inputs)
        grid, coords, _ = self.inputs
        direction = (0, -1)

        visited_tiles = set([coords])
        
        adjacent = move(coords, direction)
        print(coords, adjacent)
        print(grid.min_x, grid.max_x, grid.min_y, grid.max_y)
        print(grid.is_in_bounding_box(*adjacent))
        while grid.is_in_bounding_box(*adjacent):
            # print(adjacent)
            if grid.get(*adjacent) == '#':
                direction = rotate(direction, "R")
                adjacent = move(coords, direction)
            else:
                coords = adjacent
                visited_tiles.add(coords)
                adjacent = move(coords, direction)
        return len(visited_tiles)
        

    def is_looped(self, grid, coords):
        direction = (0, -1)
        visited_tiles = set([(*coords, *direction)])
        
        adjacent = move(coords, direction)
        # print(coords, adjacent)
        # print(grid.min_x, grid.max_x, grid.min_y, grid.max_y)
        # print(grid.is_in_bounding_box(*adjacent))
        while grid.is_in_bounding_box(*adjacent):
            if (*adjacent, *direction) in visited_tiles:
                return True
            if grid.get(*adjacent) == '#':
                direction = rotate(direction, "R")
                adjacent = move(coords, direction)
            else:
                coords = adjacent
                visited_tiles.add((*coords, *direction))
                adjacent = move(coords, direction)
        return False


    def part_2(self):
        print(self.inputs)
        grid, initial_coords, _ = self.inputs
        direction = (0, -1)
        coords = initial_coords

        visited_tiles = set([coords])
        
        adjacent = move(coords, direction)
        print(coords, adjacent)
        print(grid.min_x, grid.max_x, grid.min_y, grid.max_y)
        print(grid.is_in_bounding_box(*adjacent))
        while grid.is_in_bounding_box(*adjacent):
            # print(adjacent)
            if grid.get(*adjacent) == '#':
                direction = rotate(direction, "R")
                adjacent = move(coords, direction)
            else:
                coords = adjacent
                visited_tiles.add(coords)
                adjacent = move(coords, direction)
        print(visited_tiles)

        visited_tiles.discard(initial_coords)

        count = 0
        correct_tiles = []
        for tile in visited_tiles:
            new_grid, _, _ = self.inputs
            # print(new_grid)
            new_grid.set(tile[0], tile[1], '#')
            if self.is_looped(new_grid, initial_coords):
                correct_tiles.append(tile)
                count += 1
        
        print(correct_tiles)
        return count


if __name__ == "__main__":
    Year2024Day06().print_results()

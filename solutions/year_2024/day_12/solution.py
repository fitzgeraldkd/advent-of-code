from classes.square_grid import SquareGrid
from collections import defaultdict
from common.pathing import get_adjacent, move
from solutions import BaseSolution


class Year2024Day12(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        inputs = super()._parse_inputs()
        x_range = range(len(inputs[0]))
        y_range = range(len(inputs))

        garden = SquareGrid(default=lambda: None)
        index = 0
        for y, row in enumerate(inputs):
            for x, value in enumerate(row):
                if garden.get(x, y) is None:
                    garden.set(x, y, index)
                    cells_to_check = set(get_adjacent((x, y)))
                    checked_cells = set([(x, y)])
                    while len(cells_to_check) > 0:
                        cell_to_check = cells_to_check.pop()
                        if (
                            cell_to_check[0] in x_range and
                            cell_to_check[1] in y_range and
                            inputs[cell_to_check[1]][cell_to_check[0]] == value
                        ):
                            garden.set(*cell_to_check, index)
                            checked_cells.add(cell_to_check)
                            adj = get_adjacent(cell_to_check)
                            for adj_cell in adj:
                                if adj_cell not in checked_cells:
                                    cells_to_check.add(adj_cell)

                        checked_cells.add(cell_to_check)
                    index += 1

        return garden

    def part_1(self):
        garden = self.inputs
        areas = defaultdict(int)
        perimeters = defaultdict(int)

        def garden_mapper(value, x, y):
            areas[value] += 1
            for adj_x, adj_y in get_adjacent((x, y)):
                if garden.get(adj_x, adj_y) != value:
                    perimeters[value] += 1
            return value

        garden.map_all(garden_mapper)

        results = 0
        for index in areas:
            results += areas[index] * perimeters[index]

        return results

    def part_2(self):
        garden = self.inputs
        areas = defaultdict(int)
        perimeters = defaultdict(int)
        perimeter_edges = defaultdict(set)

        def garden_mapper(value, x, y):
            areas[value] += 1
            for adj_x, adj_y in get_adjacent((x, y)):
                if garden.get(adj_x, adj_y) != value:
                    edge = ((x + adj_x) / 2, (y + adj_y) / 2)
                    direction = (1, 0) if adj_x == x else (0, 1)
                    facing = adj_y > y if adj_x == x else adj_x > x
                    edges = perimeter_edges[value]
                    if (
                        (*move(edge, direction), facing) not in edges and
                        (*move(edge, direction, magnitude=-1), facing) not in edges
                    ):
                        perimeters[value] += 1
                    edges.add((*edge, facing))

        garden.each(garden_mapper)

        results = 0
        for index in areas:
            results += areas[index] * perimeters[index]

        return results


if __name__ == "__main__":
    Year2024Day12().print_results()

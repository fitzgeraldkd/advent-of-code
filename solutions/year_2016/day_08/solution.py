from solutions import BaseSolution


class Display:
    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows
        self.lights = [[False for _ in range(columns)] for _ in range(rows)]

    def rect(self, columns: int, rows: int):
        for x in range(columns):
            for y in range(rows):
                self.lights[y][x] = True

    def rotate_column(self, column: int, offset: int):
        offset = self.rows - (offset % self.rows)
        column_lights = [self.lights[row][column] for row in range(self.rows)]
        column_lights = [*column_lights[offset:], *column_lights[:offset]]
        for row in range(self.rows):
            self.lights[row][column] = column_lights[row]

    def rotate_row(self, row: int, offset: int):
        offset = self.columns - (offset % self.columns)
        self.lights[row] = [*self.lights[row][offset:], *self.lights[row][:offset]]

    def count_lights(self):
        count = 0
        for row in self.lights:
            for light in row:
                if light:
                    count += 1
        return count

    def print(self):
        for row in self.lights:
            print("".join(["#" if light else "." for light in row]))


class Year2016Day08(BaseSolution):
    module_file = __file__

    def part_1(self):
        operations = self.inputs
        display = Display(columns=50, rows=6)

        for operation in operations:
            if operation.startswith("rect"):
                _, dimensions = operation.split(" ")
                columns, rows = dimensions.split("x")
                display.rect(int(columns), int(rows))
            else:
                _, axis, at, _, amount = operation.split(" ")
                _, coordinate = at.split("=")
                if axis == "row":
                    display.rotate_row(int(coordinate), int(amount))
                else:
                    display.rotate_column(int(coordinate), int(amount))

        return display.count_lights()

    def part_2(self):
        operations = self.inputs
        display = Display(columns=50, rows=6)

        for operation in operations:
            if operation.startswith("rect"):
                _, dimensions = operation.split(" ")
                columns, rows = dimensions.split("x")
                display.rect(int(columns), int(rows))
            else:
                _, axis, at, _, amount = operation.split(" ")
                _, coordinate = at.split("=")
                if axis == "row":
                    display.rotate_row(int(coordinate), int(amount))
                else:
                    display.rotate_column(int(coordinate), int(amount))

        display.print()
        return None


if __name__ == "__main__":
    Year2016Day08().print_results()

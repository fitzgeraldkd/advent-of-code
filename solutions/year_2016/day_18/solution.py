from solutions import BaseSolution

TRAP_CONDITIONS = ["^^.", ".^^", "^..", "..^"]


class Year2016Day18(BaseSolution):
    module_file = __file__

    PART_1_ROWS = 40

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_next_row(self, board: list):
        last_row = board[-1]
        new_row = []
        for i in range(len(last_row)):
            checks = []
            for j in [-1, 0, 1]:
                if i + j < 0 or i + j >= len(last_row):
                    checks.append(".")
                else:
                    checks.append(last_row[i + j])
            new_row.append("^" if "".join(checks) in TRAP_CONDITIONS else ".")
        return "".join(new_row)

    def get_safe_tiles(self, board: list):
        safe_tiles = 0
        for row in board:
            for tile in row:
                safe_tiles += 1 if tile == "." else 0
        return safe_tiles

    def part_1(self):
        board = [self.inputs]

        while len(board) < self.PART_1_ROWS:
            board.append(self.get_next_row(board))

        return self.get_safe_tiles(board)

    def part_2(self):
        row = self.inputs

        safe_tiles = 0
        rows_counted = 0

        # TODO: Check if the pattern repeats.

        while rows_counted < 400000:
            safe_tiles += self.get_safe_tiles([row])
            row = self.get_next_row([row])
            rows_counted += 1

        return safe_tiles


if __name__ == "__main__":
    Year2016Day18().print_results()

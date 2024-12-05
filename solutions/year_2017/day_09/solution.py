from solutions import BaseSolution


class Year2017Day09(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        stream = self.inputs

        depth = 0
        in_garbage = False
        skip_next = False
        score = 0

        for char in stream:
            if in_garbage:
                if skip_next:
                    skip_next = False
                    continue
                elif char == '!':
                    skip_next = True
                elif char == '>':
                    in_garbage = False
            else:
                if char == '<':
                    in_garbage = True
                elif char == '{':
                    depth += 1
                    score += depth
                elif char == '}':
                    depth -= 1

        return score

    def part_2(self):
        stream = self.inputs

        garbage_length = 0

        in_garbage = False
        skip_next = False

        for char in stream:
            if in_garbage:
                if skip_next:
                    skip_next = False
                    continue
                elif char == '!':
                    skip_next = True
                elif char == '>':
                    in_garbage = False
                else:
                    garbage_length += 1
            else:
                if char == '<':
                    in_garbage = True

        return garbage_length


if __name__ == "__main__":
    Year2017Day09().print_results()

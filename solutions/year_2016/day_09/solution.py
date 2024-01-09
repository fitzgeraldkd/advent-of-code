from solutions import BaseSolution


class Year2016Day09(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def decompress(self, file: str):
        decompressed_file = []
        index = 0
        while index < len(file):
            if file[index] == "(":
                closing_index = file[index:].index(")") + index
                length, count = [
                    int(value) for value in file[index + 1 : closing_index].split("x")
                ]
                substring = file[closing_index + 1 : closing_index + length + 1]
                decompressed_file.append(substring * count)
                index = closing_index + length + 1
            else:
                decompressed_file.append(file[index])
                index += 1
        return "".join(decompressed_file)

    def decompress_recursive(self, file: str):
        index = 0
        size = 0
        while index < len(file):
            if file[index] == "(":
                close_index = file.index(")", index)
                length, count = [
                    int(value) for value in file[index + 1 : close_index].split("x")
                ]

                size += (
                    self.decompress_recursive(
                        file[close_index + 1 : close_index + length + 1]
                    )
                    * count
                )

                index = close_index + length + 1
            else:
                index += 1
                size += 1

        return size

    def part_1(self):
        file = self.inputs

        decompressed_file = self.decompress(file)

        return len(decompressed_file)

    def part_2(self):
        file = self.inputs

        decompressed_file = self.decompress_recursive(file)

        return decompressed_file


if __name__ == "__main__":
    Year2016Day09().print_results()

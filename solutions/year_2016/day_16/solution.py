from solutions import BaseSolution


class Year2016Day16(BaseSolution):
    module_file = __file__

    PART_1_LENGTH = 272

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def expand_data(self, data: str):
        data_to_append = (
            data[::-1].replace("1", "_").replace("0", "1").replace("_", "0")
        )
        return f"{data}0{data_to_append}"

    def get_checksum(self, data: str):
        checksum = []
        for pair in [data[i : i + 2] for i in range(0, len(data), 2)]:
            checksum.append("1" if pair[0] == pair[1] else "0")
        checksum = "".join(checksum)
        return checksum if len(checksum) % 2 == 1 else self.get_checksum(checksum)

    def part_1(self):
        data = self.inputs

        while len(data) < self.PART_1_LENGTH:
            data = self.expand_data(data)

        data = data[: self.PART_1_LENGTH]

        return self.get_checksum(data)

    def part_2(self):
        data = self.inputs

        while len(data) < 35651584:
            data = self.expand_data(data)

        data = data[:35651584]

        return self.get_checksum(data)


if __name__ == "__main__":
    Year2016Day16().print_results()

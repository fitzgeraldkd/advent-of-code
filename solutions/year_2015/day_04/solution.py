import hashlib

from solutions import BaseSolution


MAX_ATTEMPTS = 10000000


def hash(input: str):
    return hashlib.md5(input.encode("utf-8")).hexdigest()


class Year2015Day04(BaseSolution):
    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        for i in range(MAX_ATTEMPTS):
            hashed = hash(f"{self.inputs}{i}")
            if hashed.startswith("00000"):
                return i

    def part_2(self):
        for i in range(MAX_ATTEMPTS):
            hashed = hash(f"{self.inputs}{i}")
            if hashed.startswith("000000"):
                return i


if __name__ == "__main__":
    Year2015Day04(__file__).print_results()

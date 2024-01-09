import hashlib
import re

from solutions import BaseSolution


class Year2016Day14(BaseSolution):
    module_file = __file__

    hashed = {}
    salt = ""

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def get_hash(self, index: int, stretched: bool):
        if index in self.hashed:
            return self.hashed[index]
        else:
            hash = f"{self.salt}{index}"
            for _ in range(2017 if stretched else 1):
                hash = hashlib.md5(hash.encode("utf-8")).hexdigest()
            self.hashed[index] = hash
            return hash

    def is_key(self, index: int, stretched=False):
        hash = self.get_hash(index, stretched)
        triplet_match = re.search(r"([0-9a-f])(\1){2}", hash)
        if triplet_match:
            for stream in range(1000):
                stream_hash = self.get_hash(index + stream + 1, stretched)
                if triplet_match.group(0)[0] * 5 in stream_hash:
                    return True
        return False

    def part_1(self):
        self.salt = self.inputs
        self.hashed = {}
        indeces = []
        print("salt:", self.salt)

        index = 0
        while len(indeces) < 64:
            if self.is_key(index):
                indeces.append(index)
            index += 1

        return indeces[-1]

    def part_2(self):
        self.salt = self.inputs
        self.hashed = {}
        indeces = []

        index = 0
        while len(indeces) < 64:
            if self.is_key(index, stretched=True):
                indeces.append(index)
            index += 1

        return indeces[-1]


if __name__ == "__main__":
    Year2016Day14().print_results()

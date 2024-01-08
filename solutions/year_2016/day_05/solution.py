import hashlib

from solutions import BaseSolution


class Year2016Day05(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        return super()._parse_inputs()[0]

    def part_1(self):
        door_id = self.inputs

        password = []
        index = 0
        while len(password) < 8:
            hash = hashlib.md5(f"{door_id}{index}".encode("utf-8")).hexdigest()

            if (hash).startswith("00000"):
                password.append(hash[5])

            index += 1

        return "".join(password)

    def part_2(self):
        door_id = self.inputs

        password = [None, None, None, None, None, None, None, None]
        index = 0
        while any([character is None for character in password]):
            hash = hashlib.md5(f"{door_id}{index}".encode("utf-8")).hexdigest()

            if (hash).startswith("00000") and hash[5] not in [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            ]:
                position = int(hash[5])
                if position < len(password) and password[position] is None:
                    password[position] = hash[6]

            index += 1

        return "".join(password)


if __name__ == "__main__":
    Year2016Day05().print_results()

import re

from solutions import BaseSolution


REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


class Year2020Day04(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_group(self, lines):
        passport = {}
        for line in lines:
            fields = line.strip().split(" ")
            for field in fields:
                key, value = field.split(":")
                passport[key] = value
        return passport

    def part_1(self):
        passports = self.inputs
        valid_count = 0

        for passport in passports:
            if len(REQUIRED_FIELDS - set(passport.keys())) == 0:
                valid_count += 1

        return valid_count

    def part_2(self):
        passports = self.inputs
        valid_count = 0

        for passport in passports:
            if len(REQUIRED_FIELDS - set(passport.keys())) != 0:
                continue

            if not (1920 <= int(passport["byr"]) <= 2002):
                continue

            if not (2010 <= int(passport["iyr"]) <= 2020):
                continue

            if not (2020 <= int(passport["eyr"]) <= 2030):
                continue

            min_hgt, max_hgt = (150, 193) if passport["hgt"][-2:] == "cm" else (59, 76)
            if not (min_hgt <= int(passport["hgt"][:-2]) <= max_hgt):
                continue

            if not re.search(r"#[0-9a-f]{6}", passport["hcl"]):
                continue

            if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                continue

            if not re.search(r"^[0-9]{9}$", passport["pid"]):
                continue

            valid_count += 1

        return valid_count


if __name__ == "__main__":
    Year2020Day04().print_results()

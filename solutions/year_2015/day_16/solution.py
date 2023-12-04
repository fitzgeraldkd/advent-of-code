from solutions import BaseSolution


class Year2015Day16(BaseSolution):
    FILTERS = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    module_file = __file__

    def _parse_line(self, line: str):
        [name, traits] = line.strip().split(": ", 1)
        sue = {"id": int(name.split(" ")[1])}
        for trait in traits.split(", "):
            [trait_name, quantity] = trait.split(": ")
            sue[trait_name] = int(quantity)
        return sue

    def part_1(self):
        sues = self.inputs

        def matches_property(sue, trait, quantity):
            if trait not in sue:
                return True

            return sue[trait] == quantity

        for trait in self.FILTERS.keys():
            sues = list(
                filter(
                    lambda sue: matches_property(sue, trait, self.FILTERS[trait]), sues
                )
            )

        return sues[0]["id"]

    def part_2(self):
        sues = self.inputs

        def matches_property(sue, trait, quantity):
            if trait not in sue:
                return True
            elif trait in ["cats", "trees"]:
                return sue[trait] > quantity
            elif trait in ["pomeranians", "goldfish"]:
                return sue[trait] < quantity
            else:
                return sue[trait] == quantity

        for trait in self.FILTERS.keys():
            sues = list(
                filter(
                    lambda sue: matches_property(sue, trait, self.FILTERS[trait]), sues
                )
            )

        return sues[0]["id"]


if __name__ == "__main__":
    Year2015Day16().print_results()

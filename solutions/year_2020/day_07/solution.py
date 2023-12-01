from solutions import BaseSolution


def can_hold_shiny_gold_bag(bags, bag: str):
    for content in bags[bag].keys():
        if (content == "shiny gold") or can_hold_shiny_gold_bag(bags, content):
            return True
    return False


def get_total_bag_count(bags, bag: str):
    total_count = 0

    for content, quantity in bags[bag].items():
        total_count += quantity * (1 + get_total_bag_count(bags, content))

    return total_count


class Year2020Day07(BaseSolution):
    def _parse_line(self, line: str):
        container, joined_content = line.strip()[:-1].split(" bags contain ")
        contents = {}

        if joined_content != "no other bags":
            for content in joined_content.split(", "):
                quantity, description = content.split(" ", maxsplit=1)
                contents[description[: description.rfind(" bag")]] = int(quantity)
        return container, contents

    def _parse_inputs(self):
        bags = {}
        for line in self._read_inputs():
            container, contents = self._parse_line(line)
            bags[container] = contents
        return bags

    def part_1(self):
        bags = self.inputs
        return len([bag for bag in bags.keys() if can_hold_shiny_gold_bag(bags, bag)])

    def part_2(self):
        return get_total_bag_count(self.inputs, "shiny gold")


if __name__ == "__main__":
    Year2020Day07(__file__).print_results()

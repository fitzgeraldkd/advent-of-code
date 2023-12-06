from copy import deepcopy

import regex
from typing import List
from solutions import BaseSolution


class Year2020Day19(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_rule(self, rule_dict: dict, rule: List[List[int]]):
        parsed_subrules = []
        for subrule in rule:
            parsed_subrule = ""
            for index in subrule:
                if isinstance(rule_dict[index], list):
                    rule_dict[index] = self._parse_rule(rule_dict, rule_dict[index])

                parsed_subrule += rule_dict[index]
            parsed_subrules.append(r"(" + parsed_subrule + r")")
        return r"(" + r"|".join(parsed_subrules) + r")"

    def _parse_inputs(self):
        rules, messages = super()._parse_inputs()
        part_1_rule_dict = {}
        for rule in rules:
            index, pattern_string = rule.split(": ")
            index = int(index)
            if pattern_string.startswith('"'):
                part_1_rule_dict[index] = rf"{pattern_string[1:-1]}"
            else:
                part_1_rule_dict[index] = [
                    [int(p) for p in patterns.split(" ")]
                    for patterns in pattern_string.split(" | ")
                ]

        part_2_rule_dict = deepcopy(part_1_rule_dict)
        for index, rule in part_1_rule_dict.items():
            if isinstance(rule, list):
                part_1_rule_dict[index] = self._parse_rule(part_1_rule_dict, rule)

        if 31 in part_2_rule_dict and 42 in part_2_rule_dict:
            rule_31 = self._parse_rule(part_2_rule_dict, part_2_rule_dict[31])
            rule_42 = self._parse_rule(part_2_rule_dict, part_2_rule_dict[42])
            part_2_rule_dict[8] = rf"({rule_42})+"
            part_2_rule_dict[
                11
            ] = rf"({rule_42}(?P<recursive>{rule_42}(?&recursive){rule_31}|){rule_31})"
        for index, rule in part_2_rule_dict.items():
            if isinstance(rule, list):
                part_2_rule_dict[index] = self._parse_rule(part_2_rule_dict, rule)

        return messages, part_1_rule_dict, part_2_rule_dict

    def part_1(self):
        messages, rule_dict, _ = self.inputs
        total = 0
        rule = rule_dict[0]

        for message in messages:
            if regex.match(rf"^{rule}$", message):
                total += 1

        return total

    def part_2(self):
        messages, _, rule_dict = self.inputs
        total = 0
        rule = rule_dict[0]

        for message in messages:
            if regex.match(rf"^{rule}$", message):
                total += 1

        return total


if __name__ == "__main__":
    Year2020Day19().print_results()

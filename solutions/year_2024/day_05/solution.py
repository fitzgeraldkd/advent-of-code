from collections import defaultdict
from typing import List
from solutions import BaseSolution


class Year2024Day05(BaseSolution):
    module_file = __file__
    group_delimiter = "\n"

    def _parse_inputs(self):
        order_rules, page_updates = super()._parse_inputs()
        page_updates = [[int(v) for v in row.strip().split(",")] for row in page_updates]
        order_rules_map = defaultdict(list)
        for rule in order_rules:
            a, b = [int(v) for v in rule.strip().split("|")]
            order_rules_map[a].append(b)
        return [order_rules_map, page_updates]

    def is_ordered_correctly(self, order_rules, pages: List[int]):
        checked_pages = []
        for page in pages:
            if any(p in order_rules[page] for p in checked_pages):
                return False
            checked_pages.append(page)

        return True

    def fix_ordering(self, order_rules, pages: List[int]):
        fixed_pages = []
        for page in pages:
            i = next(
                (i for i, p in enumerate(fixed_pages) if p in order_rules[page]),
                len(fixed_pages),
            )
            fixed_pages.insert(i, page)

        return fixed_pages

    def part_1(self):
        order_rule_map, page_updates = self.inputs

        results = 0
        for pages in page_updates:
            if self.is_ordered_correctly(order_rule_map, pages):
                results += pages[(len(pages) - 1) // 2]

        return results

    def part_2(self):
        order_rule_map, page_updates = self.inputs

        results = 0
        for pages in page_updates:
            if not self.is_ordered_correctly(order_rule_map, pages):
                fixed_order = self.fix_ordering(order_rule_map, pages)
                results += fixed_order[(len(fixed_order) - 1) // 2]

        return results


if __name__ == "__main__":
    Year2024Day05().print_results()

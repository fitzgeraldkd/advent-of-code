from collections import OrderedDict

from typing import List
from solutions import BaseSolution


class Year2020Day16(BaseSolution):
    group_delimiter = "\n"
    module_file = __file__

    def _parse_line(self, line: str, variant: str):
        if variant == "ticket":
            return [int(value) for value in line.strip().split(",")]
        else:
            field, ranges = line.strip().split(": ")
            ranges = [
                [int(value) for value in range.split("-")]
                for range in ranges.split(" or ")
            ]
            return field, [range(start, end + 1) for start, end in ranges]

    def _parse_group(self, lines: List[str]):
        if "ticket" in lines[0]:
            parsed_lines = [
                self._parse_line(line, variant="ticket") for line in lines[1:]
            ]
            if "your ticket" in lines[0]:
                return parsed_lines[0]
            else:
                return parsed_lines
        else:
            parsed_lines = [self._parse_line(line, variant="fields") for line in lines]
            return OrderedDict([[field, ranges] for field, ranges in parsed_lines])

    def get_error_rate(self, valid_ranges, ticket):
        return sum(
            value for value in ticket if not any(value in r for r in valid_ranges)
        )

    def identify_fields(self, fields, valid_tickets):
        field_items = list(fields.items())
        possible_mappings = {
            key: set(range(len(valid_tickets[0]))) for key in fields.keys()
        }
        for ticket in valid_tickets:
            for i, value in enumerate(ticket):
                for field, ranges in field_items:
                    if not any((value in r) for r in ranges):
                        possible_mappings[field].discard(i)

        changed = True
        while changed:
            changed = False
            knowns = {
                next(iter(i)): field
                for field, i in possible_mappings.items()
                if len(i) == 1
            }
            for field, indeces in possible_mappings.items():
                for index in list(indeces):
                    if index in knowns and knowns[index] != field:
                        changed = True
                        indeces.remove(index)

        if any(len(indeces) != 1 for indeces in possible_mappings.values()):
            return None
        else:
            return {
                field: indeces.pop() for field, indeces in possible_mappings.items()
            }

    def part_1(self):
        fields, _, other_tickets = self.inputs
        valid_ranges = []
        for field in fields.values():
            valid_ranges.extend(field)

        return sum(
            self.get_error_rate(valid_ranges, ticket) for ticket in other_tickets
        )

    def part_2(self):
        fields, my_ticket, other_tickets = self.inputs
        valid_ranges = []
        for field in fields.values():
            valid_ranges.extend(field)

        valid_tickets = [
            ticket
            for ticket in other_tickets
            if self.get_error_rate(valid_ranges, ticket) == 0
        ]
        valid_tickets.append(my_ticket)

        identified_fields = self.identify_fields(fields, valid_tickets)
        total = 1
        for field, index in identified_fields.items():
            if field.startswith("departure "):
                total *= my_ticket[index]

        return total


if __name__ == "__main__":
    Year2020Day16().print_results()

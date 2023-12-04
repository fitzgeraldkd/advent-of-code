import re

from classes.priority_queue import PriorityQueue
from solutions import BaseSolution


class Year2015Day19(BaseSolution):
    module_file = __file__

    def _parse_inputs(self):
        parsed_lines = super()._parse_inputs()
        molecule = parsed_lines.pop()
        parsed_lines.pop()
        replacements = [replacement.split(" => ") for replacement in parsed_lines]
        return replacements, molecule

    def part_1(self):
        replacements, molecule = self.inputs
        molecules = set()

        for replacement in replacements:
            matches = list(re.finditer(replacement[0], molecule))
            for match in matches:
                molecules.add(
                    molecule[: match.start()] + replacement[1] + molecule[match.end() :]
                )

        return len(molecules)

    def part_2(self):
        replacements, target = self.inputs
        queue = PriorityQueue()
        queue.add_item(target, len(target))

        steps = 0
        checked_molecules = set()
        while not queue.is_empty():
            steps += 1
            molecule = queue.pop()
            checked_molecules.add(molecule)

            for replacement in replacements:
                matches = list(re.finditer(replacement[1], molecule))
                for match in matches:
                    new_molecule = (
                        molecule[: match.start()]
                        + replacement[0]
                        + molecule[match.end() :]
                    )
                    if new_molecule in checked_molecules:
                        continue
                    if new_molecule == "e":
                        return steps
                    queue.add_item(new_molecule, len(new_molecule))


if __name__ == "__main__":
    Year2015Day19().print_results()

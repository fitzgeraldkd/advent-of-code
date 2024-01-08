from functools import reduce
import math

from solutions import BaseSolution


class Year2015Day24(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def get_permutations(self, weights, target, permutations, partial=[]):
        for index, weight in enumerate(weights):
            if sum(partial) + weight == target:
                permutations.append([*partial, weight])
            elif sum(partial) + weight < target:
                self.get_permutations(
                    weights[index + 1 :], target, permutations, [*partial, weight]
                )
        return permutations

    def part_1(self):
        inputs = self.inputs
        sleigh_weight = int(sum(inputs) / 3)

        permutations = self.get_permutations(inputs, sleigh_weight, [])

        min_count = math.inf
        min_quantum_entanglement = math.inf

        for permutation in permutations:
            if len(permutation) < min_count:
                min_count = len(permutation)
                # min_quantum_entanglement = math.prod(permutation)
                min_quantum_entanglement = reduce(lambda a, b: a * b, permutation)
            elif len(permutation) == min_count:
                # min_quantum_entanglement = min(min_quantum_entanglement, math.prod(permutation))
                min_quantum_entanglement = min(
                    min_quantum_entanglement, reduce(lambda a, b: a * b, permutation)
                )

        return min_quantum_entanglement

    def part_2(self):
        inputs = self.inputs
        sleigh_weight = int(sum(inputs) / 4)

        permutations = self.get_permutations(inputs, sleigh_weight, [])

        min_count = math.inf
        min_quantum_entanglement = math.inf

        for permutation in permutations:
            if len(permutation) < min_count:
                min_count = len(permutation)
                # min_quantum_entanglement = math.prod(permutation)
                min_quantum_entanglement = reduce(lambda a, b: a * b, permutation)
            elif len(permutation) == min_count:
                # min_quantum_entanglement = min(min_quantum_entanglement, math.prod(permutation))
                min_quantum_entanglement = min(
                    min_quantum_entanglement, reduce(lambda a, b: a * b, permutation)
                )

        return min_quantum_entanglement


if __name__ == "__main__":
    Year2015Day24().print_results()

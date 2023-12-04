from solutions import BaseSolution


class Year2015Day17(BaseSolution):
    TARGET_VOLUME = 150
    module_file = __file__

    def _parse_line(self, line: str):
        return int(line.strip())

    def count_permutations(self, containers, target, depth, solutions):
        containers = list(filter(lambda container: container <= target, containers))

        for i in range(len(containers)):
            if containers[i] == target:
                if depth in solutions:
                    solutions[depth] += 1
                else:
                    solutions[depth] = 1
            else:
                solutions = self.count_permutations(
                    containers[i + 1 :], target - containers[i], depth + 1, solutions
                )

        return solutions

    def part_1(self):
        solutions = self.count_permutations(self.inputs, self.TARGET_VOLUME, 1, {})
        return sum(solutions.values())

    def part_2(self):
        solutions = self.count_permutations(self.inputs, self.TARGET_VOLUME, 1, {})
        return solutions[min(solutions.keys())]


if __name__ == "__main__":
    Year2015Day17().print_results()

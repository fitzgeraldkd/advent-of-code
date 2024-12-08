from typing import List, Tuple

from solutions import BaseSolution


class Year2017Day12(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        program, connected_programs = line.strip().split(' <-> ')
        return int(program), [int(connected_program) for connected_program in connected_programs.split(', ')]

    def build_network(self, pipes: List[Tuple[int, List[int]]]):
        network = {}

        for program, connected_programs in pipes:
            network[program] = connected_programs

        return network

    def get_nodes_in_group(self, network, start):
        nodes_in_group = set()
        nodes_to_check = { start }

        while len(nodes_to_check) > 0:
            node_to_check = nodes_to_check.pop()
            nodes_in_group.add(node_to_check)
            for connected_program in network[node_to_check]:
                if connected_program not in nodes_in_group:
                    nodes_to_check.add(connected_program)

        return nodes_in_group

    def part_1(self):
        pipes = self.inputs
        network = self.build_network(pipes)

        return len(self.get_nodes_in_group(network, 0))

    def part_2(self):
        pipes = self.inputs
        network = self.build_network(pipes)

        nodes_to_check = set(network.keys())
        groups = 0

        while len(nodes_to_check) > 0:
            node_to_check = nodes_to_check.pop()
            group = self.get_nodes_in_group(network, node_to_check)
            for node in group:
                nodes_to_check.discard(node)

            groups += 1

        return groups


if __name__ == "__main__":
    Year2017Day12().print_results()

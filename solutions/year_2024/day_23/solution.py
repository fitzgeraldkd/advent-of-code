from collections import defaultdict

from solutions import BaseSolution


class Year2024Day23(BaseSolution):
    module_file = __file__

    def _parse_line(self, line):
        return super()._parse_line(line).split("-")

    # def get_networks(self, connections: dict):
    #     checked_computers = set()
    #     networks = []
    #     for computer in connections:
    #         checked_computers.add(computer)
    #     return networks

    def get_networks_recursive(self, connections: dict, partial_network: set, checked_computers: set):
        networks = [partial_network]
        checked_computers = set(checked_computers)

        partial_network_connections = [connections[c] for c in partial_network]
        common = set.intersection(*partial_network_connections)
        for computer in common:
            if computer in checked_computers:
                continue

            checked_computers.add(computer)
            new_networks = self.get_networks_recursive(connections, set([*partial_network, computer]), checked_computers)
            networks.extend(new_networks)

        return networks

    def part_1(self):
        networks = defaultdict(set)
        triangle_networks = set()

        for computer_a, computer_b in self.inputs:
            networks[computer_a].add(computer_b)
            networks[computer_b].add(computer_a)
            for computer in networks[computer_a]:
                if computer in networks[computer_b]:
                    triangle_networks.add(tuple(sorted([computer_a, computer_b, computer])))

        filtered_triangle_networks = [n for n in triangle_networks if any(c.startswith("t") for c in n)]
        return len(filtered_triangle_networks)

    def part_2(self):
        connections = defaultdict(set)

        for computer_a, computer_b in self.inputs:
            connections[computer_a].add(computer_b)
            connections[computer_b].add(computer_a)

        networks = []
        checked_computers = set()
        for computer in connections:
            checked_computers.add(computer)
            new_networks = self.get_networks_recursive(connections, set([computer]), checked_computers)
            networks.extend(new_networks)

        max_network = set()
        for network in networks:
            if len(network) > len(max_network):
                max_network = network

        return ",".join(sorted(max_network))


if __name__ == "__main__":
    Year2024Day23().print_results()

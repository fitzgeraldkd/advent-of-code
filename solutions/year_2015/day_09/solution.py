import math
import re

from classes.graph import Graph
from solutions import BaseSolution


def get_distances(
    graph, start: str, previous_key: tuple, distances, remaining_nodes: set
):
    previous_distance = distances[previous_key] if previous_key in distances else 0

    for node in graph.nodes[start].adjacent.keys():
        if node not in remaining_nodes:
            continue

        key = (*previous_key, node)

        distances[key] = previous_distance + graph.nodes[start].adjacent[node]

        sub_remaining_nodes = remaining_nodes.copy()
        sub_remaining_nodes.remove(node)
        get_distances(
            graph,
            start=node,
            previous_key=key,
            distances=distances,
            remaining_nodes=sub_remaining_nodes,
        )

    return distances


class Year2015Day09(BaseSolution):
    module_file = __file__

    def _parse_line(self, line: str):
        split_input = re.split(r" to | = ", line.strip())
        return {
            "start": split_input[0],
            "end": split_input[1],
            "distance": int(split_input[2]),
        }

    def part_1(self):
        inputs = self.inputs
        graph = Graph()
        locations = set()

        for input in inputs:
            locations.add(input["start"])
            locations.add(input["end"])
            graph.add_node(input["start"])
            graph.add_node(input["end"])
            graph.connect_nodes(input["start"], input["end"], input["distance"])

        distances = {}
        for node in graph.nodes.keys():
            distances = get_distances(
                graph,
                start=node,
                previous_key=(node,),
                distances=distances,
                remaining_nodes=set(filter(lambda n: n != node, graph.nodes.keys())),
            )

        min_distance = math.inf
        for key in distances.keys():
            if len(key) == len(locations) and distances[key] < min_distance:
                min_distance = distances[key]

        return min_distance

    def part_2(self):
        inputs = self.inputs
        graph = Graph()
        locations = set()

        for input in inputs:
            locations.add(input["start"])
            locations.add(input["end"])
            graph.add_node(input["start"])
            graph.add_node(input["end"])
            graph.connect_nodes(input["start"], input["end"], input["distance"])

        distances = {}
        for node in graph.nodes.keys():
            distances = get_distances(
                graph,
                start=node,
                previous_key=(node,),
                distances=distances,
                remaining_nodes=set(filter(lambda n: n != node, graph.nodes.keys())),
            )

        max_distance = 0
        for key in distances.keys():
            if len(key) == len(locations) and distances[key] > max_distance:
                max_distance = distances[key]

        return max_distance


if __name__ == "__main__":
    Year2015Day09().print_results()

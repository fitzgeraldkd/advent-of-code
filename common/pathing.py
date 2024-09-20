import math
import operator
from typing import List, Tuple

from classes.priority_queue import PriorityQueue

DIRECTIONS: List[Tuple[int, int]] = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_manhattan_distance(point_a, point_b):
    return sum(abs(vector) for vector in map(operator.sub, point_a, point_b))


def move(position, direction, magnitude=1):
    return tuple(
        map(operator.add, position, tuple(magnitude * vector for vector in direction))
    )


def rotate(facing: Tuple[int, int], rotation: str):
    direction_index = DIRECTIONS.index(facing)
    if rotation == "R":
        new_index = (direction_index + 1) % len(DIRECTIONS)
    else:
        new_index = (direction_index - 1) % len(DIRECTIONS)
    return DIRECTIONS[new_index]


def get_adjacent(position: Tuple[int, int]):
    return [tuple(map(operator.add, position, direction)) for direction in DIRECTIONS]


def a_star(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    get_is_wall,
    get_heuristic,
    progress=None,
):
    queue = PriorityQueue()
    previous = {}
    g_score = {start: 0}
    f_score = {start: get_heuristic(start, goal)}
    queue.add_item(start, f_score[start])

    while not queue.is_empty():
        current = queue.pop()

        if current == goal:
            path = []
            node = current
            while node != start:
                path.append(node)
                node = previous[node]
            path.append(start)
            return path

        for neighbor in get_adjacent(current):
            if get_is_wall(neighbor, current=current):
                continue
            neighbor_g_score = g_score[current] + 1
            if neighbor_g_score < g_score.get(neighbor, math.inf):
                previous[neighbor] = current
                g_score[neighbor] = neighbor_g_score
                f_score[neighbor] = neighbor_g_score + get_heuristic(neighbor, goal)
                if queue.has_item(neighbor):
                    queue.update_priority(neighbor, f_score[neighbor])
                else:
                    queue.add_item(neighbor, f_score[neighbor])

        if progress is not None:
            progress.update()

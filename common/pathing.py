import operator
from typing import List, Tuple

DIRECTIONS: List[Tuple[int, int]] = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def get_manhattan_distance(point_a, point_b):
    return sum(abs(vector) for vector in map(operator.sub, point_a, point_b))


def move(position, direction, magnitude=1):
    return tuple(map(operator.add, position, tuple(magnitude * vector for vector in direction)))


def rotate(facing, rotation):
    direction_index = DIRECTIONS.index(facing)
    if rotation == 'R':
        new_index = (direction_index + 1) % len(DIRECTIONS)
    else:
        new_index = (direction_index - 1) % len(DIRECTIONS)
    return DIRECTIONS[new_index]

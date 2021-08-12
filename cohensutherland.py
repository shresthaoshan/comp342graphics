from typing import Tuple

Coordinate = Tuple[float, float]

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def compare(point: Coordinate, min_point: Coordinate, max_point: Coordinate):
    x, y = point
    x_min, y_min = min_point
    x_max, y_max = max_point
    if x < x_min:
        return LEFT
    if x > x_max:
        return RIGHT
    if y < y_min:
        return BOTTOM
    if y > y_max:
        return TOP
    return INSIDE


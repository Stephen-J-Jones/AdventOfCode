def calc_taxi_distance(x, y):
    return abs(x) + abs(y)


MOVE_FACTORS = ((0, 1), (1, 0), (0, -1), (-1, 0))

NEW_DIRECTION = {
    "R": lambda old_direction: (old_direction + 1) % 4,
    "L": lambda old_direction: (old_direction - 1) % 4,
}


def distance_between_two_points(first, second):
    return calc_taxi_distance(first[0] - second[0], first[1] - second[1])

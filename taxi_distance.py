def calc_taxi_distance(x, y):
    return abs(x) + abs(y)


MOVE_FACTORS = ((0, 1), (1, 0), (0, -1), (-1, 0))

NEW_DIRECTION = {
    'R': lambda old_direction: (old_direction + 1) % 4,
    'L': lambda old_direction: (old_direction - 1) % 4,
}

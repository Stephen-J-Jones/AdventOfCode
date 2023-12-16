def calc_taxi_distance(x, y):
    return abs(x) + abs(y)


MOVE_FACTORS = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 0,0 is top left. 1,0 is one row down
MOVE_FACTORS_YX = ((-1, 0), (0, 1), (1, 0), (0, -1))

NEW_DIRECTION = {
    "R": lambda old_direction: (old_direction + 1) % 4,
    "L": lambda old_direction: (old_direction - 1) % 4,
}


def new_position_yx(old_position, direction):
    y, x = old_position
    y += MOVE_FACTORS_YX[direction][0]
    x += MOVE_FACTORS_YX[direction][1]
    return y, x


def distance_between_two_points(first, second):
    return calc_taxi_distance(first[0] - second[0], first[1] - second[1])

from shared import PUZZLE, read_lines
from taxi_distance import calc_taxi_distance, MOVE_FACTORS, NEW_DIRECTION


def navigate(directions):
    heading = 0
    x = 0
    y = 0
    visited = set('0,0')
    for step in [step.strip() for step in directions.split(',')]:
        turn = step[0]
        heading = NEW_DIRECTION[turn](heading)
        blocks = int(step[1:])
        for block in range(1, blocks + 1):
            x += MOVE_FACTORS[heading][0]
            y += MOVE_FACTORS[heading][1]
            if has_visited(visited, x, y):
                return calc_taxi_distance(x, y)


def has_visited(visited, x, y):
    key = f"{x},{y}"
    if key in visited:
        return True
    visited.add(key)
    return False


if __name__ == "__main__":
    for line in read_lines(PUZZLE):
        distance = navigate(line)
        print(distance)

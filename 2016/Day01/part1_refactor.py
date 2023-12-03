from shared import SAMPLE, PUZZLE, read_lines
from taxi_distance import MOVE_FACTORS, NEW_DIRECTION, calc_taxi_distance


def navigate(directions):
    heading = 0
    x = 0
    y = 0
    for step in [step.strip() for step in directions.split(',')]:
        turn = step[0]
        heading = NEW_DIRECTION[turn](heading)
        blocks = int(step[1:])
        x += blocks * MOVE_FACTORS[heading][0]
        y += blocks * MOVE_FACTORS[heading][1]
    return calc_taxi_distance(x, y)


if __name__ == "__main__":
    for line in read_lines(PUZZLE):
        distance = navigate(line)
        print(distance)

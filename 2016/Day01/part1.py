from shared import SAMPLE, PUZZLE, read_lines

test1 = "R2, L3"
test2 = "R2, R2, R2"
test3 = "R5, L5, R5, R3"


def navigate(directions):
    heading = 0
    x = 0
    y = 0
    for step in directions.split(', '):
        turn = step[0]
        blocks = int(step[1:])
        if turn == 'R':
            heading = (heading + 90) % 360
        else:
            heading = (heading - 90) % 360
        if heading == 0:
            y += blocks
        if heading == 90:
            x += blocks
        if heading == 180:
            y -= blocks
        if heading == 270:
            x -= blocks
    return abs(x) + abs(y)


if __name__ == "__main__":
    directions = [line for line in read_lines(PUZZLE)][0]
    distance = navigate(directions)
    print(distance)

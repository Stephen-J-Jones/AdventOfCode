from shared import SAMPLE, PUZZLE, read_lines

test1 = "R2, L3"
test2 = "R2, R2, R2"
test3 = "R5, L5, R5, R3"
test4 = "R8, R4, R4, R8"


def navigate(directions):
    heading = 0
    x = 0
    y = 0
    visited = {}
    visited['0,0'] = 0
    for step in directions.split(', '):
        turn = step[0]
        blocks = int(step[1:])
        if turn == 'R':
            heading = (heading + 90) % 360
        else:
            heading = (heading - 90) % 360
        if heading == 0:
            for block in range(1, blocks + 1):
                y += 1
                if has_visited(visited, x, y):
                    return taxi_distance(x, y)
        if heading == 90:
            for block in range(1, blocks + 1):
                x += 1
                if has_visited(visited, x, y):
                    return taxi_distance(x, y)
        if heading == 180:
            for block in range(1, blocks + 1):
                y -= 1
                if has_visited(visited, x, y):
                    return taxi_distance(x, y)
        if heading == 270:
            for block in range(1, blocks + 1):
                x -= 1
                if has_visited(visited, x, y):
                    return taxi_distance(x, y)


def has_visited(visited, x, y):
    key = f"{x},{y}"
    if key in visited:
        return True
    visited[key] = 1
    return False


def taxi_distance(x, y):
    return abs(x) + abs(y)


if __name__ == "__main__":
    directions = [line for line in read_lines(PUZZLE)][0]
    distance = navigate(directions)
    print(distance)

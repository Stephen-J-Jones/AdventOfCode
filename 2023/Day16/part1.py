import timeit

from shared import (
    PUZZLE,
    read_lines,
)
from taxi_distance import new_position_yx, NEW_DIRECTION


def new_direction_slash(old_direction):
    # /
    if (old_direction + 1) % 2 == 0:
        # turn left
        new_direction = NEW_DIRECTION["L"](old_direction)
    else:
        # turn right
        new_direction = NEW_DIRECTION["R"](old_direction)
    return new_direction


def new_direction_back_slash(old_direction):
    # \
    if (old_direction + 1) % 2 == 0:
        # turn right
        new_direction = NEW_DIRECTION["R"](old_direction)
    else:
        # turn left
        new_direction = NEW_DIRECTION["L"](old_direction)
    return new_direction


def new_direction_dash(beam):
    # -
    old_direction, y, x = beam
    if (old_direction + 1) % 2 == 0:
        # go straight
        return [beam]
    else:
        # split
        return [
            (NEW_DIRECTION["L"](old_direction), y, x),
            (NEW_DIRECTION["R"](old_direction), y, x),
        ]


def new_direction_pipe(beam):
    # |
    old_direction, y, x = beam
    if old_direction in [0, 2]:
        # go straight
        return [beam]
    else:
        # split
        return [
            (NEW_DIRECTION["L"](old_direction), y, x),
            (NEW_DIRECTION["R"](old_direction), y, x),
        ]


def do_puzzle():
    data = [l for l in read_lines(PUZZLE)]
    width = len(data[0])
    height = len(data)
    beams = [(1, 0, 0)]
    covered = set()
    pathways = set()
    while beams:
        new_beams = []
        for beam in beams:
            pathways.add(beam)
            direction, y, x = beam
            covered.add((y, x))
            c = data[y][x]
            match c:
                case ".":
                    turned_beams = [beam]
                case "/":
                    turned_beams = [(new_direction_slash(direction), y, x)]
                case "\\":
                    turned_beams = [(new_direction_back_slash(direction), y, x)]
                case "-":
                    turned_beams = new_direction_dash(beam)
                case "|":
                    turned_beams = new_direction_pipe(beam)
                case _:
                    raise Exception
            for nb in turned_beams:
                moved = nb[0], *new_position_yx((nb[1], nb[2]), nb[0])
                if moved in pathways:
                    continue
                if moved[1] in range(width) and moved[2] in range(height):
                    covered.add((moved[1], moved[2]))
                    new_beams.append(moved)
        beams = new_beams
    print(len(covered))


def read_into_dicts(columns, i, rows):
    for line in read_lines():
        for col_idx, c in enumerate(line):
            if c == ".":
                continue
            else:
                rows[i][col_idx] = c
                columns[col_idx][i] = c


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

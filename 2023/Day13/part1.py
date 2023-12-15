import timeit

from shared import (
    PUZZLE,
    read_lines,
)


def do_puzzle():
    patterns = []
    pattern = []
    for l in read_lines(PUZZLE):
        if not l:
            patterns.append(pattern)
            pattern = []
            continue
        pattern.append(l)
    patterns.append(pattern)
    left = 0
    above = 0
    for rows in patterns:
        columns = list(zip(*rows))
        above += find_reflection(rows)
        left += find_reflection(columns)
    print(f"{100*above+left}")


def find_reflection(rows):
    for idx, r in enumerate(rows[1:], start=1):
        if rows[idx - 1] == r:
            reflection = True
            for x in range(min(idx, len(rows) - idx)):
                if rows[idx - 1 - x] == rows[idx + x]:
                    continue
                reflection = False
                break
            if reflection:
                return idx
    return 0


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

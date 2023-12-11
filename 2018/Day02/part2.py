import timeit
from itertools import combinations

from shared import (
    PUZZLE,
    read_lines,
)


def do_puzzle():
    data = [line for line in read_lines(PUZZLE)]
    for pair in combinations(data, 2):
        common = []
        diff = []
        for idx, c in enumerate(pair[0]):
            if pair[1][idx] == c:
                common.append(c)
            else:
                diff.append(c)
        if len(common) == len(pair[0]) - 1:
            print("".join(common))
            break


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

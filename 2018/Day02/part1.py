import timeit
from collections import Counter

from shared import (
    PUZZLE,
    read_lines,
)


def do_puzzle():
    twice = 0
    thrice = 0
    for line in read_lines(PUZZLE):
        ctr = Counter(line)
        twice += 1 if len([a for a, b in ctr.items() if b == 2]) else 0
        thrice += 1 if len([a for a, b in ctr.items() if b == 3]) else 0
    print(twice * thrice)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

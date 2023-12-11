import re
import timeit
from itertools import combinations
from shared import (
    SAMPLE,
    PUZZLE,
    read_lines,
    find_all_numbers_in_string,
    find_all_digits_in_string,
)
from taxi_distance import distance_between_two_points

GAL = "#"
SPC = "."

SPACE_TO_ADD = 999


def do_puzzle():
    universe = [list(l) for l in read_lines(PUZZLE)]
    insert_cols = []
    for c in range(len(universe[0]) - 1, -1, -1):
        col = [l[c] for l in universe]
        if GAL not in col:
            insert_cols.append(c)
    for c in insert_cols:
        for l in universe:
            for w in range(SPACE_TO_ADD):
                l.insert(c + 1, SPC)
    insert_rows = []
    for idx, l in enumerate(universe):
        if GAL not in l:
            insert_rows.append(idx)
    for r in insert_rows[::-1]:
        for w in range(SPACE_TO_ADD):
            universe.insert(r + 1, [SPC] * len(universe[r]))
    galaxies = []
    for idx, l in enumerate(universe):
        galaxies.extend([(idx, i) for i, x in enumerate(l) if x == GAL])
    distances = []
    for first, second in combinations(galaxies, 2):
        distances.append(distance_between_two_points(first, second))
    print(sum(distances))


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

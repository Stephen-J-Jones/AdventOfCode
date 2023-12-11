import timeit
from itertools import combinations

from shared import (
    PUZZLE,
    read_lines,
)
from taxi_distance import distance_between_two_points

GAL = "#"
SPC = "."
SPACE_TO_ADD = 999999


def do_puzzle():
    all_galaxies = []
    insert_rows = []
    row_idx = 0
    insert_cols = None
    for line in read_lines(PUZZLE):
        if insert_cols is None:
            insert_cols = set([i for i in range(len(line))])
        row = list(line)
        galaxies = [[row_idx, i] for i, c in enumerate(row) if c == GAL]
        all_galaxies.extend(galaxies)
        if not galaxies:
            insert_rows.append(row_idx)
        insert_cols = insert_cols - set([g[1] for g in galaxies])
        row_idx += 1
    for gal in all_galaxies:
        gal[0] += len([i for i in insert_rows if i < gal[0]]) * SPACE_TO_ADD
        gal[1] += len([i for i in insert_cols if i < gal[1]]) * SPACE_TO_ADD
    distances = []
    for first, second in combinations(all_galaxies, 2):
        distances.append(distance_between_two_points(first, second))
    print(sum(distances))


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

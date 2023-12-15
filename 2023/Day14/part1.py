import re
import timeit

from shared import (
    PUZZLE,
    read_lines,
)


def do_puzzle():
    data = [l for l in read_lines(PUZZLE)]
    as_columns = ["".join(col) for col in zip(*data)][::-1]
    total_weight = 0
    m = []
    for column in as_columns:
        cubes = re.finditer(r"#", column + "#")
        start = 0
        new_column = []
        for cube in cubes:
            cnt_O = column[start : cube.start()].count("O")
            cnt_dots = column[start : cube.start()].count(".")
            new_column += (
                "O" * cnt_O + "." * cnt_dots + "#" * (cube.end() - cube.start())
            )
            start = cube.end()
        total_weight += sum(
            [len(column) - i for i, v in enumerate(new_column) if v == "O"]
        )
        m.append(new_column[:-1])
    print(total_weight)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

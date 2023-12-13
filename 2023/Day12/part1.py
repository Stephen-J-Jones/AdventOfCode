import re
import timeit

from shared import (
    PUZZLE,
    read_lines,
)


def do_puzzle():
    a = 0
    for l in read_lines(PUZZLE):
        sketch, damaged = l.split(" ")
        damaged = tuple(map(int, damaged.split(",")))
        questions = [m for m in re.finditer(r"\?", sketch)]
        mask_format = f"{{:0{len(questions)}b}}"
        for i in range(2 ** len(questions)):
            trial = sketch
            mask = mask_format.format(i)
            for cnt, idx in enumerate(questions):
                if mask[cnt] == "1":
                    trial = trial[: idx.start()] + "#" + trial[idx.start() + 1 :]
            test = tuple(map(len, re.findall(r"#+", trial)))
            if damaged == test:
                a += 1
    print(a)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

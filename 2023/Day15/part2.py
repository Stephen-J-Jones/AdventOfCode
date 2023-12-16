import functools
import timeit

from shared import (
    PUZZLE,
    read_lines,
)


def hash_string(s):
    current_value = 0
    for c in s:
        ascii = ord(c)
        current_value += ascii
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value


def do_puzzle():
    data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    data = "".join([l for l in read_lines(PUZZLE)])
    boxes = [dict() for i in range(256)]
    for step in data.split(","):
        if "=" in step:
            # add
            label, lens = step.split("=")
            boxes[hash_string(label)][label] = int(lens)
        if "-" in step:
            label, lens = step.split("-")
            boxes[hash_string(label)].pop(label, None)
    total = 0
    for idx, box in enumerate(boxes, start=1):
        keys = list(box.keys())
        total += sum([(keys.index(key) + 1) * val * idx for key, val in box.items()])
    print(total)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

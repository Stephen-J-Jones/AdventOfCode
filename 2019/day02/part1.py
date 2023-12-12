import timeit

from shared import (
    PUZZLE,
    read_lines,
)

ptr_move = {
    1: 4,
    2: 4,
    99: 1,
}

operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
}


def do_puzzle():
    program = [int(c) for c in [l.split(",") for l in read_lines(PUZZLE)][0]]
    program[1] = 12
    program[2] = 2
    i = 0
    while i < len(program):
        if program[i] == 99:
            print(program[0])
            break
        op_code, x, y, addr = program[i : i + ptr_move[program[i]]]
        program[addr] = operations[op_code](program[x], program[y])
        i += ptr_move[op_code]


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

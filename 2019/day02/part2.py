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

TARGET = 19690720


def do_puzzle():
    program_original = [int(c) for c in [l.split(",") for l in read_lines(PUZZLE)][0]]
    done = False
    for noun in range(100):
        if done:
            break
        for verb in range(100):
            if done:
                break
            program = program_original.copy()
            program[1] = noun
            program[2] = verb
            i = 0
            while i < len(program):
                if program[i] == 99:
                    if program[0] == TARGET:
                        print(f"DONE ** {100*noun+verb} **")
                        done = True
                    break
                op_code, x, y, addr = program[i : i + ptr_move[program[i]]]
                program[addr] = operations[op_code](program[x], program[y])
                i += ptr_move[op_code]


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

import timeit

from shared import (
    SAMPLE,
    PUZZLE,
    read_lines,
    find_all_numbers_in_string,
    find_all_digits_in_string,
)


def do_puzzle():
    valid = 0
    for line in read_lines(PUZZLE):
        policy, password = line.split(":")
        rng, char = policy.split(" ")
        lwr, upr = tuple(map(abs, find_all_numbers_in_string(rng)))
        if password.count(char) in range(lwr, upr + 1):
            valid += 1
    print(valid)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

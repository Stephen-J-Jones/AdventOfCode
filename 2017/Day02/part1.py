import timeit

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string, find_all_digits_in_string


def do_puzzle():
    checksum = 0
    for line in read_lines(PUZZLE):
        numbers = find_all_numbers_in_string(line)
        checksum += max(numbers) - min(numbers)
    print(checksum)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10 ** 3
    print(f"{exec_time:.03f}ms")

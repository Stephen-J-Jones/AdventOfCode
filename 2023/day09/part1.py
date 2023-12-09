import timeit

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string, find_all_digits_in_string


def get_diffs(numbers):
    if set(numbers) == {0}:
        return 0
    diffs = []
    for i in range(1, len(numbers)):
        diffs.append(numbers[i] - numbers[i - 1])
    return numbers[-1] + get_diffs(diffs)


def do_puzzle():
    finals = []
    for line in read_lines(PUZZLE):
        numbers = find_all_numbers_in_string(line)
        finals.append(get_diffs(numbers))
    print(sum(finals))


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10 ** 3
    print(f"{exec_time:.03f}ms")

import timeit

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string, find_all_digits_in_string

KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

MOVES = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


def do_puzzle():
    start = [1, 1]
    code = []
    for line in read_lines(PUZZLE):
        for c in line:
            move = MOVES[c]
            start[0] = min(max(start[0] + move[0], 0), 2)
            start[1] = min(max(start[1] + move[1], 0), 2)
        code.append(KEYPAD[start[0]][start[1]])
    print(code)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10 ** 3
    print(f"{exec_time:.03f}ms")

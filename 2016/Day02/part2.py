import timeit

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string, find_all_digits_in_string

KEYPAD = ['LL1RR', 'L234R', '56789', 'LABCR', 'LLDRR', ]
MOVES = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


def do_puzzle():
    position = [2, 0]
    code = []
    for line in read_lines(PUZZLE):
        for c in line:
            move = MOVES[c]
            y = min(max(position[0] + move[0], 0), 4)
            if KEYPAD[y][position[1]] not in ['L', 'R']:
                position[0] = y
            x = min(max(position[1] + move[1], 0), 4)
            if KEYPAD[position[0]][x] not in ['L', 'R']:
                position[1] = x
        code.append(KEYPAD[position[0]][position[1]])
    print(''.join(code))


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10 ** 3
    print(f"{exec_time:.03f}ms")

import timeit

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string


def do_puzzle():
    races = []
    for line in read_lines(PUZZLE):
        races.append(find_all_numbers_in_string(line))
    time = int("".join([str(n) for n in races[0]]))
    distance = int("".join([str(n) for n in races[1]]))
    ways_to_win = 0
    for s in range(time):
        new_d = s * (time - s)
        if new_d > distance:
            ways_to_win += 1
    print(ways_to_win)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10 ** 3
    print(f"{exec_time:.03f}ms")

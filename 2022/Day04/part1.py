from shared import read_lines


def is_a_in_b(a, b):
    return a[0] >= b[0] and a[-1] <= b[-1]


if __name__ == '__main__':
    # data = [
    #     "2-4,6-8",
    #     "2-3,4-5",
    #     "5-7,7-9",
    #     "2-8,3-7",
    #     "6-6,4-6",
    #     "2-6,4-8",
    # ]
    data = read_lines('puzzle_input.txt')
    counter = 0
    for line in data:
        split_line = line.split(",")
        split_a = [int(x) for x in split_line[0].split("-")]
        split_b = [int(x) for x in split_line[1].split("-")]
        range_a = range(split_a[0], split_a[1] + 1)
        range_b = range(split_b[0], split_b[1] + 1)
        if is_a_in_b(range_a, range_b) or is_a_in_b(range_b, range_a):
            counter += 1
    print(counter)

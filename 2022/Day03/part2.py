from part1 import points
from shared import read_lines, chunked_iterable

if __name__ == "__main__":
    # data = [
    #     "vJrwpWtwJgWrhcsFMMfFFhFp",
    #     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #     "PmmdzqPrVvPwwTWBwg",
    #     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #     "ttgJtRGJQctTZtZT",
    #     "CrZsJsPPZsGzwwsLwLmpwMDw",
    # ]
    data = read_lines('puzzle_input.txt')
    total = 0
    for chunk in chunked_iterable(data, 3):
        a = set(chunk[0])
        b = set(chunk[1])
        c = set(chunk[2])
        common = a & b & c
        total += points(common.pop())
    print(total)

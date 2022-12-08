from shared import read_lines
def points(char:str):
    if char.islower():
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27


if __name__ == '__main__':
    # data = ["vJrwpWtwJgWrhcsFMMfFFhFp",
    #         "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    #         "PmmdzqPrVvPwwTWBwg",
    #         "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    #         "ttgJtRGJQctTZtZT",
    #         "CrZsJsPPZsGzwwsLwLmpwMDw", ]
    data = read_lines('puzzle_input.txt')
    total = 0
    for d in data:
        left = set(d[:len(d) // 2])
        right = set(d[len(d) // 2:])
        total += points((left & right).pop())
    print(total)

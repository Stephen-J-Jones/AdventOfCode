import time

from shared import SAMPLE, read_lines, find_all_numbers_in_string, PUZZLE


class Num:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.val = val
        self.right = right


DECRYPTION_KEY = 811589153


def read_into_data_structures():
    instructions = []
    ordered = []
    for line in read_lines(PUZZLE):
        val = find_all_numbers_in_string(line)[0]
        num = Num(val * DECRYPTION_KEY)
        instructions.append(num)
        ordered.append(num)
    for i in range(len(instructions)):
        instructions[i].left = instructions[i - 1] if i > 0 else instructions[-1]
        instructions[i].right = instructions[i + 1] if i < len(instructions) - 1 else instructions[0]
    return instructions


def reorder():
    instructions = read_into_data_structures()
    count = len(instructions) - 1
    for mix in range(10):
        for instruction in instructions:
            new_right = instruction.right
            new_right.left = instruction.left
            instruction.left.right = new_right
            for i in range(instruction.val % count):
                new_right = new_right.right
            instruction.left = new_right.left
            instruction.right = new_right
            new_right.left = instruction
            instruction.left.right = instruction
    return instructions


FIRST = 1000
SECOND = 2000
THIRD = 3000


def get_coordinates():
    ordered = reorder()
    start = next(x for x in ordered if x.val == 0)
    count = len(ordered)
    first = get_nth_number(FIRST, count, start)
    second = get_nth_number(SECOND, count, start)
    third = get_nth_number(THIRD, count, start)
    return sum([first, second, third])


def get_nth_number(n, count, start):
    num = start
    for i in range(n % count):
        num = num.right
    return num.val


if __name__ == "__main__":
    print(get_coordinates())

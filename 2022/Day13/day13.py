import json

from shared import read_lines, PUZZLE, SAMPLE


def are_in_order(pair: list) -> bool:
    first = json.loads(pair[0])
    second = json.loads(pair[1])
    return check_first_smaller(first, second)


def check_first_smaller(first, second):
    for i in range(len(first)):
        left = first[i]
        try:
            right = second[i]
        except IndexError:
            return False
        if isinstance(left, int) and isinstance(right, int):
            if left > right:
                return False
            if left < right:
                return True
            if left == right:
                continue
        if isinstance(left, list) and isinstance(right, int):
            return check_first_smaller(left, [right])
        if isinstance(left, int) and isinstance(right, list):
            return check_first_smaller([left], right)
        if isinstance(left, list) and isinstance(right, list):
            if len(left) == len(right) == 0:
                continue
            return check_first_smaller(left, right)
    if len(first) < len(second):
        return True


def count_in_order():
    count = 0
    vertex = 1
    data = read_lines(PUZZLE)
    pair = []
    for line in data:
        if not line:
            if are_in_order(pair):
                count += vertex
            pair = []
            vertex += 1
            continue
        pair.append(line)
    return count


def arrange_in_order():
    DIV1 = "[[2]]"
    DIV2 = "[[6]]"
    arranged = [DIV1, DIV2]
    data = read_lines(PUZZLE)
    pair = []
    for line in data:
        if not line:
            continue
        for i in range(len(arranged)):
            if are_in_order([line, arranged[i]]):
                arranged.insert(i, line)
                break
        else:
            arranged.append(line)
            continue
    return (arranged.index(DIV1) + 1) * (arranged.index(DIV2) + 1)


if __name__ == "__main__":
    print(count_in_order())
    print(arrange_in_order())

from shared import read_lines, SAMPLE, PUZZLE, find_all_digits_in_string

integers = [str(x) for x in range(1, 10)]
int_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_to_find = integers + int_names


def extract_digits_from_string(line):
    inline = {}
    for name in numbers_to_find:
        inline[line.find(name)] = name
        inline[line.rfind(name)] = name
    del (inline[-1])
    sorted_keys = sorted(inline)
    first = inline[sorted_keys[0]]
    last = inline[sorted_keys[-1]]
    if first in int_names:
        first = int_names.index(first) + 1
    if last in int_names:
        last = int_names.index(last) + 1
    return [int(first), int(last)]


if __name__ == "__main__":
    result = 0
    for line in read_lines(PUZZLE):
        numbers = extract_digits_from_string(line)
        result += 10 * numbers[0] + numbers[-1]
    print(result)

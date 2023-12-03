import re

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string


def is_symbol(char):
    return char != '.' and not char.isnumeric()


def build_diagram():
    line_index = 0
    numbers = {}
    symbols = set()
    for line in read_lines(PUZZLE):
        numbers[line_index] = {}
        col_index = 0
        for char in line:
            if char.isnumeric():
                numbers[line_index][col_index] = char
            if is_symbol(char):
                symbols.add(f"{line_index}:{col_index}")
            col_index += 1
        line_index += 1
    return numbers, symbols


def remap_numbers(numbers):
    new_numbers = {}
    for line_index, line_numbers in numbers.items():
        if not line_numbers:
            continue
        new_numbers[line_index] = {}
        indices = sorted(line_numbers)
        current_ptr = indices[0]
        previous_index = indices[0]
        for col_index in indices:
            if previous_index - col_index == 0:
                new_numbers[line_index][current_ptr] = line_numbers[col_index]
                previous_index = col_index
            elif col_index - previous_index == 1:
                new_numbers[line_index][current_ptr] += line_numbers[col_index]
                previous_index = col_index
            else:
                current_ptr = col_index
                previous_index = col_index
                new_numbers[line_index][current_ptr] = line_numbers[col_index]
    return new_numbers


def numbers_next_to_symbols(numbers, symbols):
    number_list = []
    for row_index, line_numbers in numbers.items():
        for col_index, number in line_numbers.items():
            for r in range(row_index - 1, row_index + 2):
                for c in range(col_index - 1, col_index + 1 + len(number)):
                    if f"{r}:{c}" in symbols:
                        number_list.append(int(number))
                        break
    return number_list


if __name__ == "__main__":
    numbers, symbols = build_diagram()
    remapped_numbers = remap_numbers(numbers)
    print(sum(numbers_next_to_symbols(remapped_numbers, symbols)))

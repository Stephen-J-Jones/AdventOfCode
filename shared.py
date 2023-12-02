import itertools
import re


def read_lines(file_name):
    with open(file_name, 'r') as data_file:
        for line in data_file:
            yield line.strip('\n')


def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


SAMPLE = "sample_input.txt"
PUZZLE = "puzzle_input.txt"


def find_all_numbers_in_string(line):
    return [int(x) for x in re.findall(r"-?\d+", line)]


def find_all_digits_in_string(line):
    return [int(x) for x in re.findall(r"\d", line)]

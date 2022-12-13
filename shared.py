import itertools


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
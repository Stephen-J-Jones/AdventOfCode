import itertools


def read_lines(file_name):
    with open(file_name, 'r') as calorie_file:
        for line in calorie_file:
            yield line.strip('\n')


def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk

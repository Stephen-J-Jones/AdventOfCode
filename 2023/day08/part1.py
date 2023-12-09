import re
import timeit

from shared import SAMPLE, PUZZLE, read_lines

L = 'L'
R = 'R'


def read_node(line, nodes):
    element_names = re.findall(r'[A-Z]+', line)
    node = {"name": element_names[0], L: element_names[1], R: element_names[2]}
    nodes[element_names[0]] = node


def do_puzzle():
    read_nodes = False
    nodes = {}
    steps = ''

    for line in read_lines(PUZZLE):
        if read_nodes:
            read_node(line, nodes)
            continue
        if not line:
            read_nodes = True
            continue
        steps = line
    node = nodes['AAA']
    i = 0
    while node["name"] != 'ZZZ':
        direction = steps[i % len(steps)]
        node = nodes[node[direction]]
        i += 1
    print(i)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10 ** 3
    print(f"{exec_time:.03f}ms")

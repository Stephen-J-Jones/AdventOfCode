import timeit

from shared import (
    SAMPLE,
    PUZZLE,
    read_lines,
    find_all_numbers_in_string,
    find_all_digits_in_string,
)

U = "U"
D = "D"
L = "L"
R = "R"

MOVES = {
    L: (0, -1),
    R: (0, 1),
    U: (-1, 0),
    D: (1, 0),
}


class Pipe:
    def __init__(self, exits, node, entry):
        self._exits = exits
        self._entries = [k for k in exits.keys()]
        self.node = node
        self.entry = entry

    def entry_allowed(self, direction):
        return direction in self._entries

    def exit(self):
        return self._exits.get(self.entry)

    def next_node(self):
        ext = self.exit()
        new_node = [self.node[0] + MOVES[ext][0], self.node[1] + MOVES[ext][1]]
        return new_node, ext


START = "S"
LR = "-"
TR = "7"
EMPTY = "."
TB = "|"
BL = "L"
BR = "J"
TL = "F"

PIPES = {
    LR: lambda node, entry: Pipe({R: R, L: L}, node, entry),
    TB: lambda node, entry: Pipe({U: U, D: D}, node, entry),
    TR: lambda node, entry: Pipe({R: D, U: L}, node, entry),
    TL: lambda node, entry: Pipe({L: D, U: R}, node, entry),
    BL: lambda node, entry: Pipe({D: R, L: U}, node, entry),
    BR: lambda node, entry: Pipe({D: L, R: U}, node, entry),
    EMPTY: lambda node, entry: Pipe({}, node, entry),
    START: lambda node, entry: Pipe({}, node, entry),
}


def build_map():
    lines = []
    i = 0
    start = []
    for line in read_lines(PUZZLE):
        lines.append(line)
        if START in line:
            start = [i, line.index(START)]
        i += 1
    return lines, start


def first_move(node, sketch):
    for potential_move in [m for m in MOVES.keys()]:
        potential_node = [
            min(len(sketch), max(0, node[0] + MOVES[potential_move][0])),
            min(len(sketch[node[0]]), max(0, node[1] + MOVES[potential_move][1])),
        ]
        pipe = PIPES[sketch[potential_node[0]][potential_node[1]]](
            potential_node, potential_move
        )
        if pipe.entry_allowed(potential_move):
            return pipe


def do_puzzle():
    sketch, start = build_map()
    pipe = first_move(start, sketch)
    i = 1
    while pipe.node != start:
        node, ext = pipe.next_node()
        pipe = PIPES[sketch[node[0]][node[1]]](node, ext)
        i += 1
    print(i // 2)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

import timeit

from shared import (
    SAMPLE,
    PUZZLE,
    read_lines,
    find_all_numbers_in_string,
    find_all_digits_in_string,
)

from matplotlib.path import Path

BOX_HLINE = "─"
BOX_LINES = "S─│└┘┌┐"
BOX_EDGE = "│└┘┌┐"

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

START = "S"
LR = "-"
TR = "7"
EMPTY = "."
TB = "|"
BL = "L"
BR = "J"
TL = "F"

char_mapping = {
    START: "S",
    LR: "─",
    TR: "┐",
    EMPTY: ".",
    TB: "│",
    BL: "└",
    BR: "┘",
    TL: "┌",
}


class Pipe:
    def __init__(self, exits, node, entry, char):
        self._exits = exits
        self._entries = [k for k in exits.keys()]
        self.node = node
        self.entry = entry
        self.char = char

    def entry_allowed(self, direction):
        return direction in self._entries

    def exit(self):
        return self._exits.get(self.entry)

    def next_node(self):
        ext = self.exit()
        new_node = [self.node[0] + MOVES[ext][0], self.node[1] + MOVES[ext][1]]
        return new_node, ext

    def box_char(self):
        return char_mapping[self.char]


PIPES = {
    LR: lambda node, entry: Pipe({R: R, L: L}, node, entry, LR),
    TB: lambda node, entry: Pipe({U: U, D: D}, node, entry, TB),
    TR: lambda node, entry: Pipe({R: D, U: L}, node, entry, TR),
    TL: lambda node, entry: Pipe({L: D, U: R}, node, entry, TL),
    BL: lambda node, entry: Pipe({D: R, L: U}, node, entry, BL),
    BR: lambda node, entry: Pipe({D: L, R: U}, node, entry, BR),
    EMPTY: lambda node, entry: Pipe({}, node, entry, EMPTY),
    START: lambda node, entry: Pipe({}, node, entry, START),
}


def build_map():
    lines = []
    i = 0
    start = []
    for line in read_lines(PUZZLE):
        lines.append([c for c in line])
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


# ┌ ─ ┐ │ ┌ ─ ┘#
def do_puzzle():
    sketch, start = build_map()
    pipe = first_move(start, sketch)
    i = 1
    poly = []
    poly.append([*start][::-1])
    while pipe.node != start:
        poly.append([*pipe.node][::-1])
        node, ext = pipe.next_node()
        pipe = PIPES[sketch[node[0]][node[1]]](node, ext)
        sketch[node[0]][node[1]] = pipe.box_char()
        i += 1
    path = Path(poly)
    area = 0
    for y in range(len(sketch)):
        for x in range(len(sketch[0])):
            if [x, y] in poly:
                continue
            if path.contains_point((x, y)):
                area += 1
    print(area)
    # new_sketch = []
    # fill = [EMPTY, "X"]
    # for line in sketch:
    #     inner = False
    #     new_line = ""
    #     for c in line:
    #         if c in BOX_LINES:
    #             new_line += c
    #             inner = not inner
    #         elif c not in BOX_LINES:
    #             new_line += fill[inner]
    #         else:
    #             new_line += fill[inner]
    #     new_sketch.append(new_line)
    # for l in new_sketch:
    #     print(l)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

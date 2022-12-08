import re
from collections import defaultdict

from shared import read_lines

if __name__ == "__main__":
    # data = (l for l in [
    #     "    [D]",
    #     "[N] [C]",
    #     "[Z] [M] [P]",
    #     " 1   2   3",
    #     "",
    #     "move 1 from 2 to 1",
    #     "move 3 from 1 to 3",
    #     "move 2 from 2 to 1",
    #     "move 1 from 1 to 2", ]
    #         )
    data = read_lines('puzzle_input.txt')
    stacks = defaultdict(list)
    for line in data:
        if not line:
            break
        if "[" not in line:
            break
        for index, crate in enumerate([line[i:i + 4] for i in range(0, len(line), 4)]):
            for c in "[] ":
                crate = crate.replace(c, "")
            if crate:
                stacks[index + 1].insert(0, crate)
    stacks = dict(sorted(stacks.items()))
    for line in data:
        if not line:
            continue
        cnt, frm, to = [int(x) for x in re.findall(r"\d+", line)]
        for i in range(cnt):
            stacks[to].append(stacks[frm].pop())
    tops = ""
    for val in stacks.values():
        tops += (val[-1])
    print(tops)

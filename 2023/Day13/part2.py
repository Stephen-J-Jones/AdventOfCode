import timeit

from shared import (
    PUZZLE,
    read_lines,
)


def do_puzzle():
    patterns = []
    pattern = []
    for l in read_lines(PUZZLE):
        if not l:
            patterns.append(pattern)
            pattern = []
            continue
        pattern.append(l)
    patterns.append(pattern)
    left = 0
    above = 0
    for rows in patterns:
        columns = list(zip(*rows))
        findings = {"A": find_reflection(rows, 0), "L": find_reflection(columns, 0)}
        findings2 = {"A": find_reflection(rows, 1), "L": find_reflection(columns, 1)}
        left += findings2["L"] if findings2["L"] != findings["L"] else 0
        above += findings2["A"] if findings2["A"] != findings["A"] else 0
    print(f"{100*above+left}")


def find_reflection(lines, diff_allowed):
    for idx, line in enumerate(lines[1:], start=1):
        allowed_diff = diff_allowed
        if (diff := fuzzy_match(lines[idx - 1], line)) <= allowed_diff:
            if diff == diff_allowed:
                allowed_diff = 0
            reflection = True
            for x in range(1, min(idx, len(lines) - idx)):
                if (
                    diff := fuzzy_match(lines[idx - 1 - x], lines[idx + x])
                ) <= allowed_diff:
                    if diff == diff_allowed:
                        allowed_diff = 0
                    continue
                reflection = False
                break
            if reflection and allowed_diff == 0:
                return idx
    return 0


def fuzzy_match(line1, line2):
    diffs = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            diffs += 1
    return diffs


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

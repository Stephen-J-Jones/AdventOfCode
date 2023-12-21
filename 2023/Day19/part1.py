import timeit

from shared import (
    PUZZLE,
    read_lines,
)


def parse_instructions(instruction_lines):
    instructions = {}
    for l in instruction_lines:
        key, value = l.split("{")
        check_strings = value[:-1].split(",")
        checks = []
        for check in check_strings:
            if "<" in check:
                op, destination = check.split(":")
                k, v = op.split("<")
                checks.append(
                    lambda part, _k=k, _v=v, _d=destination: _d
                    if part[_k] < int(_v)
                    else None,
                )
            elif ">" in check:
                op, destination = check.split(":")
                k, v = op.split(">")
                checks.append(
                    lambda part, _k=k, _v=v, _d=destination: _d
                    if part[_k] > int(_v)
                    else None,
                )
            else:
                checks.append(lambda part, _check=check: (_check))
        instructions[key] = checks
    return instructions


def parse_part(part_string):
    part = {}
    for piece in part_string[1:-1].split(","):
        k, v = piece.split("=")
        part[k] = int(v)
    return part


def read_input():
    instruction_lines = []
    parts = []
    put_in_parts = False
    for l in read_lines(PUZZLE):
        if l == "":
            put_in_parts = True
            continue
        if put_in_parts:
            parts.append(l)
        else:
            instruction_lines.append(l)
    return parse_instructions(instruction_lines), [parse_part(part) for part in parts]


def get_op_result(part, current, instructions):
    for op in current:
        next_key = op(part)
        if next_key in ["A", "R"]:
            return next_key
        if next_key is not None:
            return get_op_result(part, instructions[next_key], instructions)


def do_puzzle():
    instructions, parts = read_input()
    accepted_parts = []
    for part in parts:
        current = instructions["in"]
        result = get_op_result(part, current, instructions)
        if result == "A":
            accepted_parts.append(part)
    total = 0
    for part in accepted_parts:
        total += sum([v for v in part.values()])
    print(total)


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

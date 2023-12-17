import timeit

from shared import (
    SAMPLE,
    PUZZLE,
    read_lines,
    find_all_numbers_in_string,
    find_all_digits_in_string,
)

ROOT = "root"
HUMAN = "humn"

operations = {
    "+": lambda monkeys, a, b: lambda: monkeys[a]() + monkeys[b](),
    "-": lambda monkeys, a, b: lambda: monkeys[a]() - monkeys[b](),
    "/": lambda monkeys, a, b: lambda: monkeys[a]() // monkeys[b](),
    "*": lambda monkeys, a, b: lambda: monkeys[a]() * monkeys[b](),
    "==": lambda monkeys, a, b: lambda: monkeys[a]() == monkeys[b](),
}

inverse_operations = {
    "+": lambda monkeys, a, b: lambda: b - monkeys[a](),
    "-": lambda monkeys, a, b: lambda: b + monkeys[a](),
    "/": lambda monkeys, a, b: lambda: b * monkeys[a](),
    "*": lambda monkeys, a, b: lambda: b // monkeys[a](),
}


def do_puzzle():
    raw_monkeys = {}
    monkeys = {}
    root_a = ""
    root_b = ""
    for l in read_lines(PUZZLE):
        key, instruction = l.split(": ")
        raw_monkeys[key] = instruction
        if instruction.strip().isnumeric():
            monkeys[key.strip()] = lambda number=instruction: int(number)
        else:
            key1, operation, key2 = instruction.strip().split(" ")
            if key == ROOT:
                operation = "=="
                root_a = key1
                root_b = key2
            monkeys[key] = operations[operation](monkeys, key1, key2)
    path = [(HUMAN,)] + [(k, v) for k, v in raw_monkeys.items() if HUMAN in v]
    while True:
        if path[-1][0] == ROOT:
            break
        y = [(k, v) for k, v in raw_monkeys.items() if path[-1][0] in v]
        if len(y) == 1:
            path.extend(y)
        else:
            raise Exception
    # key1, operation, key2 = path[-1][1].strip().split(" ")
    # fixed_key = [k for k in [key1, key2] if k != path[-2][0]][0]
    # target = monkeys[fixed_key]()
    target = 0
    path.reverse()
    for i, monkey in enumerate(path):
        if monkey[0] == HUMAN:
            break
        key1, operation, key2 = monkey[1].strip().split(" ")
        fixed_key = [k for k in [key1, key2] if k != path[i + 1][0]][0]
        val = monkeys[fixed_key]()
        print(f"{target} {operation} {val}")
        target = inverse_operations[operation](monkeys, fixed_key, target)()
    for i in range(target, 7172286853922):
        monkeys[HUMAN] = lambda _i=i: _i
        if monkeys[ROOT]():
            print(monkeys["zmvq"]())
            print(monkeys["dbcq"]())
            print(i)
            break


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")


# 7172286853922
# 3349136380742
# 3349136380742

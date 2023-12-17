import timeit

from shared import (
    PUZZLE,
    SAMPLE,
    read_lines,
)

operations = {
    "+": lambda monkeys, a, b: lambda: monkeys[a]() + monkeys[b](),
    "-": lambda monkeys, a, b: lambda: monkeys[a]() - monkeys[b](),
    "/": lambda monkeys, a, b: lambda: monkeys[a]() // monkeys[b](),
    "*": lambda monkeys, a, b: lambda: monkeys[a]() * monkeys[b](),
}


def do_puzzle():
    monkeys = {}
    for l in read_lines(PUZZLE):
        key, instruction = l.split(": ")
        if instruction.strip().isnumeric():
            monkeys[key.strip()] = lambda number=instruction: int(number)
        else:
            key1, operation, key2 = instruction.strip().split(" ")
            monkeys[key] = operations[operation](monkeys, key1, key2)
    monkeys["humn"] = lambda: -7172286853922
    print(monkeys["root"]())


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10**3
    print(f"{exec_time:.03f}ms")

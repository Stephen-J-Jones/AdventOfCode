import re
from dataclasses import dataclass, field
from math import prod
from typing import Callable
from shared import read_lines


def get_data():
    sample_data = read_lines("sample_input.txt")
    puzzle_data = read_lines("puzzle_input.txt")
    data = puzzle_data
    return data


@dataclass
class Monkey:
    name: str = ""
    inspection_count: int = 0
    items: list = field(default_factory=list)
    operation: Callable = None
    test_value: int = 0
    false_monkey: int = 0
    true_monkey: int = 0


def get_all_numbers(string):
    return re.findall(r"\d+", string)


def get_first_number(line):
    return next(int(x) for x in get_all_numbers(line))


def get_monkeys():
    data = get_data()
    monkeys = []
    for line in data:
        if line.startswith("Monkey"):
            monkey = Monkey(name=line[:-1])
            monkeys.append(monkey)
            continue
        if "Starting items" in line:
            monkey.items = [int(x) for x in get_all_numbers(line)]
        if "Operation" in line:
            monkey.operation = eval(f'lambda old: {(line.split("=")[-1].strip())}')
        if "Test" in line:
            monkey.test_value = get_first_number(line)
        if "If true" in line:
            monkey.true_monkey = get_first_number(line)
        if "If false" in line:
            monkey.false_monkey = get_first_number(line)
    return monkeys


def count_inspections():
    ROUNDS = 10000
    WORRY_REDUCTION = 1
    monkeys = get_monkeys()
    lcm = prod([monkey.test_value for monkey in monkeys])
    for i in range(ROUNDS):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspection_count += 1
                new_worry = monkey.operation(monkey.items.pop())
                new_worry = new_worry // WORRY_REDUCTION
                if new_worry % monkey.test_value == 0:
                    destination_monkey = monkeys[monkey.true_monkey]
                else:
                    destination_monkey = monkeys[monkey.false_monkey]
                destination_monkey.items.append(new_worry % lcm)
    counts = [monkey.inspection_count for monkey in monkeys]
    counts.sort()
    return counts[-1] * counts[-2]


if __name__ == "__main__":
    print(count_inspections())

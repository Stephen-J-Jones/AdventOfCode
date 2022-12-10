from shared import read_lines

ROW_WIDTH = 40


def get_data():
    data_small = read_lines("sample_data.txt")
    data_test = read_lines("puzzle_input.txt")
    data = data_test
    return data


def run_cycles():
    data = get_data()
    X = 1
    cycle = 0
    history = {1: X}
    result = 0
    grid = []
    grid.append(["."] * ROW_WIDTH)
    for line in data:
        instruction = line.split(" ")
        if instruction[0] == "noop":
            update_grid(X, cycle, grid)
            cycle = add_to_history(X, cycle, history)
            continue
        if instruction[0] == "addx":
            update_grid(X, cycle, grid)
            cycle = add_to_history(X, cycle, history)
            update_grid(X, cycle, grid)
            cycle = add_to_history(X, cycle, history)
            X += int(instruction[1])
            continue
    for i in range(20, len(history.items()), 40):
        result += i * history[i]
    print(result)
    for g in grid:
        print("".join(g))


def update_grid(X, cycle, grid):
    row, column = get_address(cycle)
    if column == 0:
        grid.append( ["."] * ROW_WIDTH)
    do_draw = column in range(X - 1, X + 2)
    if do_draw:
        grid[row][column] = "#"


def get_address(cycle):
    row = cycle // ROW_WIDTH
    column = cycle % ROW_WIDTH
    return row, column


def add_to_history(X, cycle, history):
    cycle += 1
    history[cycle] = X
    return cycle


if __name__ == "__main__":
    run_cycles()

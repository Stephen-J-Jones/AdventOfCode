from shared import read_lines


def part_1_count_visible_trees():
    column_count, columns, data, row_count = prepare_tree_grid()
    total = 0
    # total = 2 * column_count
    # total += 2 * row_count - 4
    for row_index in range(row_count):
        for col_index in range(column_count):
            current_tree = data[row_index][col_index]
            if (
                    all(t < current_tree for t in data[row_index][:col_index]) or
                    all(t < current_tree for t in data[row_index][col_index + 1:]) or
                    all(t < current_tree for t in columns[col_index][:row_index]) or
                    all(t < current_tree for t in columns[col_index][row_index + 1:])):
                total += 1
            else:
                pass
    return total


def part_2_scenic_score():
    scenic_score = 0
    column_count, columns, data, row_count = prepare_tree_grid()
    for row_index in range(1, row_count):
        for col_index in range(1, column_count):
            current_tree = data[row_index][col_index]
            to_left = data[row_index][col_index - 1::-1]
            to_right = data[row_index][col_index + 1:]
            up = columns[col_index][row_index - 1::-1]
            down = columns[col_index][row_index + 1:]
            left_score = find_scenic_score_in_direction(current_tree, to_left)
            right_score = find_scenic_score_in_direction(current_tree, to_right)
            up_score = find_scenic_score_in_direction(current_tree, up)
            down_score = find_scenic_score_in_direction(current_tree, down)
            scenic_score = max(scenic_score, left_score * right_score * up_score * down_score)
    return scenic_score


def find_scenic_score_in_direction(current_tree, to_left):
    score = 0
    for cell in to_left:
        if cell < current_tree:
            score += 1
        elif cell >= current_tree:
            score += 1
            break
    return score


def prepare_tree_grid():
    # data = ["30373",
    #         "25512",
    #         "65332",
    #         "33549",
    #         "35390", ]
    data = [line for line in read_lines("puzzle_input.txt")]
    column_count = len(data[0])
    row_count = len(data)
    columns = make_columns(column_count, data, row_count)
    return column_count, columns, data, row_count


def make_columns(column_count, data, row_count):
    columns = [""] * column_count
    for column_index in range(column_count):
        for row_index in range(row_count):
            columns[column_index] += data[row_index][column_index]
    return columns


if __name__ == "__main__":
    print(part_1_count_visible_trees())
    print(part_2_scenic_score())

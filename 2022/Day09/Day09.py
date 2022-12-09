from shared import read_lines


def move_head(head, direction):
    x, y = head
    if direction == "R":
        x += 1
    elif direction == "L":
        x -= 1
    elif direction == "U":
        y += 1
    elif direction == "D":
        y -= 1
    return x, y


def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail
    dx = hx - tx
    dy = hy - ty
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tx, ty
    if abs(dx) > 1:
        tx = tx + (abs(dx) // dx)
        if abs(dy) == 1:
            ty = hy
        elif abs(dy) > 1:
            ty = ty + (abs(dy) // dy)
        return tx, ty
    if abs(dy) > 1:
        ty = ty + (abs(dy) // dy)
        if abs(dx) == 1:
            tx = hx
        elif abs(dx) > 1:
            tx = tx + (abs(dx) // dx)
        return tx, ty
    return tail



def follow_rope():
    data = get_data()
    current_h = (0, 0)
    current_t = (0, 0)
    tail_history = set()
    tail_history.add(current_t)
    for move in data:
        direction, count = move.split()
        for step in range(int(count)):
            current_h = move_head(current_h, direction)
            tail_history.add((current_t := move_tail(current_h, current_t)))
    print(len(tail_history))


def follow_knots():
    data = get_data()
    nodes = [(0, 0)] * 10
    current_t = (0, 0)
    tail_history = set()
    tail_history.add(current_t)
    for move in data:
        direction, count = move.split()
        for step in range(int(count)):
            nodes[0] = move_head(nodes[0], direction)
            for node_index in range(1, len(nodes)):
                nodes[node_index] = move_tail(nodes[node_index - 1], nodes[node_index])
            tail_history.add(nodes[-1])
    print(len(tail_history))


def get_data():
    # data = [
    #     "R 4",
    #     "U 4",
    #     "L 3",
    #     "D 1",
    #     "R 4",
    #     "D 1",
    #     "L 5",
    #     "R 2",
    # ]
    # data = [
    #     "R 5",
    #     "U 8",
    #     "L 8",
    #     "D 3",
    #     "R 17",
    #     "D 10",
    #     "L 25",
    #     "U 20"
    # ]
    data = read_lines("puzzle_input.txt")
    return data


if __name__ == "__main__":
    follow_rope()
    follow_knots()

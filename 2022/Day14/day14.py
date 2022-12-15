import os
import sys

from shared import read_lines, PUZZLE, SAMPLE

ROCK = "#"
EMPTY = " "


def to_points(node):
    x, y = node.split(",")
    return int(x), int(y)


def draw_line(grid, first_point, second_point):
    fx, fy = first_point
    grid[fy][fx] = ROCK
    sx, sy = second_point
    grid[sy][sx] = ROCK
    if fx == sx:
        for row in range(fy, sy, (sy - fy) // abs(fy - sy)):
            grid[row][fx] = ROCK
    else:
        for col in range(fx, sx, (sx - fx) // abs(fx - sx)):
            grid[fy][col] = ROCK


def build_rocks():
    data = read_lines(PUZZLE)
    INITIAL_WIDTH = 1000
    grid = [[EMPTY for i in range(1000)] for j in range(200)]
    left = sys.maxsize
    right = 0
    bottom = 0
    for line in data:
        nodes = [n.strip() for n in line.split("->")]
        for n_index in range(1, len(nodes)):
            first_point = to_points(nodes[n_index - 1])
            second_point = to_points(nodes[n_index])
            draw_line(grid, first_point, second_point)
            left = min(left, first_point[0], second_point[0])
            right = max(right, first_point[0], second_point[0])
            bottom = max(bottom, first_point[1], second_point[1])
    grid[bottom + 2] = [ROCK for i in range(1000)]
    grid = grid[:bottom + 3]
    # for r_index in range(len(grid)):
    #     grid[r_index] = grid[r_index][left - 50:right + 50]
    return grid, 0,


START = 500, 0


def flow_sand():
    grid, left = build_rocks()
    bottom = len(grid)
    sand_count = 0
    left_margin = sys.maxsize
    right = 0
    start_x, start_y = START
    start_x -= left
    while True:
        sand_x = start_x
        sand_y = start_y
        if grid[0][start_x] != EMPTY:
            break
        while True:
            if grid[sand_y + 1][sand_x] is EMPTY:
                sand_y += 1
                continue
            if grid[sand_y + 1][sand_x - 1] is EMPTY:
                sand_y += 1
                sand_x -= 1
                continue
            if grid[sand_y + 1][sand_x + 1] is EMPTY:
                sand_y += 1
                sand_x += 1
                continue
            break
        sand_count += 1
        left_margin = min(left_margin, sand_x)
        right = max(right, sand_x)
        grid[sand_y][sand_x] = "."
    for r_index in range(len(grid)):
        grid[r_index] = grid[r_index][left_margin:right + 1]
    return grid, sand_count


if __name__ == "__main__":
    g, count = flow_sand()
    for rx in g:
        print("".join(rx))
    print(count)

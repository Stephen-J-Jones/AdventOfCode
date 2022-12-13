import sys
from collections import defaultdict
from dataclasses import dataclass, field

from shared import read_lines

START = 'S'
END = 'E'


@dataclass
class Cell:
    height: int or str = None
    letter: str = None
    neighbours: list = field(default_factory=list)
    row: int = 0
    column: int = 0
    distance: int = sys.maxsize
    explored: bool = False
    parent: object = None

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column


def get_data(file):
    grid = []
    line_count = 0
    start = None
    end = None
    for line in read_lines(file):
        grid.append([])
        for c_index in range(len(line)):
            cell = Cell(
                height=ord(line[c_index]) if line[c_index] not in [START, END] else line[c_index], row=line_count,
                letter=line[c_index],
                column=c_index)
            if cell.height == START:
                cell.height = ord('a')
                cell.distance = 0
                start = cell
            if cell.height == END:
                cell.height = ord('z')
                end = cell
            grid[line_count].append(cell)
        line_count += 1
    return grid, start, end


def find_children(cell, grid):
    moves = [(cell.row - 1, cell.column),
             (cell.row + 1, cell.column),
             (cell.row, cell.column - 1),
             (cell.row, cell.column + 1), ]
    for move in moves:
        r, c = move
        if r < 0 or c < 0:
            continue
        try:
            neighbour_cell = grid[r][c]
            if neighbour_cell.height - cell.height >= -1:
                cell.neighbours.append(neighbour_cell)
        except IndexError:
            pass


def build_neighbours():
    grid, start, end = get_data("puzzle_input.txt")
    row_count = len(grid)
    column_count = len(grid[0])
    for row_index in range(row_count):
        for column_index in range(column_count):
            find_children(grid[row_index][column_index], grid)
    return grid, start, end


def cell_as_tuple(cell):
    return cell.row, cell.column


def find_shortest_path():
    grid, start, end = build_neighbours()
    queue = [end]
    end.explored = True
    end.distance=0
    while len(queue) > 0:
        current = queue.pop(0)
        if current.letter == 'a':
            break
        for neighbour in [neighbour for neighbour in current.neighbours if not neighbour.explored]:
            neighbour.distance = current.distance + 1
            neighbour.explored = True
            neighbour.parent = current
            queue.append(neighbour)
    return current.distance


if __name__ == "__main__":
    print(find_shortest_path())

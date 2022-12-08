from collections import defaultdict
from dataclasses import dataclass, field
from shared import read_lines


@dataclass
class Node:
    name: str = ""
    size: int = 0
    children: dict = field(default_factory=dict)
    parent: object = None


def add_to_parent(current_dir: Node, file_size: int):
    if current_dir.parent:
        parent = current_dir.parent
        parent.size += file_size
        add_to_parent(parent, file_size)


def accumulate_total(node: Node):
    total = 0
    if node.size <= 100000:
        total += node.size
    for child_node in node.children.values():
        total += accumulate_total(child_node)
    return total


if __name__ == "__main__":
    # data = [
    #     "$ cd /",
    #     "$ ls",
    #     "dir a",
    #     "14848514 b.txt",
    #     "8504156 c.dat",
    #     "dir d",
    #     "$ cd a",
    #     "$ ls",
    #     "dir e",
    #     "29116 f",
    #     "2557 g",
    #     "62596 h.lst",
    #     "$ cd e",
    #     "$ ls",
    #     "584 i",
    #     "$ cd ..",
    #     "$ cd ..",
    #     "$ cd d",
    #     "$ ls",
    #     "4060174 j",
    #     "8033020 d.log",
    #     "5626152 d.ext",
    #     "7214296 k",
    # ]
    data = read_lines('puzzle_input.txt')
    listed_dirs = defaultdict(int)
    root_node = Node(name="/")
    current_dir = root_node
    line_count = 0
    for line in data:
        line_count += 1
        if line.startswith("$"):
            split_line = line.split(" ")
            command = split_line[1]
            if command == "ls":
                continue
            if command == "cd":
                folder = split_line[2]
                if folder == "..":
                    current_dir = current_dir.parent
                elif folder == "/":
                    current_dir = root_node
                else:
                    current_dir = current_dir.children[folder]
            continue
        if line.startswith("dir"):
            _, child_dir = line.split(" ")
            current_dir.children[child_dir] = Node(name=child_dir, parent=current_dir)
            continue
        file_size, _ = line.split(" ")
        file_size = int(file_size)
        current_dir.size += file_size
        add_to_parent(current_dir, file_size)
    total = accumulate_total(root_node)
    print(total)

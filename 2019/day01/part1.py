from shared import SAMPLE, PUZZLE, read_lines

if __name__ == "__main__":
    total = 0
    for line in read_lines(PUZZLE):
        total += (int(line) // 3) - 2
    print(total)

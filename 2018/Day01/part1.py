from shared import SAMPLE, PUZZLE, read_lines

if __name__ == "__main__":
    total = 0
    for i in read_lines(PUZZLE):
        total += int(i.strip())
    print(total)

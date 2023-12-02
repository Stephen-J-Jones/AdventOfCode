from shared import read_lines, SAMPLE, PUZZLE

if __name__ == '__main__':
    elves = []
    i = 0
    elves.append(0)
    for line in read_lines(PUZZLE):
        if line == "":
            i += 1
            elves.append(0)
            continue
        elves[i] += int(line)

    print(f" {max(elves)} calories")

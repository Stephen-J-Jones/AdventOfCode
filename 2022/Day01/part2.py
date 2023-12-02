from shared import read_lines, PUZZLE

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
    total = 0
    elves.sort()
    print(sum(elves[-3:]))
    for i in range(3):
        l = max(elves)
        total += l
        elves.pop(elves.index(l))

    print(f" {total} calories")

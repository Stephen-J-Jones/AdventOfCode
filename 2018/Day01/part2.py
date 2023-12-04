from shared import SAMPLE, PUZZLE, read_lines

if __name__ == "__main__":
    total = 0
    frequencies = set([total])
    # data = [int(x) for x in "+7, +7, -2, -7, -4".split(',')]
    data = [int(x.strip()) for x in read_lines(PUZZLE)]
    i = 0
    length = len(data)
    while True:
        total += data[i % length]
        if total in frequencies:
            break
        frequencies.add(total)
        i += 1
    print(total)

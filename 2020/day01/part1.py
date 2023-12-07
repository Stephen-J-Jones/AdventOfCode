from shared import SAMPLE, PUZZLE, read_lines

TARGET = 2020

if __name__ == "__main__":
    values = sorted([int(line) for line in read_lines(PUZZLE)])
    below_half = [val for val in values if val <= TARGET // 2]
    above_half = [val for val in values if val > TARGET // 2]
    for small in below_half:
        for big in above_half:
            if small + big == 2020:
                print(small * big)
                exit()

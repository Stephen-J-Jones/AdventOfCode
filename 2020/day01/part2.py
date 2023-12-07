from shared import SAMPLE, PUZZLE, read_lines

TARGET = 2020

if __name__ == "__main__":
    values = set([int(line) for line in read_lines(PUZZLE)])
    for one in values:
        for two in values:
            for three in values:
                if one + two + three == 2020:
                    print(one * two * three)
                    exit()

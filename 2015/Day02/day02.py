from shared import read_lines


def total_paper():
    data = read_lines("puzzle_input.txt")
    total = 0
    ribbon=0
    for line in data:
        l, w, h = [int(x) for x in line.split("x")]
        s1 = l * w
        c1 = l+w
        s2 = l * h
        c2 = l+h
        s3 = w * h
        c3 = w+h
        total += 2 * (s1 + s2 + s3)
        total += min([s1, s2, s3])
        ribbon += 2 * min(c1,c2,c3)
        ribbon += l*w*h
    return total, ribbon


if __name__ == "__main__":
    print(total_paper())

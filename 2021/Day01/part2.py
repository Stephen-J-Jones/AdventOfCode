from shared import read_lines

if __name__ == '__main__':
    # data = [
    #     "199",
    #     "200",
    #     "208",
    #     "210",
    #     "200",
    #     "207",
    #     "240",
    #     "269",
    #     "260",
    #     "263",
    # ]
    # data = [int(x) for x in data]
    data = [int(l) for l in read_lines('data.txt')]
    counter = 0
    for i in range(len(data) - 3):
        if sum(data[i:i + 3]) < sum(data[i + 1:i + 1 + 3]):
            counter += 1
    print(counter)

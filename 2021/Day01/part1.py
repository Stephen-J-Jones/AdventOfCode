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
    data = [l for l in read_lines('data.txt')]
    counter = 0
    for i in range(1, len(data)):
        if int(data[i]) > int(data[i - 1]):
            counter += 1
    print(counter)

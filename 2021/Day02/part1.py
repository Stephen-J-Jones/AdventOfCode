from shared import read_lines

if __name__ == '__main__':
    # data = [
    #     "forward 5",
    #     "down 5",
    #     "forward 8",
    #     "up 3",
    #     "down 8",
    #     "forward 2"
    # ]
    data = read_lines('data.txt')
    x = 0
    depth = 0
    aim = 0
    for move in data:
        command, distance = move.split(" ")
        distance = int(distance)
        if command == "forward":
            x += distance
            depth += aim * distance
        if command == "down":
            aim += distance
#            depth += distance
        if command == "up":
            aim -= distance
 #           depth -= distance
    print(x * depth)

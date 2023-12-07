from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string

if __name__ == "__main__":
    races = []
    for line in read_lines(PUZZLE):
        races.append(find_all_numbers_in_string(line))
    times = races[0]
    distances = races[1]
    i = 0
    winning_product = 1
    for time in times:
        distance = distances[i]
        i += 1
        ways_to_win = 0
        for s in range(time):
            new_d = s * (time - s)
            if new_d > distance:
                ways_to_win += 1
        winning_product *= ways_to_win
    print(winning_product)

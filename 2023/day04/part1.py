from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string


def parse_line(line):
    no_card = [part.strip() for part in line.split(":")]
    numbers = [part.strip() for part in no_card[-1].split("|")]
    winning = find_all_numbers_in_string(numbers[0])
    play = find_all_numbers_in_string(numbers[1])
    return winning, play


if __name__ == "__main__":
    total_points = 0
    for line in read_lines(PUZZLE):
        game_points = 0
        winning, play = parse_line(line)
        for n in play:
            if n in winning:
                if game_points == 0:
                    game_points = 1
                else:
                    game_points = game_points * 2
        total_points += game_points
    print(total_points)

from shared import SAMPLE, PUZZLE, read_lines
from day2 import parse_game

red_available = 12
green_available = 13
blue_available = 14

available = {'red': red_available, 'green': green_available, 'blue': blue_available}


def are_all_pulls_possible(pulls):
    for pull in pulls.split(';'):
        for ball_count in pull.split(','):
            count, color = tuple(ball_count.split())
            if int(count) > available[color]:
                return False
    return True


def is_game_possible(line):
    game_number, pulls = parse_game(line)
    return game_number if are_all_pulls_possible(pulls) else 0


if __name__ == '__main__':
    count = 0
    for line in read_lines(PUZZLE):
        count += is_game_possible(line)
    print(count)

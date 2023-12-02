from shared import SAMPLE, PUZZLE, read_lines
from day2 import parse_game


def power_ball(pulls):
    ball_accumulator = {}
    for pull in pulls.split(';'):
        for ball_count in pull.split(','):
            count, color = tuple(ball_count.split())
            ball_accumulator[color] = max(ball_accumulator.get(color, 0), int(count))
    x = 1
    for count in ball_accumulator.values():
        x = x * count
    return x


if __name__ == '__main__':
    count = 0
    for line in read_lines(PUZZLE):
        count += power_ball(parse_game(line)[-1])
    print(count)

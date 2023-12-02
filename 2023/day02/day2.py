from shared import find_all_numbers_in_string


def parse_game(line):
    game_split = line.split(':')
    return find_all_numbers_in_string(game_split[0])[0], game_split[-1]

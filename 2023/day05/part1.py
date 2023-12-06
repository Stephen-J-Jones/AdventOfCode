from collections import defaultdict

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string

SEEDS = "seeds"
SEED_TO_SOIL = "seed-to-soil"
SOIL_TO_FERTILIZER = "soil-to-fertilizer"
FERTILIZER_TO_WATER = "fertilizer-to-water"
WATER_TO_LIGHT = "water-to-light"
LIGHT_TO_TEMPERATURE = "light-to-temperature"
TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity"
HUMIDITY_TO_LOCATION = "humidity-to-location"
SOURCE = "source"
DESTINATION = "destination"
RANGE = "range"
RANGE_KEYS = [DESTINATION, SOURCE, RANGE]


def build_mappings():
    mapping = defaultdict(list)
    key = ''
    for line in read_lines(PUZZLE):
        if line == "":
            continue
        if line.startswith(SEEDS):
            mapping[SEEDS] = find_all_numbers_in_string(line)
            continue
        if line.startswith(SEED_TO_SOIL):
            key = SEED_TO_SOIL
            continue
        if line.startswith(SOIL_TO_FERTILIZER):
            key = SOIL_TO_FERTILIZER
            continue
        if line.startswith(FERTILIZER_TO_WATER):
            key = FERTILIZER_TO_WATER
            continue
        if line.startswith(WATER_TO_LIGHT):
            key = WATER_TO_LIGHT
            continue
        if line.startswith(LIGHT_TO_TEMPERATURE):
            key = LIGHT_TO_TEMPERATURE
            continue
        if line.startswith(TEMPERATURE_TO_HUMIDITY):
            key = TEMPERATURE_TO_HUMIDITY
            continue
        if line.startswith(HUMIDITY_TO_LOCATION):
            key = HUMIDITY_TO_LOCATION
            continue
        range_numbers = find_all_numbers_in_string(line)
        mapping[key].append(dict(zip(RANGE_KEYS, range_numbers)))
    return mapping


def source_to_destination(source, ranges):
    for range_representation in ranges:
        if source in range(range_representation[SOURCE], range_representation[SOURCE] + range_representation[RANGE]):
            return range_representation[DESTINATION] + source - range_representation[SOURCE]
    return source


if __name__ == "__main__":
    mapping = build_mappings()
    locations = set()
    for seed in mapping[SEEDS]:
        soil = source_to_destination(seed, mapping[SEED_TO_SOIL])
        fertilizer = source_to_destination(soil, mapping[SOIL_TO_FERTILIZER])
        water = source_to_destination(fertilizer, mapping[FERTILIZER_TO_WATER])
        light = source_to_destination(water, mapping[WATER_TO_LIGHT])
        temperature = source_to_destination(light, mapping[LIGHT_TO_TEMPERATURE])
        humidity = source_to_destination(temperature, mapping[TEMPERATURE_TO_HUMIDITY])
        locations.add(source_to_destination(humidity, mapping[HUMIDITY_TO_LOCATION]))
    print(min(locations))

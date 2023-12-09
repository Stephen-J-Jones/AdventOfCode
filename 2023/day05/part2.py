import timeit
from collections import defaultdict

from shared import SAMPLE, PUZZLE, read_lines, find_all_numbers_in_string
from time import process_time

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
            seeds = find_all_numbers_in_string(line)
            seed_pairs = []
            for i in range(0, len(seeds), 2):
                r = range(seeds[i], seeds[i] + seeds[i + 1] - 1)
                seed_pairs.append((r.start, r.stop))
            mapping[SEEDS] = seed_pairs
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


def source_to_destination(input_ranges, ranges):
    destination_ranges = []
    new_ranges = input_ranges
    temp_ranges = []
    for range_representation in ranges:
        source_range = range(range_representation[SOURCE],
                             range_representation[SOURCE] + range_representation[RANGE] - 1)
        destination_offset = range_representation[DESTINATION] - range_representation[SOURCE]
        for split in new_ranges:
            # all_left
            if split[1] < source_range.start:
                temp_ranges.append(split)
                continue
            # part_left
            if split[0] < source_range.start and split[1] <= source_range.stop:
                temp_ranges.append([split[0], source_range.start - 1])
                destination_ranges.append([source_range.start + destination_offset,
                                           source_range.start + destination_offset + (split[1] - source_range.start)])
                continue
            # all_in
            if split[0] in source_range and split[1] <= source_range.stop:
                destination_ranges.append([split[0] + destination_offset, split[1] + destination_offset])
                continue
            # part_right
            if source_range.start <= split[0] and split[0] <= source_range.stop and split[1] > source_range.stop:
                destination_ranges.append([split[0] + destination_offset, source_range.stop + destination_offset])
                temp_ranges.append([source_range.stop + 1, split[1]])
                continue
            # all right
            if split[0] > source_range.stop:
                temp_ranges.append(split)
                continue
            # overlap
            if split[0] < source_range.start and split[1] > source_range.stop:
                temp_ranges.append([split[0], source_range.start - 1])
                temp_ranges.append([source_range.stop + 1, split[1]])
                destination_ranges.append([source_range.start + destination_offset,
                                           source_range.stop + destination_offset])
                continue
        new_ranges = temp_ranges
        temp_ranges = []
    return destination_ranges + new_ranges


def do_puzzle():
    mapping = build_mappings()
    locations = []
    for seed in mapping[SEEDS]:
        soil = source_to_destination([seed], mapping[SEED_TO_SOIL])
        fertilizer = source_to_destination(soil, mapping[SOIL_TO_FERTILIZER])
        water = source_to_destination(fertilizer, mapping[FERTILIZER_TO_WATER])
        light = source_to_destination(water, mapping[WATER_TO_LIGHT])
        temperature = source_to_destination(light, mapping[LIGHT_TO_TEMPERATURE])
        humidity = source_to_destination(temperature, mapping[TEMPERATURE_TO_HUMIDITY])
        location = source_to_destination(humidity, mapping[HUMIDITY_TO_LOCATION])
        locations.extend(location)
    print(min(locations)[0])


if __name__ == "__main__":
    exec_time = timeit.timeit(do_puzzle, number=1) * 10 ** 3
    print(f"{exec_time:.03f}ms")

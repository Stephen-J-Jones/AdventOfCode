import time

from shared import SAMPLE, read_lines, find_all_numbers_in_string, PUZZLE


def find_taxi_distance(s, b):
    sx, sy = s
    bx, by = b
    dx = abs(sx - bx)
    dy = abs(sy - by)
    return dx + dy


class Sensor:
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.bx = bx
        self.by = by
        self.taxi_distance = find_taxi_distance((self.x, self.y), (self.bx, self.by))
        self.top = self.y - self.taxi_distance
        self.bottom = self.y + self.taxi_distance

    def covered_range_for_y(self, y):
        width = (self.taxi_distance - abs(y - self.y))
        covered_range = self.x - width, self.x + width
        return covered_range


def build_sensor_array():
    data = read_lines(PUZZLE)
    sensors = []
    beacons = set()
    for line in data:
        x, y, bx, by = find_all_numbers_in_string(line)
        sensors.append(Sensor(x, y, bx, by))
        beacons.add((bx, by))
    return sensors, beacons


def find_where_beacon_cannot_be(y):
    sensors, beacons = build_sensor_array()
    covered = set()
    for sensor in [sensor for sensor in sensors if sensor.top <= y <= sensor.bottom]:
        l, r = sensor.covered_range_for_y(y)
        covered |= set(range(l, r + 1))
    count = len(covered)
    for beacon in [beacon for beacon in beacons if beacon[1] == y and beacon[0] in covered]:
        count -= 1
    return count


def find_beacon(lower, upper):
    sensors, _ = build_sensor_array()
    for y in range(lower, upper + 1):
        covered_ranges = []
        for sensor in [sensor for sensor in sensors if sensor.top <= y <= sensor.bottom]:
            covered_ranges.append(sensor.covered_range_for_y(y))
        covered_ranges.sort()
        pointer = lower
        for covered_range in covered_ranges:
            if covered_range[0] <= pointer <= covered_range[1]:
                pointer = covered_range[1] + 1
            if pointer > upper:
                break
        if pointer <= upper:
            return y, pointer


X_MULTIPLIER = 4000000


def calculate_frequency(lower, upper):
    y, x = find_beacon(lower, upper)
    return x * X_MULTIPLIER + y


LOWER = 0
UPPER = 4000000
if __name__ == "__main__":
    tic = time.perf_counter()
    print(find_where_beacon_cannot_be(2000000))
    print(time.perf_counter() - tic)

    tic = time.perf_counter()
    print(calculate_frequency(LOWER, UPPER))
    print(time.perf_counter() - tic)

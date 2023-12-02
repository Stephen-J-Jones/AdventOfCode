from collections import defaultdict

from shared import SAMPLE, read_lines, find_all_numbers_in_string, PUZZLE


class Room:
    def __init__(self, name):
        self.name = name
        self.rate = 0
        self.paths = []
        self.back = None


def build_graph() -> dict[str, Room]:
    rooms = {}
    for line in read_lines(SAMPLE):
        bits = line.split(" ")
        name = bits[1]
        rate = find_all_numbers_in_string(bits[4])[0]
        paths_names = bits[9:]
        room = rooms.get(name, Room(name))
        room.rate = rate
        rooms[name] = room
        for p in paths_names:
            p = p.replace(",", "")
            sub_room = rooms.get(p, Room(p))
            rooms[p] = sub_room
            room.paths.append(sub_room)
    return rooms


def visit():
    room_graph, start = build_graph()
    starting_room = room_graph[start]
    filtered_rooms = [room for room in room_graph.values() if room.rate > 0]
    ordered_by_rate = sorted(filtered_rooms, key=lambda x: x.rate)
    remaining_time = 30
    opened = []
    queue = [starting_room]
    while remaining_time > 0 and len(ordered_by_rate) > 0:
        destination = ordered_by_rate.pop()
        explored = set()
        current_room = None
        while destination != current_room:
            current_room = queue.pop(0)
            explored.add(current_room)
            for p in [p for p in current_room.paths if p is not current_room.back and p not in explored]:
                p.back = current_room
                queue.append(p)
        back = destination
        while back != starting_room:
            remaining_time -= 1
            back = back.back
        remaining_time -= 1
        opened.append((remaining_time, destination.rate))
        starting_room = destination
        queue = [starting_room]
        for room in explored:
            room.back = None
    pressure = 0
    for t, rate in opened:
        pressure += t * rate
    return pressure


if __name__ == "__main__":
    print(visit())

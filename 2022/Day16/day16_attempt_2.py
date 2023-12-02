from shared import SAMPLE, read_lines, find_all_numbers_in_string, PUZZLE

from day16 import build_graph, Room


class Node:
    def __init__(self, ):
        self.parent = None
        self.child = None


def find_shortest_path(start: Room, destination: Room):
    current_room = start
    queue = [start]
    explored = set()
    while destination != current_room:
        current_room = queue.pop(0)
        explored.add(current_room)
        for p in [p for p in current_room.paths if p is not current_room.back and p not in explored]:
            p.back = current_room
            queue.append(p)
    path = [destination]
    back = destination.back
    while back != start:
        back = back.back
        path.append(back)
    for e in explored:
        e.back = None
    path.reverse()
    return path


def visit():
    room_graph = build_graph()
    starting_room = room_graph["AA"]
    filtered_rooms = [room for room in room_graph.values() if room.rate > 0]
    remaining_time = 30
    opened = []
    while remaining_time > 0 and len(filtered_rooms) > 0:
        max_relief = 0
        actual_travel = 0
        selected_destination = None
        for destination in filtered_rooms:
            travel_time = len(find_shortest_path(starting_room, destination))
            possible_relief = (remaining_time - travel_time) * destination.rate
            if possible_relief > max_relief:
                selected_destination = destination
                max_relief = possible_relief
                actual_travel = travel_time
        remaining_time -= actual_travel
        remaining_time -= 1
        opened.append((selected_destination.name, remaining_time, selected_destination.rate))
        starting_room = selected_destination
        filtered_rooms.remove(selected_destination)
    return calc_total_pressure(opened)


def calc_total_pressure(opened):
    pressure = 0
    for t, rate in opened:
        pressure += t * rate
    return pressure


if __name__ == "__main__":
    print(visit())

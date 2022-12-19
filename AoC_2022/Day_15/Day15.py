import re
import time

def nb_beacon_not_here_in_row(line_target, part):
    global x_max
    pos_beacon_not_here = set()
    for idx, sensor in enumerate(sensors_mapping):
        vert_distance = abs(line_target - sensor[1]) 
        if vert_distance <= distances[idx]:
            Lbound = sensor[0] + (vert_distance - distances[idx])
            Ubound = sensor[0] + distances[idx] - vert_distance + 1
            covered_position = range(Lbound, Ubound)
            if part == 1:
                pos_beacon_not_here = pos_beacon_not_here.union(set(covered_position))
            else:
                Lbound = 0 if Lbound < 0 else Lbound
                Ubound = x_max + 1 if Ubound > x_max + 1 else Ubound
                covered_position = range(Lbound, Ubound)
                pos_beacon_not_here = pos_beacon_not_here.union(set(covered_position))
    return pos_beacon_not_here


start = time.perf_counter()
with open(r'AoC_2022\Day_15\Day15.txt', "r") as f:
    inputs = f.read().splitlines()
    pattern = re.compile(r"(-?\d+)")
    sensors_mapping = [tuple([int(match.group(1)) for match in pattern.finditer(line)][:2]) for line in inputs]
    beacon_mapping = [tuple([int(match.group(1)) for match in pattern.finditer(line)][2:]) for line in inputs]
    distances = [abs(sensor[0] - beacon_mapping[idx][0]) + abs(sensor[1] - beacon_mapping[idx][1]) for idx, sensor in enumerate(sensors_mapping)]
    target_line = 10
    
    #part 1
    pos_beacon_not_here = nb_beacon_not_here_in_row(target_line, 1)
    for beacon in beacon_mapping:
        if beacon[1] == target_line:
            pos_beacon_not_here.remove(beacon[0])
            break #assumptions of only 1 Beacon on the target line
    print(len(pos_beacon_not_here))
    time_part_1 = time.perf_counter()
    print((time_part_1 - start) * 1000)

    #part 2
    x_max = 4_000_000
    target_line = 104 #325
    while True:
        pos_beacon_not_here = nb_beacon_not_here_in_row(target_line, 2)
        print([target_line, len(pos_beacon_not_here)])
        if len(pos_beacon_not_here) < x_max + 1: #there is a available space
            all_position = set(range(0, x_max + 1))
            all_position = all_position.difference(pos_beacon_not_here)
            print(all_position.pop() * 4_000_000 + target_line) 
            break
        target_line += 1



        



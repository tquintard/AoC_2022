import re
import time

def nb_beacon_not_here_in_row(line_target): #return all positions (x) where a beacon can't be positionned 
    pos_beacon_not_here = set()
    for idx, sensor in enumerate(sensors_mapping):
        vert_distance = abs(line_target - sensor[1]) #vertical distance between a sensor and the target line
        if vert_distance <= distances[idx]:
            Lbound = sensor[0] + (vert_distance - distances[idx])
            Ubound = sensor[0] + distances[idx] - vert_distance + 1
            covered_position = range(Lbound, Ubound) #create a list of numbers from Lbound to Ubound
            pos_beacon_not_here = pos_beacon_not_here.union(set(covered_position)) #update the set with new positions
    return pos_beacon_not_here

def row_not_full(line_target):
    coverage = [] #list of lbound and ubound
    for idx, sensor in enumerate(sensors_mapping):
        vert_distance = abs(line_target - sensor[1]) #vertical distance between a sensor and the target line
        if vert_distance <= distances[idx]:
            Lbound = sensor[0] + (vert_distance - distances[idx])
            Ubound = sensor[0] + distances[idx] - vert_distance
            coverage.append([Lbound, Ubound])
            coverage = sorted(coverage)
            idx = 0
            for boundary in coverage[:0:-1]:
                #example: coverage =[[1, 14], [2, 22]] at end of for loop coverage = [[1, 22]]
                #example: coverage =[[1, 14], [2, 3]] at end of for loop coverage = [[1, 14]]
                #example: coverage =[[1, 14], [15, 22]] at end of for loop coverage = [[1, 14], [15, 22]]
                if coverage[-(idx + 2)][0] <= boundary[0] <= coverage[-(idx + 2)][1]:
                    if boundary[1] > coverage[-(idx + 2)][1]:
                        coverage[-(idx + 2)][1] = boundary[1]
                    coverage.pop(-(idx + 1))
                    idx -=1      
                if coverage[-(idx + 2)][0] <= 0 and coverage[-(idx + 2)][1] >= x_max:
                    #if the left neighbours of current boundary is out of range [0, x_max] then the row is full -> return False
                    return False
                idx +=1
    return True

start = time.perf_counter()
with open(r'Day15.txt', "r") as f:
    inputs = f.read().splitlines()
    pattern = re.compile(r"(-?\d+)")
    sensors_mapping = [tuple([int(match.group(1)) for match in pattern.finditer(line)][:2]) for line in inputs]
    beacon_mapping = [tuple([int(match.group(1)) for match in pattern.finditer(line)][2:]) for line in inputs]
    distances = [abs(sensor[0] - beacon_mapping[idx][0]) + abs(sensor[1] - beacon_mapping[idx][1]) for idx, sensor in enumerate(sensors_mapping)]
    target_line = 2_000_000
    
    #part 1
    pos_beacon_not_here = nb_beacon_not_here_in_row(target_line)
    for beacon in beacon_mapping:
        if beacon[1] == target_line:
            pos_beacon_not_here.remove(beacon[0])
            break #assumptions of only 1 Beacon on the target line
    print(len(pos_beacon_not_here))
    time_part_1 = time.perf_counter()
    print((time_part_1 - start) * 1000)

    #part 2
    x_max = 4_000_000
    target_line = 325 #325
    while True:
        if row_not_full(target_line): #there is a available space
            pos_beacon_not_here = nb_beacon_not_here_in_row(target_line)
            all_position = set(range(0, x_max + 1))
            all_position = all_position.difference(pos_beacon_not_here)
            print(all_position.pop() * 4_000_000 + target_line) 
            break
        target_line += 1
    print((time.perf_counter() - time_part_1) * 1000)

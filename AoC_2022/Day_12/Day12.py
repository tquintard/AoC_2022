import string
import copy
import time
ALPHA = string.ascii_lowercase

def find_start_end(heightmap, letter):
    for row, line in enumerate(heightmap):
        for col in range(len(line)):
            if line[col][0] == letter:
                if letter =='S':
                    line[col][0] ='a'
                else:
                    line[col][0] ='z'
                return row, col


def navigate(pos, distance, heightmap):
    global map_dimensions
    actual_letter = heightmap[pos[0]][pos[1]][0]
    if heightmap[pos[0]][pos[1]][1] > distance:
        #already visited but from a longer path
        heightmap[pos[0]][pos[1]][1] = distance
        #looking on the right
        if pos[1] < map_dimensions[1] - 1:
            next_letter = heightmap[pos[0]][pos[1] + 1][0]
            if ord(next_letter) - ord(actual_letter) <= 1:
                distance += 1
                navigate([pos[0], pos[1] + 1], distance, heightmap)
                distance -= 1
        #looking down
        if pos[0] < map_dimensions[0] - 1:
            next_letter = heightmap[pos[0] + 1][pos[1]][0]
            if ord(next_letter) - ord(actual_letter) <= 1:
                distance += 1
                navigate([pos[0] + 1, pos[1]], distance, heightmap)
                distance -= 1
        #looking left
        if pos[1] > 0:
            next_letter = heightmap[pos[0]][pos[1] - 1][0]
            if ord(next_letter) - ord(actual_letter) <= 1:
                distance += 1
                navigate([pos[0], pos[1] - 1], distance, heightmap)
                distance -= 1
        #looking up
        if pos[0] > 0:
            next_letter = heightmap[pos[0] - 1][pos[1]][0]
            if ord(next_letter) - ord(actual_letter) <= 1:
                distance += 1
                navigate([pos[0] - 1, pos[1]], distance, heightmap)
                distance -= 1

start = time.perf_counter()
with open(r'AoC_2022\Day_12\Day12.txt', "r") as f:
    inputs = f.read().splitlines()
    map_dimensions= (len(inputs), len(inputs[0]))
    max_distance = map_dimensions[0] * map_dimensions[1] - 1
    #part 1
    heightmap = [[[char, max_distance] for char in line ]for line in inputs]
    start_pos = find_start_end(heightmap,'S')
    end_pos = find_start_end(heightmap, 'E')
    distance = 0
    navigate(start_pos, distance, heightmap)
    print(heightmap[end_pos[0]][end_pos[1]][1])
    time_part_1 = time.perf_counter() - start
    print(f'Time Part 1: {time_part_1*1000}')
    #part 2
    heightmap = [[[char, max_distance] for char in line ]for line in inputs]
    start_pos = find_start_end(heightmap,'S')
    end_pos = find_start_end(heightmap, 'E')
    all_distance =[]
    for row, line in enumerate(heightmap):
        for col in range(len(line)):
            if line[col][0] == 'a':
                distance = 0
                temp_map = copy.deepcopy(heightmap)
                try:
                    navigate([row, col], distance, temp_map)
                except:
                    pass
                all_distance.append(temp_map[end_pos[0]][end_pos[1]][1])
    print(min(all_distance))
    time_part_2 = time.perf_counter() - start - time_part_1
    print(f'Time Part 1: {time_part_2*1000}')
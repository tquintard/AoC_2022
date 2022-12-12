import time

def find_start_end(heightmap, letter):
    for row, line in enumerate(heightmap):
        for col in range(len(line)):
            if line[col][0] == letter:
                if letter =='S':
                    line[col][0] ='a'
                else:
                    line[col][0] ='z'
                return row, col

def go_next(actual_letter, next_pos, direction, distance):
    next_letter = heightmap[next_pos[0]][next_pos[1]][0]
    if (ord(next_letter) - ord(actual_letter)) * direction <= 1:
        navigate(next_pos, distance + 1, heightmap, direction)

def navigate(pos, distance, heightmap, direction):
    global map_dimensions
    global min_distance
    try:
        actual_letter = heightmap[pos[0]][pos[1]][0]
        if heightmap[pos[0]][pos[1]][1] > distance: #already visited but from a longer path
            heightmap[pos[0]][pos[1]][1] = distance
            if pos[1] < map_dimensions[1] - 1: #looking on the right
                go_next(actual_letter, [pos[0], pos[1] + 1], direction, distance)
            if pos[0] < map_dimensions[0] - 1: #looking down
                go_next(actual_letter, [pos[0] + 1, pos[1]], direction, distance)
            if pos[1] > 0: #looking left
                go_next(actual_letter, [pos[0], pos[1] - 1], direction, distance)
            if pos[0] > 0: #looking up
                go_next(actual_letter, [pos[0] - 1, pos[1]], direction, distance)
            #update min_distance if required
            if actual_letter == 'a' and heightmap[pos[0]][pos[1]][1] < min_distance:
                min_distance = heightmap[pos[0]][pos[1]][1]
    except RecursionError:
        pass

start = time.perf_counter()
with open(r'AoC_2022\Day_12\Day12.txt', "r") as f:
    inputs = f.read().splitlines()
    map_dimensions= (len(inputs), len(inputs[0]))
    max_distance = map_dimensions[0] * map_dimensions[1] - 1
    heightmap = [[[char, max_distance] for char in line ]for line in inputs]
    start_pos = find_start_end(heightmap,'S')
    end_pos = find_start_end(heightmap, 'E')
    min_distance = max_distance
    navigate(end_pos, 0, heightmap, -1)
    print([heightmap[start_pos[0]][start_pos[1]][1], min_distance])
    print(time.perf_counter() - start)
    

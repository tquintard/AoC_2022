import time
def pour_sand(grid, bottom_grid, part):
    bottom_grid -= 2 * (2 - part)
    counter = 0
    while True:
        sand = [500, 0]
        sand_is_resting = False
        while sand[1] < bottom_grid:
            if grid[sand[1] + 1][sand[0]] != '.':
                if grid[sand[1] + 1][sand[0] - 1] != '.':
                    if grid[sand[1] + 1][sand[0] + 1] != '.':
                        grid[sand[1]][sand[0]] = 'o'
                        sand_is_resting = True
                        counter += 1
                        if sand == [500, 0]:
                            return counter
                        break
                    else:
                        sand[0] += 1
                        sand[1] += 1
                else:
                    sand[0] -= 1
                    sand[1] += 1
            else:
                sand[1] += 1
        if not(sand_is_resting):
            return counter
start = time.perf_counter()
with open(r'AoC_2022\Day_14\Day14.txt', "r") as f:
    rocks_position = [[[int(coord) for coord in xycoord.split(',')] for xycoord in line.split(' -> ')]for line in f.read().splitlines() ]
    #find the bottom, top left and top right of the grid
    bottom_grid = max([rock[1] for rock_position in rocks_position for rock in rock_position]) + 2
    #generate an empty grid
    grid = [['.' for i in range(0, 1001)] for j in range(bottom_grid)]
    grid.append(['#' for i in range(0, 1001)])
    #place the rock
    for rock_position in rocks_position:
        grid[rock_position[0][1]][rock_position[0][0]] = '#'
        for ind, rock in enumerate(rock_position[1:]):
            if rock[0] == rock_position[ind][0]:
                direction = 1 if rock[1] < rock_position[ind][1] else -1
                for i in range(rock[1], rock_position[ind][1], direction):
                    grid[i][rock[0]] = '#'
            elif rock[1] == rock_position[ind][1]:
                direction = 1 if rock[0] < rock_position[ind][0] else -1
                for i in range(rock[0], rock_position[ind][0], direction):
                    grid[rock[1]][i] = '#'
    # part 1
    counter = pour_sand(grid, bottom_grid, 1)
    #print(sep='\n', *[''.join([coord for coord in line[475:525]]) for line in grid])
    print(counter)
    #part 2
    counter += pour_sand(grid, bottom_grid, 2)
    #print(sep='\n', *[''.join([coord for coord in line[475:525]]) for line in grid])
    print(counter)
    print((time.perf_counter() - start)*1000)


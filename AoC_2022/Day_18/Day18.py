import time
import sys
start = time.perf_counter()
sys.setrecursionlimit(3000)

def flood_fill(x,y,z,start_char,char_to_update):
    #if the cube is not the same character as the starting point
    if grid[x][y][z] != start_char:
        return
    #if the cube is not the new character
    elif grid[x][y][z] == char_to_update:
        return
    else:
        #update the character of the current cube to the replacement character
        grid[x][y][z] = char_to_update
        neighbors = [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]
        for n in neighbors:
            if 0 <= n[0] <= width-1 and 0 <= n[1] <= length-1 and 0 <= n[2] <= depth-1:
                flood_fill(n[0],n[1],n[2],start_char,char_to_update)

def count_free_faces(cubes):
    cubes_face = [6 for cube in cubes]
    for i, cube in enumerate(cubes):
        for j, next_cube in enumerate(cubes[i + 1:]):
            xy_plane_n_adjacent_test = cube[0] == next_cube[0] and cube[1] == next_cube[1] and abs(cube[2] - next_cube[2]) == 1
            yz_plane_n_adjacent_test = cube[2] == next_cube[2] and cube[1] == next_cube[1] and abs(cube[0] - next_cube[0]) == 1
            xz_plane_n_adjacent_test = cube[0] == next_cube[0] and cube[2] == next_cube[2] and abs(cube[1] - next_cube[1]) == 1
            if xy_plane_n_adjacent_test or yz_plane_n_adjacent_test or xz_plane_n_adjacent_test:
                cubes_face[i] -= 1
                cubes_face[i + 1 + j] -= 1
            # if cubes_face[i] == 0:
            #     break

    return sum(cubes_face)

with open('Day18.txt', "r") as f:
    lavas = [list(map(int, eval(f'[{input}]'))) for input in f.read().splitlines()]
    
    #part 1
    total_lava_free_faces = count_free_faces(lavas)
    print(total_lava_free_faces)
    time_p1 = time.perf_counter()
    print((time_p1- start)*1000)

    #part 2
    #build a 3D grid
    width = 0 #x dimension
    length = 0 #y dimension
    depth = 0 #z dimension
    for lava in lavas:
        width = lava[0] if width < lava[0] else width
        length = lava[1] if length < lava[1] else length
        depth = lava[2] if depth < lava[2] else depth
    
    grid = [[['.' for z in range(depth)]for y in range(length)] for x in range(width)]
    for lava in lavas:
        grid[lava[0] - 1][lava[1] - 1][lava[2] - 1] = '#'

    #flood fill the grid from the outside    
    flood_fill(0,0,0,'.','~')
    #print(sep='\n         \n', *['\n'.join([''.join([coord for coord in grid[x][y]]) for y,y_plan in enumerate(grid[x])]) for x,x_plan in enumerate(grid)])

    #find coordinate of trap air cube
    air_cube = []
    for x, x_plan in enumerate(grid):
        for y, y_plan in enumerate(x_plan):
            for z, z_plan in enumerate(y_plan):
                if grid[x][y][z] == '.':
                    if 0 < x < width-1 and 0 < y < length-1 and 0 < z < depth-1:
                        air_cube.append([x,y,z])
    total_air_trap_face = count_free_faces(air_cube)
    print(total_lava_free_faces - total_air_trap_face)
    time_p2 = time.perf_counter()
    print((time_p2- time_p1)*1000)
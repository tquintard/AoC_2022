def move_head(head, instruction):
    if instruction == 'R':
        head[0] += 1
    elif instruction == 'L':
        head[0] -= 1
    elif instruction == 'U':
        head[1] += 1
    elif instruction == 'D':
        head[1] -= 1

def move_knot(knot, direction, distance):
    if direction == 'H': #horizontal
        knot[0] += distance_previous_knot[0] // 2
        knot[1] += distance_previous_knot[1]
    elif direction == 'V':
        knot[0] += distance_previous_knot[0]
        knot[1] += distance_previous_knot[1] // 2
    else:
        knot[0] += distance_previous_knot[0] // 2
        knot[1] += distance_previous_knot[1] // 2

with open(r'AoC_2022\Day_9\Day9.txt', "r") as f:
    inputs = f.read().splitlines()
    head_movement = [line.split() for line in inputs]
    for part in range(2):
        rope_len = 2 + 8*part
        rope_pos = [[0,0] for i in range(rope_len)]
        pos_visited =set()
        pos_visited.add(tuple(rope_pos[-1]))
        for movement in head_movement:
            head = [0]
            for i in range(int(movement[1])):
                move_head(rope_pos[0], movement[0])
                for knot in range(1,rope_len):
                    distance_previous_knot = [rope_pos[knot - 1][0] - rope_pos[knot][0], rope_pos[knot - 1][1] - rope_pos[knot][1]]
                    if abs(distance_previous_knot[0]) > 1 and abs(distance_previous_knot[1]) > 1:
                        move_knot(rope_pos[knot], '', distance_previous_knot)
                    elif abs(distance_previous_knot[0]) > 1:
                        move_knot(rope_pos[knot], 'H', distance_previous_knot)
                    elif abs(distance_previous_knot[1]) > 1:
                        move_knot(rope_pos[knot], 'V', distance_previous_knot)
                pos_visited.add(tuple(rope_pos[-1]))
        print(len(pos_visited))

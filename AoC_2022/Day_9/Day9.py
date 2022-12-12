import copy

def move_head(knot, instruction):
    if instruction == 'R':
        knot[0] += 1
    elif instruction == 'L':
        knot[0] -= 1
    elif instruction == 'U':
        knot[1] += 1
    elif instruction == 'D':
        knot[1] -= 1
    
with open(r'AoC_2022\Day_9\example.txt', "r") as f:
    inputs = f.read().splitlines()
    head_movement = [line.split() for line in inputs]
    H_pos=[0,0] #position: [horizontal , vertical] with positive deplacement on the right and top
    T_pos=[0,0]
    pos_visited =set()
    pos_visited.add(tuple(T_pos))
    #part 1
    for movement in head_movement:
        for i in range(int(movement[1])):
            H_pos_mem = copy.deepcopy(H_pos)
            move_head(H_pos, movement[0])
            if abs(T_pos[0]-H_pos[0]) > 1 or abs(T_pos[1]-H_pos[1]) > 1:
                T_pos = H_pos_mem
                pos_visited.add (tuple(T_pos))
    print(len(pos_visited))
    # part #2
    rope_pos = [[0,0] for i in range(10)]
    pos_visited =set()
    pos_visited.add(tuple(rope_pos[-1]))
    
    for movement in head_movement:
        head = [0]
        print(movement)
        
        for i in range(int(movement[1])):
            head_rejoin = False
            head_end_mem = copy.deepcopy(rope_pos[head[-1]])
            for knot in range(10):
                if knot in head:
                    move_head(rope_pos[knot], movement[0])
                else:
                    if abs(rope_pos[knot][0] - rope_pos[knot - 1][0]) > 1 or abs(rope_pos[knot][1] - rope_pos[knot - 1][1]) > 1:
                        if not head_rejoin:
                            head_rejoin = True
                            relative_movement = [head_end_mem[0] - rope_pos[knot][0], head_end_mem[1] - rope_pos[knot][1]]
                            rope_pos[knot] = head_end_mem
                            head.append(knot)
                        else:
                            rope_pos[knot][0] += relative_movement[0]
                            rope_pos[knot][1] += relative_movement[1]
            pos_visited.add(tuple(rope_pos[-1]))
        print(rope_pos)
    print(len(pos_visited))

   
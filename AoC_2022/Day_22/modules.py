import re

DIRECTION = [('x', 1, '>'), ('y', 1, 'v'), ('x', -1, '<'), ('y', -1, '^')]

def get_instructions(path):
    #get the list of tiles movement
    pattern = r'\d+'
    tile_moves = list(map(int, re.findall(pattern, path)))
    #get the list of direction
    pattern = r'[R|L]'
    direction = [0]
    for match in re.findall(pattern, path):
        if match == 'R':
            direction.append((direction[-1] + 1) % 4)
        else:
            direction.append((direction[-1] - 1) % 4)
    return tile_moves, direction

def get_board(board):
    max_line = max(map(len,board))
    return [[char for char in line + ' ' * (max_line - len(line))] for line in board]

def check_next_tile(offset, dir, board, start_y, start_x, sens, dim):
    if DIRECTION[dir][0] == 'x':
        offset[1] += 1
    else:
        offset[0] += 1  
    return board[(start_y + offset[0] * sens) % dim[0]][(start_x + offset[1] * sens) % dim[1]]
              
def tile_move(board, dim, curr_pos, move, dir):
    offset = [0, 0]
    start_y, start_x = curr_pos
    blocked = False
    iter = 0
    sens = DIRECTION[dir][1]
    while not blocked and iter <= move:
        board[curr_pos[0]][curr_pos[1]] = DIRECTION[dir][2]
        next_tile = check_next_tile(offset, dir, board, start_y, start_x, sens, dim)
        while iter < move:
            if next_tile == ' ':
                next_tile = check_next_tile(offset, dir, board, start_y, start_x, sens, dim)
            elif next_tile == '#':
                blocked = True
                break
            else:
                curr_pos = [(start_y + (offset[0]) * sens) % dim[0], (start_x + (offset[1]) * sens) % dim[1]]
                break
        iter += 1
    return curr_pos
    
def print_board(board):
    print("\033c")
    print(sep ='\n', *[''.join(line) for line in board])   
     
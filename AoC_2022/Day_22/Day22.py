import sys, time
from get_aoc import get_inputs
from modules import get_instructions, get_board, tile_move, print_board

def main():
    start = time.perf_counter()
    inputs = get_inputs(__file__).split('\n\n')
    tile_moves, direction = get_instructions(inputs[1])
    board = get_board(inputs[0].split('\n'))
    dim = [len(board), len(board[0])]
    curr_pos = [0, board[0].index('.')]  
    for i, move in enumerate(tile_moves):
        curr_pos = tile_move(board, dim, curr_pos, move, direction[i])            
        result = lambda x, y: 1000 * (x[0] + 1) + 4 * (x[1] + 1) + y
    # print_board(board)
    print(result(curr_pos, direction[-1]))
    print(time.perf_counter()- start)

if __name__ == '__main__':
    sys.exit(main())
    
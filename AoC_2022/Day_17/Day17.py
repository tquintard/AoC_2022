import sys, time
from get_aoc import get_inputs
from tetris import Blocks

BLOCK_SHAPES = ['-', '+', 'L', '|', 'O']

def main():
    start = time.perf_counter()
    jets = get_inputs(__file__)
    # init of lists to collect the position occupied by resting block, 
    # list of [shape, jet dir, block pos] and height of resting blocks
    tiles_filled, shape_dir_hpos, grid_height = [], [], []
    dir, shape, height_grid = 0, 0 , 0
    while True:
        block = Blocks(BLOCK_SHAPES[shape % len(BLOCK_SHAPES)], height_grid + 3, 2)
        while not(block.resting):
            jet = jets[dir % len(jets)]
            block.move_block(jet, tiles_filled)
            dir += 1
        height_grid = block.max_v + 1 if block.max_v + 1 > height_grid else height_grid
        tiles_filled += block.coords
        couple = (shape % len(BLOCK_SHAPES), dir % len(jets), block.min_h)
        # test to see if a resting block at given shape, last jet dir received and block hor position
        # is already exisiting in the couple_shape_dir, if yes then a repetion is detected
        if couple in shape_dir_hpos:
            break
        else:
            shape_dir_hpos.append(couple)
            grid_height.append(height_grid)
        shape += 1
    blocks_before_rept = shape_dir_hpos.index(couple) + 1
    height_before_rept = grid_height[shape_dir_hpos.index(couple)]
    blocks_in_rept =  shape - blocks_before_rept + 1
    for part in [1, 2]:
        all_blocks = 2022 if part == 1 else 1_000_000_000_000
        nb_rep = (all_blocks - blocks_before_rept) // blocks_in_rept
        rept_height = (height_grid - height_before_rept) * nb_rep
        remaining_block = all_blocks - (blocks_before_rept + nb_rep * blocks_in_rept)
        remaining_height = grid_height[shape_dir_hpos.index(couple) + remaining_block] - height_before_rept       
        print(height_before_rept + rept_height + remaining_height)
    print(time.perf_counter()- start)
if __name__ == '__main__':
    sys.exit(main())
    
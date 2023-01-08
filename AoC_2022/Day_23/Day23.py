import sys, time
from get_aoc import get_inputs
from modules import print_grid

def main():
    start = time.perf_counter()
    grid = [[char for char in line] for line in get_inputs(__file__, True).splitlines()]
    print_grid(grid)


    print(time.perf_counter()- start)

if __name__ == '__main__':
    sys.exit(main())
    
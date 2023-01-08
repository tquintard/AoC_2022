import sys, time
from get_aoc import get_inputs
from modules import SNAFU_to_b10, b10_to_SNAFU

def main():
    start = time.perf_counter()
    snafu = [line for line in get_inputs(__file__).splitlines()]
    sum_b10 = sum(map(SNAFU_to_b10,snafu))
    print(b10_to_SNAFU(sum_b10))
    print(time.perf_counter()- start)

if __name__ == '__main__':
    sys.exit(main())
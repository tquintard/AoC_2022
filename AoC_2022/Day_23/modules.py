def print_grid(grid):
    print("\033c")
    print(sep ='\n', *[''.join(line) for line in grid])   
     
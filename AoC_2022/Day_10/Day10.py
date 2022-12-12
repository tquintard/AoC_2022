import time
start = time.perf_counter()
with open(r'AoC_2022\Day_10\Day10.txt', "r") as f:
    program = [line.split() for line in f.read().splitlines()]
    register = [1]
    for line in program:
        if line[0] == 'noop': #takes 1 cycle
            register.append(register[-1]) #add a cycle with previous value
        else: #takes 2 cycles
            register.append(register[-1]) #add a cycle with previous value
            register.append(register[-1] + int(line[1])) #add a cycle with previous value + the value of command
    #Part 1
    print(sum([register[i] * (i + 1) for i in range(19, 220, 40)]))
    #Part 2
    CRT = ['' for i in range(6)]
    for cycle, value in enumerate(register[:-1]):
        CRT_row = cycle // 40
        start_pos = int(value)
        sprit_pos = range(start_pos, start_pos + 3)
        if (cycle + 1 - CRT_row * 40) in sprit_pos:
            CRT[CRT_row] += '#'
        else:
            CRT[CRT_row] += '.'
    print(sep='\n', *CRT)
    print(time.perf_counter() - start)

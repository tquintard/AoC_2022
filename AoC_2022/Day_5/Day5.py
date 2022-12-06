import re
import copy
import time

def move_crates(crane_instructions, crates_positions, crate_model):
    temp_crates_positions = copy.deepcopy(crates_positions)
    #for each crane instruction:
    #   move the upper crate from source stack to target stack if crane model is 9000
    #   else, from bottom of crates to be moved, move the crate from soucre stack to target stack  
    for crane_instruction in crane_instructions:
        for i in range(-crane_instruction[0],0):
            i = -1 if crate_model == 9000 else i
            temp_crates_positions[crane_instruction[2]-1].append(temp_crates_positions[crane_instruction[1]-1][i])
            temp_crates_positions[crane_instruction[1]-1].pop(i)
    return temp_crates_positions

start = time.perf_counter()
with open('Day5.txt', "r") as f:
    #get all the inputs
    inputs = f.read().splitlines()
    #find the line that separate the crates position and the cranes moving instructions and define the number of stack of crate
    line_separator = inputs.index('')
    nb_stack_of_crates = max(map(int,inputs[line_separator - 1].split()))
    #built a list for the initial crates position. List to be transposed in order to be easier to work with
    crates_positions = [[crates_position[1 + i * 4] for crates_position in inputs[:line_separator-1][::-1] 
                            if crates_position[1 + i * 4] != ' '] 
                            for i in range(nb_stack_of_crates)]
    #built a list for the initial crane instructions in form of [nb_crates_to_move, stack_source, stack_target]
    pattern = re.compile(r"(\d+)")
    crane_instructions = [[int(match.group(1)) for match in pattern.finditer(crane_instruction)] 
                            for crane_instruction in inputs[line_separator + 1:]]
    #Part 1
    print (''.join([stack[-1] for stack in move_crates(crane_instructions, crates_positions, 9000)]))
    #Part 2
    print (''.join([stack[-1] for stack in move_crates(crane_instructions, crates_positions, 9001)]))
    print((time.perf_counter() - start) * 1000)

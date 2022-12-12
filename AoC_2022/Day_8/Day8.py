import time
start = time.perf_counter()

def look_around_scenic(actual_tree,directions):
    global scenic_score
    local_scenic_score = 1
    for direction in directions:
        direction_scenic_score = 0    
        for tree in direction:
            direction_scenic_score += 1
            if actual_tree <= tree:
                break
        local_scenic_score = local_scenic_score * direction_scenic_score
    return local_scenic_score if local_scenic_score > scenic_score else scenic_score

def look_around_max(actual_tree,directions):
    for direction in directions:
        if tree > max(direction):
            return 1
    return 0

with open(r'AoC_2022\Day_8\Day8.txt', "r") as f:
    inputs = f.read().splitlines()
    nb_cols = len(inputs[0])
    nb_rows = len(inputs)
    #create suitable matrix of row of trees and column of tree
    row_of_trees = [[] for i in range(nb_rows)]
    col_of_trees = [[] for i in range(nb_cols)]
    for row, trees in enumerate(inputs):
        for col, tree in enumerate(trees):
            row_of_trees[row].append(int(tree))
            col_of_trees[col].append(int(tree))
    
    total_of_tree_visible = (nb_cols + nb_rows - 2)*2
    scenic_score = 0
    for row, trees in enumerate(row_of_trees[1:-1]):
        for col, tree in enumerate(trees[1:-1]):
            all_directions = (trees[:col + 1][::-1], trees[col + 2:], col_of_trees[col+1][:row + 1][::-1], col_of_trees[col+1][row + 2:])
            #Part 1
            total_of_tree_visible += look_around_max(tree,all_directions)
            #Part 2
            scenic_score = look_around_scenic(tree,all_directions)
            
    print(total_of_tree_visible)            
    print(scenic_score)
    print((time.perf_counter() - start)*1000)

    

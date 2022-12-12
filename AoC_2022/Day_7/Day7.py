import time
start = time.perf_counter()

def size_children_folder(tree, branch):
    size_folder = 0
    for children in branch[1]:
        tagert_folder_path = branch[0] + '/' + children
        for children_branch in tree:
            if children_branch[0] == tagert_folder_path:
                children_branch[2] += size_children_folder(tree, children_branch)
                size_folder += children_branch[2]
                break
    return size_folder 
                
with open(r'AoC_2022\Day_7\Day7.txt', "r") as f:
    inputs = f.read().splitlines()
    tree = [['', [], 0]]
    folder_navigation = ['']
    for line, command in enumerate(inputs[1:]):
        if command == '$ cd ..':
            # if the cmd is cd .. then pop the last item of the folder_navigation to know what is the actual folder
            folder_navigation.pop()
        elif command[:4] == '$ cd':
            # if the command navigate through a folder, append the folder to the strucutre
            # folder data are presented as [path, [children], size, parent]
            folder_navigation.append(command[5:])
            tree.append(['/'.join(folder_navigation), [], 0])
        elif command[:4] == '$ ls':
            line += 2
            while inputs[line][:4] != '$ cd':
                if inputs[line][:3] == 'dir':
                    tree[-1][1].append(inputs[line][4:])
                else:
                    tree[-1][2] += int(inputs[line].split()[0])
                if line < len(inputs) - 1:
                    line += 1
                else:
                    break
    #at this point, every folder is identified with its childrens
    # only the size of the files in the folder has been counted, remains to add the size of children folders
    tree[0][2] += size_children_folder(tree, tree[0])
    #Part 1
    print(sum([branch[2] for branch in tree if branch[2] <= 100000 and branch[2] > 0 ]))
    #Part 2
    total_disk_space = 70000000
    required_space_for_update = 30000000
    space_to_free = tree[0][2] - (total_disk_space - required_space_for_update)
    print(min([branch[2] for branch in tree if branch[2] >= space_to_free]))
    print(time.perf_counter() - start)

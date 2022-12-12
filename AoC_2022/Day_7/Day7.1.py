import time
start = time.perf_counter()

class Dir:
    def __init__(self, name):
        self.name = name
        self.subfolders = dict()
        self.size = 0
        
def size_children_folder(folder):
    global total_size
    for subfolder in folder.subfolders:
        folder.size += size_children_folder(folder.subfolders[subfolder])[0]
    total_size += folder.size if folder.size < 100000 else 0
    return folder.size, total_size

def find_folder_to_delete(folder):
    global folder_to_delete
    for subfolder in folder.subfolders:
        find_folder_to_delete(folder.subfolders[subfolder])
    if folder.size >= space_to_free and folder.size < folder_to_delete.size:
        folder_to_delete = folder
    return folder_to_delete.size

with open(r'AoC_2022\Day_7\Day7.txt', "r") as f:
    inputs = f.read().splitlines()
    root = Dir('/')
    folder_navigation = [root]
    for line, command in enumerate(inputs[1:]):
        actual_dir = folder_navigation[-1]
        if command == '$ cd ..':
            folder_navigation.pop()
        elif command[:4] == '$ cd':
            folder_navigation.append(actual_dir.subfolders[command[5:]])
        elif command[:4] == '$ ls':
            line += 2
            while inputs[line][:4] != '$ cd':
                if inputs[line][:3] == 'dir':
                    actual_dir.subfolders[inputs[line][4:]] = Dir(inputs[line][4:])
                else:
                    actual_dir.size += int(inputs[line].split()[0])
                if line < len(inputs) - 1:
                    line += 1
                else:
                    break
    #Part 1
    total_size = 0
    print(size_children_folder(root)[1])
    #Part 2    
    size_limit = 70000000 - 30000000
    space_to_free = root.size - size_limit
    folder_to_delete = root
    #find_folder_to_delete(root)
    print(find_folder_to_delete(root))
    # print(size_folder_to_delete)
    print(time.perf_counter() - start)

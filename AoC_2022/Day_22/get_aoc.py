import os

def get_inputs(file, is_sample = False):
    # Get the relative path of the file folder
    script_dir = os.path.dirname(os.path.realpath(file))
    day = os.path.splitext(os.path.basename(file))[0]
    # Get the current working directory
    cwd = os.getcwd()
    # Get the relative path
    relative_path = os.path.relpath(script_dir, cwd)
    txt_file = f'example.txt' if is_sample else f'{day}.txt'
    with open(os.path.join(relative_path, txt_file), "r") as f:
        return f.read()
    

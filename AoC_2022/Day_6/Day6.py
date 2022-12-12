import time
start = time.perf_counter()

def find_marker(inputs, nb_distinct_char):
    for i in range(len(inputs) - nb_distinct_char):
        chunks = inputs[i:i+nb_distinct_char]
        if len(chunks) == len(set(chunks)):
            return i + nb_distinct_char

with open('Day6.txt', "r") as f:
    inputs = f.read()
    print(find_marker(inputs, 4), find_marker(inputs, 14))
    print((time.perf_counter() - start)*1000)

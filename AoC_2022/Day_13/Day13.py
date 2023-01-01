import time
def is_in_right_order(pair):
    min_item = min(map(len,pair))
    for i, item in enumerate(pair[0][:min_item]): #look on the left signal
        if isinstance(item, int) and isinstance(pair[1][i], int):
            if item < pair[1][i]:
                return True
            elif item > pair[1][i]:
                return False
        elif isinstance(item, list) and isinstance(pair[1][i], list):
            test = is_in_right_order([item, pair[1][i]])
            if test:
                return True
            elif test == False:
                return False
        elif isinstance(item, int):
            test = is_in_right_order([[item], pair[1][i]])
            if test:
                return True
            elif test == False:
                return False
        elif isinstance(pair[1][i], int):
            test = is_in_right_order([item, [pair[1][i]]])
            if test:
                return True
            elif test == False:
                return False
    if len(pair[0])<len(pair[1]):
        return True
    elif len(pair[0])>len(pair[1]):
        return False

start = time.perf_counter()
with open(r'AoC_2022\Day_13\Day13.txt', "r") as f:
    signals = [eval(signal) for signal in f.read().splitlines() if signal != '']
    #Part 1
    sum_indices = 0
    for idx in range(0, len(signals), 2):
        sum_indices += idx // 2 + 1 if is_in_right_order([signals[idx], signals[idx + 1]]) else 0

    print(sum_indices)
    
    #Part 2
    signals.append([[6]])
    signals.append([[2]])
    for idx in range(len(signals)):
        for j, temp_signal in enumerate(signals[idx + 1:]):
            if not is_in_right_order([signals[idx], temp_signal]):
                signals[j + idx + 1] = signals[idx]
                signals[idx] = temp_signal

    print((signals.index([[6]]) + 1) * (signals.index([[2]]) + 1))
    print(time.perf_counter() - start)

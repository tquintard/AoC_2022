import copy
def set_monkeys(inputs):
    global mod
    monkeys_info = copy.deepcopy(inputs)
    monkeys =[]
    mod = 1
    for monkey in monkeys_info:
        #Starting items
        monkey[0] = list(map(int,monkey[0].split(": ")[1].split(", ")))
        #Operation
        operand = int(monkey[1][25:]) if monkey[1][25:] != 'old' else monkey[1][25:]
        monkey[1] = [monkey[1][23], operand]
        #Dividend
        monkey[2] = int(monkey[2].split()[-1])
        #Target monkey (true, false)
        monkey[3] =[int(monkey[3].split()[-1]), int(monkey[4].split()[-1])]
        monkey.pop()
        #add to the monkeys list
        monkeys.append(monkey)
        mod *= monkey[2]
    return monkeys

with open(r'AoC_2022\Day_11\Day11Bis.txt', "r") as f:
    monkeys_info = [monkey.splitlines()[1:] for monkey in f.read().split('\n\n')]  
    for part in range(2):
        monkeys = set_monkeys(monkeys_info)
        activity = [0 for monkey in monkeys]
        relief = 3 - part * 2
        nb_rounds = 20 + 9980 * part
        for round in range(nb_rounds):
            for i, monkey in enumerate(monkeys):
                activity[i] += len(monkey[0])
                for item in monkey[0]:
                    if monkey[1][1] == 'old':
                        if monkey[1][0] == '*':
                            item = (item ** 2) // relief
                        else:
                            item = (item * 2) // relief
                    else:
                        if monkey[1][0] == '*':
                            item = (item * monkey[1][1]) // relief
                        else:
                            item = (item + monkey[1][1]) // relief
                    item %= mod
                    target_monkey = monkey[3][0] if item % monkey[2] == 0 else monkey[3][1]
                    monkeys[target_monkey][0].append(item)
                monkey[0] = []
        print(sorted(activity)[-2] * sorted(activity)[-1])

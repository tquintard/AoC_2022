import operator as op

OPERATORS = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, '=': op.eq}

def create_monkeys():
    with open('AoC_2022\Day_21\Day21.txt', "r") as f:
        inputs = [line.split(': ') for line in f.read().splitlines()]
    monkeys = dict()
    for input in inputs:
        if input[1].isnumeric():
            monkeys[input[0]] = Monkey(input[0], value = int(input[1]))
        else:
            monkeys[input[0]] = Monkey(input[0], expression = input[1])
    return monkeys
    
class Monkey:
    def __init__(self, name, value = None, expression = None):
        self.name = name
        self._value = value
        self.expression = expression
        if self.expression:
            self.monkey_1, self.operand, self.monkey_2 = self.expression.split()
        
    @property
    def value(self):
        if self.expression:
            monkey_1 = monkeys[self.monkey_1].value
            monkey_2 = monkeys[self.monkey_2].value
            self._value = OPERATORS[self.operand](monkey_1, monkey_2)
        return self._value

if __name__ == '__main__':
    monkeys = create_monkeys()
    #Part 1
    print(int(monkeys['root'].value))

    #Part 2
    monkeys['root'].operand = '='
    monkey_1 = monkeys['root'].monkey_1
    monkey_2 = monkeys['root'].monkey_2
    increment = 1_000_000_000_000
    prev_monkey_1_sup_2 = monkeys[monkey_1]._value > monkeys[monkey_2]._value
    while not(monkeys['root'].value):
        curr_monkey_1_sup_2 = monkeys[monkey_1]._value > monkeys[monkey_2]._value
        increment //= -2 if prev_monkey_1_sup_2 != curr_monkey_1_sup_2 else 1
        prev_monkey_1_sup_2 = monkeys[monkey_1]._value > monkeys[monkey_2]._value
        monkeys['humn']._value += increment
    print(monkeys['humn']._value)

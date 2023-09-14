import numpy as np

class Monkey:
    '''
    Class for representing one Monkey (with my stuff)
    '''

    def __init__(self, id, items, operation, test, pass_monkey, fail_monkey):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.pass_monkey = pass_monkey
        self.fail_monkey = fail_monkey
        self.inspect_count = 0
    
    def get_items(self) -> list:
        return f"Monkey {self.id}: {self.items}"
    
    def add_items(self, items):
        self.items += items
    
    def test_items(self, lcm=1) -> dict:
        throw = {self.pass_monkey: [], self.fail_monkey: []}
        new_items = self.items.copy()
        for old in self.items:
            new = eval(self.operation)
            # new = new // 3 for part 1
            new = new % lcm # for part 2
            if new % self.test == 0:
                throw[self.pass_monkey].append(new)
            else:
                throw[self.fail_monkey].append(new)
            new_items.remove(old)
            self.inspect_count += 1
        self.items = new_items
        return throw

with open('2022/input/day11.txt') as file:
    text = file.readlines()
    monkeys = []
    for i in range(len(text)):
        line = text[i].split()
        if not line:
            continue
        if line[0] == "Monkey":
            id = int(line[1][0])
            items = [int(num[:2]) for num in text[i+1].split() if num[:2].isnumeric()]
            operation = text[i+2].strip()[17:]
            test = int(text[i+3].strip()[-2:])
            pass_monkey = int(text[i+4].strip()[-1])
            fail_monkey = int(text[i+5].strip()[-1])
            monkeys.append(Monkey(id, items, operation, test, pass_monkey, fail_monkey))

    lcm = np.lcm.reduce([monkey.test for monkey in monkeys]) # for part 2
    for i in range(10000): # number of rounds: 20 in part one
        for monkey in monkeys:
            throw = monkey.test_items(lcm)
            for i in throw:
                monkeys[i].add_items(throw[i])

    inspect_count = []
    for monkey in monkeys:
        inspect_count += [monkey.inspect_count]

    sorted_count = sorted(inspect_count, reverse=True)
    print(f"Monkey business: {sorted_count[0] * sorted_count[1]}")
with open('2022/input/day5.txt') as file:
    # only works on this specific file due to weird spacing conventions
    n = 4
    stacks = []
    for line in file:   
        if line == "\n":
            break
        line = [line[i+1] for i in range(0, len(line), n)]
        stacks.append(line)
    stacks.pop()
    stacks = [list(i) for i in zip(*stacks)]
    for i in range(len(stacks)):
        stacks[i] = [x for x in stacks[i] if x != ' ']
        stacks[i].reverse()

    # keep_order = False for part 1, keep_order = True for part 2
    count = 0
    for line in file:
        moves = line.split()
        boxes = stacks[int(moves[3]) - 1][-int(moves[1]):]
        keep_order = True
        if keep_order:
            boxes.reverse()
        stacks[int(moves[3]) - 1] = stacks[int(moves[3]) - 1][:-int(moves[1])]
        stacks[int(moves[5]) - 1] += boxes
        

    message = ""
    for stack in stacks:
        message += stack[-1]
    
    print(message)
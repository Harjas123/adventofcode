def signal_strength(instructions):
    x = 1
    cycle = 0
    signal = 0
    for line in instructions:
        cycle += 1
        if cycle % 40 == 20:
            signal += x * cycle
        if line[0] == "addx":
            cycle += 1
            if cycle % 40 == 20:
                signal += x * cycle
            x += int(line[1])
    return signal

def print_sprite(instructions):
    sprite = [0, 1, 2]
    cycle = 0
    for line in instructions:
        if cycle in sprite:
            print("##", end="")
        else:
            print("  ", end="")
        cycle += 1
        if cycle % 40 == 0:
            cycle = 0
            print()
        if line[0] == "addx":
            if cycle in sprite:
                print("##", end="")
            else:
                print("  ", end="")
            cycle += 1
            if cycle % 40 == 0:
                cycle = 0
                print()
            sprite = [num + int(line[1]) for num in sprite]

with open("2022/input/day10.txt") as file:
    text = file.read().splitlines()
    instructions = [row.split() for row in text]
    
    strength = signal_strength(instructions)
    print(strength)
    
    print_sprite(instructions)
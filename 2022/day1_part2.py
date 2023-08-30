
elves = []
current = 0

with open('input/day1.txt', "r") as file:
    for line in file:
        if line.strip():
            current += int(line)
        else:
            elves.append(current)
            current = 0

elves.sort(reverse=True)
print(sum(elves[:3]))
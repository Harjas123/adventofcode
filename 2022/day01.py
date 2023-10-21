max = 0
current = 0
elves = []

with open('2022/input/day01.txt', "r") as file:
    for line in file:
        if line.strip():
            current += int(line)
        else:
            elves.append(current)
            if current > max:
                max = current
            current = 0

print(max)
elves.sort(reverse=True)
print(sum(elves[:3]))
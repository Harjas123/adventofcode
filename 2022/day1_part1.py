
max = 0
current = 0

with open('input/day1.txt', "r") as file:
    for line in file:
        if line.strip():
            current += int(line)
        else:
            if current > max:
                max = current
            current = 0

print(max)
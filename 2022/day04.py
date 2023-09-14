import re

# parts 1 & 2
full_overlap = 0
overlap = 0
with open('2022/input/day4.txt') as file:
    for line in file:
        sections = re.split(",|-", line[:-1])
        sections = [int(x) for x in sections]
        range1 = set(range(sections[0], sections[1]+1))
        range2 = set(range(sections[2], sections[3]+1))
        if range1.issubset(range2) or range2.issubset(range1):
            full_overlap += 1
            overlap += 1
        elif sections[0] in range2 or sections[2] in range1:
            overlap += 1

print(full_overlap)
print(overlap)
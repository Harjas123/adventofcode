
def char_to_num(str) -> list[int]:
    ints = list(str.encode("ascii"))
    for i in range(len(ints)):
        if ints[i] >= ord("a"):
            ints[i] -= ord("a") - 1
        else:
            ints[i] -= ord("A") - 27
    return ints

def common_values(list1, list2) -> list:
    return list(set(list1) & set(list2))

# part 1
total = 0
with open('2022/input/day3.txt', "r") as file:
    for line in file:
        line1 = char_to_num(line[:(len(line)//2)])
        line2 = char_to_num(line[len(line1):-1])
        value = common_values(line1, line2)
        total += value[0]

print(total)

# part 2
total = 0
with open('2022/input/day3.txt', "r") as file:
    for line in file:
        line1 = char_to_num(line)
        line2 = char_to_num(file.readline()[:-1])
        line3 = char_to_num(file.readline()[:-1])
        value = common_values(line1, line2)
        value = common_values(value, line3)
        total += value[0]

print(total)
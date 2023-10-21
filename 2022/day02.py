replace = {"A":1, "X":1, "B":2, "Y" :2, "C":3, "Z":3}

myscore1 = 0
myscore2 = 0

with open('2022/input/day02.txt', "r") as file:
    for line in file:
        round = line.split()
        round[0] = replace[round[0]]
        round[1] = replace[round[1]]
        myscore1 += round[1]
        result = round[1] - round[0]

        #part 1
        if result == 0:
            myscore1 += 3
        if result == 1 or result == -2:
            myscore1 += 6

        #part 2
        myscore2 += round[0]
        if round[1] == 1:
            myscore2 -= 1
            if round[0] == 1:
                myscore2 += 3
        elif round[1] == 2:
            myscore2 += 3
        elif round[1] == 3:
            myscore2 += 7
            if round[0] == 3:
                myscore2 -= 3

print(myscore1)
print(myscore2)
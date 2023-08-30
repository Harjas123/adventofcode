
replace = {"A":1, "X":1, "B":2, "Y" :2, "C":3, "Z":3}

myscore = 0
with open('input/day2.txt', "r") as file:
    for line in file:
        round = line.split()
        round[0] = replace[round[0]]
        round[1] = replace[round[1]]
        myscore += round[1]
        result = round[1] - round[0]
        if result == 0:
            myscore += 3
        if result == 1 or result == -2:
            myscore += 6

print(myscore)
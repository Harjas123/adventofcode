
replace = {"A":1, "B":2, "C":3}

myscore = 0
with open('2022/input/day2.txt', "r") as file:
    for line in file:
        round = line.split()
        round[0] = replace[round[0]]
        myscore += round[0]
        if round[1] == "X":
            myscore -= 1
            if round[0] == 1:
                myscore += 3
        elif round[1] == "Y":
            myscore += 3
        elif round[1] == "Z":
            myscore += 7
            if round[0] == 3:
                myscore -= 3

print(myscore)
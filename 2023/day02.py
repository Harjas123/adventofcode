sum = 0
with open('2023/input/day02.txt', "r") as file:
    count = 0
    for line in file:
        possible = True
        game = line[8:].split(sep=";")
        for round in game:
            i = 0
            rgb = {"r":12, "g":13, "b":14}
            while i < len(round):
                if round[i].isdigit():
                    num = round[i]
                    if round[i+1].isdigit():
                        num += round[i+1]
                        i += 1
                    #print(num, end="")
                    i += 2
                    #print(round[i])
                    rgb[round[i]] -= int(num)
                    if rgb[round[i]] < 0:
                        break #seems to work
                i += 1
            #print(round, i, len(round))
            if i < len(round)-1:
                possible = False
                break
        count += 1
        if possible:
            sum += count
    print(sum)
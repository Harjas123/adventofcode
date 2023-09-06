def sum_dir(text_list):
    total = 0
    layers = 0
    for i in range(len(text_list)):
        if text_list[i] == "$ cd ..":
            layers -= 1
            if layers < 0:
                break
        elif text_list[i][:4] == "$ cd":
            layers += 1
            if layers > 1:
                continue
            yield from sum_dir(text_list[i+1:])
        elif text_list[i][0].isnumeric():
            total += int(text_list[i].split()[0])
    yield total

with open('2022/input/day7.txt') as file:
    text = file.read().splitlines()
    dir_sizes = list(sum_dir(text[1:]))
    # part 1
    sum = 0
    for dir_size in dir_sizes:
        if dir_size <= 100000:
            sum += dir_size
    print(sum)
    # part 2
    space_needed = 30000000 - (70000000 - dir_sizes[-1])
    dir_sizes.sort()
    for dir_size in dir_sizes:
        if dir_size >= space_needed:
            print(dir_size)
            break
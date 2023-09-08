import numpy as np

def is_visible(trees, x, y):
    height = trees[y][x]
    left, right, up, down = trees[y][:x], trees[y][x+1:], trees[:y, x],trees[y+1:, x]
    directions = [left, right, up, down]
    for dir in directions:
        if max(dir, default=-1) < height:
            return True
    return False

def scenic_score(trees, x, y):
    height = trees[y, x]
    distance = 1
    left, right, up, down = trees[y, x::-1], trees[y, x:], trees[y::-1, x], trees[y:, x]
    directions = [left, right, up, down]
    for dir in directions:
        for i in range(1, len(dir)):
            if dir[i] >= height:
                break
        distance *= i
    return distance


with open('2022/input/day8.txt') as file:
    treecount = 0
    # part 1
    text = file.read().splitlines()
    trees = np.array([list(row) for row in text], dtype=int)
    for y in range(0, len(trees)):
        for x in range(0, len(trees)):
            if is_visible(trees, x, y):
                treecount += 1
    print(treecount)
    # part 2
    record = 0
    for y in range(1, len(trees) - 1): # counting the rows top down
        for x in range(1, len(trees) - 1):
            score = scenic_score(trees, x, y)
            if score > record:
                record = score
    print(record)
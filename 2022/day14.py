import numpy as np
import re

with open('2022/input/day14sample.txt') as file:
    text = file.read().splitlines()
    text = [re.split(" -> |,", line) for line in text]

for line in text:
    for i in range(0, len(line), 2):
        print(f"{line[i]}, {line[i+1]}")
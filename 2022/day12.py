import numpy as np

def len_best_path(map, start=str):
    starts = np.argwhere(map == start).tolist()
    lengths = []
    for position in starts:
        length = len_path(map, tuple(position))
        if length:
            lengths.append(length)
    paths = sorted(lengths, reverse=True)
    return min(paths)

def len_path(map, start=tuple):
    queue = [start]
    visited = {start}
    dist = {start: 0}

    while len(queue) > 0:
        current = queue.pop(0)
        y, x = current

        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new = (y+dy, x+dx)
            if new[0] < 0 or new[0] > len(map) - 1 or new[1] < 0 or new[1] > len(map[0]) - 1:
                continue

            elev_change = ord(map[current]) - ord(map[new])
            if elev_change < -1 or new in visited:
                continue
            
            visited.add(new)
            dist[new] = dist[current] + 1
            queue.append(new)

            if map[new] == '{':
                return dist[new]

    return None

with open('2022/input/day12.txt') as file:
    map = np.array([list(line.strip()) for line in file])
    start = tuple(np.argwhere(map == "S")[0])
    end = tuple(np.argwhere(map == "E")[0])
    map[start] = "a"
    map[end] = "{"

    path_1 = len_path(map, start)
    path_2 = len_best_path(map, "a")

    print(f"Task 1: {path_1}, Task 2: {path_2}")
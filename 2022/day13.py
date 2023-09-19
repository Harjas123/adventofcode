import ast

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if compare(left[index_left], right[index_right]):
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


def compare(left, right):
    shortest = min(len(left), len(right))
    ordered = None
    for i in range(shortest):
        left_type = type(left[i])
        right_type = type(right[i])
        if left_type == list: # if left is list
            if right_type == int: # if right is int, convert it to a list
                right[i] = [right[i]]
            ordered = compare(left[i], right[i]) # compare 2 new lists
        elif right_type == list: # if right is list
            if left_type == int: # if left is int, convert it to a list
                left[i] = [left[i]]
            ordered = compare(left[i], right[i]) # compare 2 new lists
        elif right_type == left_type == int: # if both are ints, direct compare
            if left[i] < right[i]:
                return True
            if left[i] > right[i]:
                return False
        if ordered != None:
            return ordered
    
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False

with open('2022/input/day13.txt') as file:
    text = file.read()
    text = text.splitlines()
    all_packets = []
    # part 1
    sum = 0
    for i in range(0, len(text), 3):
        left = ast.literal_eval(text[i])
        right = ast.literal_eval(text[i + 1])
        ordered = compare(left, right)
        if ordered:
            sum += i // 3 + 1
        all_packets.append(left)
        all_packets.append(right)
    print(sum)
    # part 2
    all_packets.append([2])
    all_packets.append([6])
    sorted = merge_sort(all_packets)
    print((sorted.index([[[[2]]]]) + 1) * (sorted.index([[[[6]]]]) + 1))
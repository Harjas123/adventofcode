def get_digit_indices(line: str) -> list:
    '''
    Given a string, return the indices of the first and last numerical digit in the string.
    If none are found, returns [-1, -1].
    '''
    first = -1
    for i in range(0, len(line)):
        if line[i].isdigit():
            first = i
            break

    last = -1
    for j in range(1, len(line) + 1):
        if line[-j].isdigit():
            last = len(line) - j
            break
    
    indices = [first, last]
    return indices

def get_numbers(NUM_DICT: dict, line: str, first_digit_index=-1, last_digit_index=0) -> list:
    '''
    Given a string, return the indices of the first and last number, including letters and digits.
    If first_digit_index and last_digit_index are provided,
    number_indices will only search for word_numbers before first_digit_index and after last_digit_index.
    '''
    word_positions1 = {}
    word_positions2 = {}
    for num in NUM_DICT.keys():
        position1 = line[:first_digit_index].find(num)
        position2 = line[last_digit_index:].rfind(num)
        if position1 != -1:
            word_positions1[num] = position1
        if position2 != -1:
            word_positions2[num] = position2 + last_digit_index
    
    first_last = [line[first_digit_index], line[last_digit_index]]
    if word_positions1:
        first_word = min(word_positions1, key=word_positions1.get)
        first_word_index = word_positions1[first_word]
        if first_digit_index > first_word_index:
            first_last[0] = NUM_DICT[first_word]

    if word_positions2:
        last_word = max(word_positions2, key=word_positions2.get)    
        last_word_index = word_positions2[last_word]
        if last_digit_index < last_word_index:
            first_last[1] = NUM_DICT[last_word]
    
    return first_last

NUM_DICT = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
    }

sum1 = 0
sum2 = 0
with open('2023/input/day01.txt', "r") as file:
    for line in file:
        first, last = get_digit_indices(line)
        digit1 = line[first]
        digit2 = line[last]
        sum1 += int(digit1 + digit2)
        
        first_last = get_numbers(NUM_DICT, line, first, last)
        num1 = first_last[0]
        num2 = first_last[1]
        sum2 += int(num1 + num2)
    print(sum1)
    print(sum2)

# some comment
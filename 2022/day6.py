def packet_marker(text, marker_length):
    for i in range(len(text)):
        packet = text[i:i+marker_length]
        packet = set(packet)
        if len(packet) == marker_length:
            return i + marker_length

with open('2022/input/day6.txt') as file:
    text = file.read()
    # part 1
    print(packet_marker(text, 4))
    # part 2
    print(packet_marker(text, 14))
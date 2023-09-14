'''
My original solutions was a little bit shorter, but was also an unholy mess of nested lists that kept falling apart. This is better.

Also, I considered using linked lists for this problem, but I decided to make two separate classes instead: Knot, and Rope.
'''

class Knot:
    '''
    Class for representing one knot (in a rope)
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dir):
        if dir == "R":
            self.x += 1
        elif dir == "L":
            self.x -= 1
        elif dir == "U":
            self.y += 1
        elif dir == "D":
            self.y -= 1
    
    def follow(self, tail):
        dist = [self.x-tail.x, self.y-tail.y]
        if abs(dist[0]) >= 2:
            tail.x += int(dist[0] / 2)
            if abs(dist[1]) == 2:
                dist[1] = int(abs(dist[1])/ dist[1])
            tail.y += dist[1]
        elif abs(dist[1]) >= 2:
            tail.x += dist[0]
            tail.y += int(dist[1] / 2)

    def position(self) -> list:
        return [self.x, self.y]


class Rope:
    '''
    Class for representing a rope
    '''

    def __init__(self, x=0, y=0, knots=2):
        self.knots = [Knot(x, y) for i in range(knots)]
    
    def move_rope(self, dir: str):
        self.knots[0].move(dir)
        for j in range(len(self.knots) - 1):
            self.knots[j].follow(self.knots[j+1])
    
    def tail_position(self) -> tuple:
        return tuple(self.knots[-1].position())


with open('2022/input/day9.txt') as file:
    rope1 = Rope()
    rope2 = Rope(knots=10)
    positions1 = set()
    positions2 = set()
    for line in file:
        line = line.split()
        for i in range(int(line[1])):
            # task 1
            rope1.move_rope(dir=line[0])
            positions1.add(rope1.tail_position())
            # task 2
            rope2.move_rope(dir=line[0])
            positions2.add(rope2.tail_position())
    print(len(positions1))
    print(len(positions2))
import sys
sys.path.append('../aoclib')

from aoclib import Input
import re
from collections import defaultdict

class Robot:
    def __init__(self, x, y, xv, yv: int):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv

    def step(self, max_x, max_y, n=1):
        for _ in range(n):
            self.x = (self.x + self.xv) % max_x
            self.y = (self.y + self.yv) % max_y

class Map:
    def __init__(self, x, y: int, robots: list[Robot]):
        self.x = x
        self.y = y
        self.robots = robots
        self.steps = 0

    def __str__(self):
        field = [[0 for _ in range(self.x)] for _ in range(self.y)]
        for r in self.robots:
            field[r.y][r.x] += 1
        return '\n'.join(''.join('*' if x>0 else ' ' for x in l) for l in field)

    def step(self, n=1):
        for r in self.robots:
            r.step(self.x, self.y, n)
        self.steps += n

    def solve1(self) -> int:
        self.step(100)
        _x, _y = self.x // 2, self.y // 2
        field = [[0 for _ in range(self.x)] for _ in range(self.y)]
        for r in self.robots:
            field[r.y][r.x] += 1

        q1 = 0
        for y in range(0, _y):
            for x in range(0, _x):
                q1 += field[y][x]
        
        q2 = 0
        for y in range(0, _y):
            for x in range(_x+1, len(field[0])):
                q2 += field[y][x]

        q3 = 0
        for y in range(_y+1, len(field)):
            for x in range(0, _x):
                q3 += field[y][x]
        
        q4 = 0
        for y in range(_y+1, len(field)):
            for x in range(_x+1, len(field[0])):
                q4 += field[y][x]

        return q1*q2*q3*q4

    def solve2(self) -> int:
        while not self.has_n_adjacent(20):
            self.step()
        return self.steps
        

    def has_n_adjacent(self, n=10):
        d = defaultdict(set)
        for r in self.robots:
            d[r.x].add(r.y)

        def search(l, n):
            for i in range(len(l) - n):
                if l[i+n-1] - l[i] == n-1:
                    return True 
            return False

        for x in d:
            l = sorted(list(d[x]))
            if search(l, n):
                return True
        return False

                
def parse_input(lines: list[str], x, y: int):
    rrx = re.compile(r'p=(\d+),(\d+) v=(-*\d+),(-*\d+)')
    robots = list()
    for l in lines:
        m = rrx.search(l)
        r = Robot(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        robots.append(r)

    m = Map(x, y, robots)
    return m

def solve1(lines: list[str]):
    #m = parse_input(lines, 11, 7)
    m = parse_input(lines, 101, 103)
    return m.solve1()


def solve2(lines: list[str]):
    m = parse_input(lines, 101, 103)
    m.solve2()
    print(m)
    return m.steps


if __name__ == '__main__':
    #lines = Input('input_test.txt').lines()
    lines = Input('input.txt').lines()

    #part 1
    print('part 1:', solve1(lines)) # 27157

    #part 2
    print('part 2:', solve2(lines)) # 8258

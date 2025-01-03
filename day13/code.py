import sys
sys.path.append('../aoclib')

from aoclib import Input
import re

class Button:
    def __init__(self, cost, x, y):
        self.cost = cost
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}, cost: {self.cost}'


class Prize:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
        

class Machine:
    def __init__(self, a, b: Button, p: Prize):
        self.a = a
        self.b = b
        self.prize = p

    def __str__(self):
        s = ''
        s += 'B_A: ' + self.a.__str__() + '\n'
        s += 'B_B: ' + self.b.__str__() + '\n'
        s += 'Prize: ' + self.prize.__str__() + '\n' 
        return s
        

def parse_input(lines: list[str]) -> list[Machine]:
    lst = list()
    brx = re.compile(r'X\+(\d+), Y\+(\d+)')
    prx = re.compile(r'X=(\d+), Y=(\d+)')

    b_a = None
    b_b = None
    m = None
    for l in lines:
        if l.startswith('Button A'):
            m = brx.search(l)
            b_a = Button(3, int(m.group(1)), int(m.group(2)))
        if l.startswith('Button B'):
            m = brx.search(l)
            b_b = Button(1, int(m.group(1)), int(m.group(2)))
        if l.startswith('Prize'):
            m = prx.search(l)
            p = Prize(int(m.group(1)), int(m.group(2)))
            machine = Machine(b_a, b_b, p)
            lst.append(machine)

    return lst

def _solve1(m: Machine) -> int:
    max_a = min(m.prize.x // m.a.x, m.prize.y // m.a.y)+1
    max_b = min(m.prize.x // m.b.x, m.prize.y // m.b.y)+1

    costs = []
    for _a in range(max_a):
        for _b in range(max_b):
            x, y, cost = m.a.x*_a + m.b.x*_b, m.a.y*_a + m.b.y*_b, m.a.cost*_a + m.b.cost*_b 
            if x == m.prize.x and y == m.prize.y:
                costs.append(cost)

    if not costs:
        return None

    return min(costs)
    

def solve1(lines: list[str]):
    machines = parse_input(lines)

    cost = 0
    for m in machines:
        c = _solve1(m)
        if not c:
            continue
        cost += c
        
    return cost


def solve2(lines: list[str]):
    machines = parse_input(lines)

    cost = 0
    for m in machines[:1]:
        continue
        m.prize.x += 10000000000000
        m.prize.y += 10000000000000
        c = _solve1(m)
        if not c:
            continue
        cost += c
        
    return cost


if __name__ == '__main__':
    #lines = Input('input_test.txt').lines()
    lines = Input('input.txt').lines()

    #part 1
    print('part 1:', solve1(lines)) # 27157

    #part 2
    print('part 2:', solve2(lines)) # 862486

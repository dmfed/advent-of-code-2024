import sys
sys.path.append('../aoclib')

from aoclib import Input

L = '<'
U = '^'
R = '>'
D = 'v'

STR_ROBOT = '@'
STR_EMPTY = '.'
STR_WALL = '#'
STR_BOX = 'O'
STR_BOX_L = '['
STR_BOX_R = ']'

class Map:
    def __init__(self, grid: list[list]):
        self.grid = grid

    def __str__(self):
        return '\n'.join(''.join(str(p) for p in line) for line in self.grid)

    def swap(self, x1, y1, x2, y2):
        self.grid[y1][x1], self.grid[y2][x2] = self.grid[y2][x2], self.grid[y1][x1]

    def type_is(self, x, y: int, obj):
        return type(self.grid[y][x]) == type(obj)

    def robot_pos(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.type_is(x, y, Robot()):
                    return x, y
    

class Instruction:
    def __init__(self, s: str):
        self.dir = s

    def __str__(self):
        return self.dir

    def right(self) -> bool:
        return self.dir == R

    def left(self) -> bool:
        return self.dir == L

    def up(self) -> bool:
        return self.dir == U

    def down(self) -> bool:
        return self.dir == D
        

class Point:
    def __init__(self, s=STR_EMPTY):
        self.s = s

    def __str__(self):
        return self.s


class Robot(Point):
    def __init__(self, s=STR_ROBOT):
        super().__init__(s)
        

class Box(Point):
    def __init__(self, s=STR_BOX, left=False):
        super().__init__(s)
        self.l = left

    def is_left(self) -> bool:
        return self.l 

        
class Wall(Point):
    def __init__(self, s=STR_WALL):
        super().__init__(s)

class Solution:
    def __init__(self, m: Map, inst: list[Instruction]):
        self.m = m
        self.inst = inst

    def apply(self, cx, cy, ins: Instruction) -> bool:
        x, y = cx, cy
        if ins.up():
            y -= 1
        elif ins.down():
            y += 1
        elif ins.left():
            x -= 1
        elif ins.right():
            x += 1
        if self.m.type_is(x, y, Wall()):
            return False
        if self.m.type_is(x, y, Point()):
            self.m.swap(cx, cy, x, y)
            return True
        # we have a box
        if not self.apply(x, y, ins):
            return False

        self.m.swap(cx, cy, x, y)
        return True

    def apply_vert(self, cx, cy, ins: Instruction):
        x, y = cx, cy
        if ins.up():
            y -= 1
        elif ins.down():
            y += 1
        if self.m.type_is(x, y, Wall()):
            return
        if self.m.type_is(x, y, Point()):
            self.m.swap(cx, cy, x, y)
            return

        box = self.m.grid[y][x]

        if not self.move_box(x, y, box, ins):
            return
        self.move_box(x, y, box, ins, act=True)
        self.m.swap(cx, cy, x, y)

    def move_box(self, cx, cy, b: Box, ins: Instruction, act=False) -> bool:
        '''here comes the ugly part :) '''
        x1, y = cx, cy
        x2 = None
        if ins.up():
            y -= 1
        elif ins.down():
            y += 1
        if b.is_left():
            x2 = x1+1
        else:
            x2 = x1-1
        if self.m.type_is(x1, y, Point()) and self.m.type_is(x2, y, Point()):
            if act:
                self.m.swap(x1, cy, x1, y)
                self.m.swap(x2, cy, x2, y)
            return True

        if self.m.type_is(x1, y, Wall()) or self.m.type_is(x2, y, Wall()):
            return False

        m1, m2 = True, True

        if self.m.type_is(x1, y, Box()):
            box = self.m.grid[y][x1]
            m1 = self.move_box(x1, y, box, ins, act)

        if self.m.type_is(x2, y, Box()):
            box = self.m.grid[y][x2]
            m2 = self.move_box(x2, y, box, ins, act)

        if m1 and m2 and act:
            self.m.swap(x1, cy, x1, y)
            self.m.swap(x2, cy, x2, y)
        return m1 and m2
            

    def solve1(self):
        for ins in self.inst:
            x, y = self.m.robot_pos()
            self.apply(x, y, ins)
        s = 0
        for y in range(len(self.m.grid)):
            for x in range(len(self.m.grid[0])):
                if self.m.type_is(x, y, Box()):
                    s += y*100 + x
        return s
                    

    def solve2(self):
        for ins in self.inst:
            x, y = self.m.robot_pos()
            if ins.left() or ins.right():
                self.apply(x, y, ins)
            else:
                self.apply_vert(x, y, ins)
        s = 0
        for y in range(len(self.m.grid)):
            for x in range(len(self.m.grid[0])):
                if self.m.type_is(x, y, Box()) and self.m.grid[y][x].is_left():
                    s += y*100 + x
        return s
                    

def parse_input(lines: list[str]):
    grid = []
    instructions = []
    for l in lines:
        if l.startswith(STR_WALL):
            grid.append(list(l))
        elif not l:
            continue
        else:
            instructions.extend(Instruction(s) for s in list(l))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s = grid[y][x]
            obj = None
            if s == STR_WALL:
                obj = Wall()
            elif s == STR_BOX:
                obj = Box()
            elif s == STR_ROBOT:
                obj = Robot()
            else:
                obj = Point()
            grid[y][x] = obj 

    m = Map(grid)
    return Solution(m, instructions)


def parse_input2(lines: list[str]):
    grid = []
    instructions = []
    for l in lines:
        if l.startswith(STR_WALL):
            row = []
            for s in l:
                if s == STR_WALL:
                    row.extend([s, s])
                elif s == STR_BOX:
                    row.extend([STR_BOX_L, STR_BOX_R])
                elif s == STR_ROBOT:
                    row.extend([s, STR_EMPTY])
                elif s == STR_EMPTY:
                    row.extend([s, s])
            grid.append(row)
        elif not l:
            continue
        else:
            instructions.extend(Instruction(s) for s in list(l))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s = grid[y][x]
            obj = None
            if s == STR_WALL:
                obj = Wall()
            elif s == STR_BOX_L:
                obj = Box(s, True)
            elif s == STR_BOX_R:
                obj = Box(s, False)
            elif s == STR_ROBOT:
                obj = Robot()
            else:
                obj = Point()
            grid[y][x] = obj 

    m = Map(grid)

    return Solution(m, instructions)

def solve1(lines: list[str]):
    s = parse_input(lines)
    return s.solve1()


def solve2(lines: list[str]):
    s = parse_input2(lines)
    return s.solve2()


if __name__ == '__main__':
    #lines = Input('input_test.txt').lines()
    lines = Input('input.txt').lines()

    #part 1
    print('part 1:', solve1(lines)) # 1456590

    #part 2
    print('part 2:', solve2(lines)) # 1489116

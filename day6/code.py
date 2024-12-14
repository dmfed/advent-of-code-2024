import sys
sys.path.append('../aoclib')

from aoclib import Input
from time import sleep

D_U = '^'
D_R = '>'
D_D = 'v'
D_L = '<'


class Guard(object):
    dirs = [D_U, D_R, D_D, D_L]
    def __init__(self, x, y, dir: str):
        self.d = dir
        self.x = x
        self.y = y

    def turn(self):
        self.d = self.dirs[(self.dirs.index(self.d) + 1) % len(self.dirs)]

    def curr(self):
        return self.x, self.y

    def want(self):
        if self.d == D_U:
            return self.x, self.y-1
        elif self.d == D_R:
            return self.x+1, self.y
        elif self.d == D_D:
            return self.x, self.y+1
        elif self.d == D_L:
            return self.x-1, self.y

    def next(self):
        self.x, self.y = self.want()
        
    def __str__(self):
        return self.d


class Map(list):
    def __init__(self, l: list):
        super().__init__(l)

    def has_obstacle(self, x, y: int) -> bool:
        return self[y][x] == '#'

    def out_of_bounds(self, x, y):
        return (x < 0 or y < 0) or (x >= len(self[0]) or y >= len(self))


class Lab(object):
    def __init__(self, m: Map, g: Guard):
        self.m = m
        self.g = g
        self.visited = set()
        self.print_visited = False
        self.g_init = Guard(g.x, g.y, g.d)

    def next(self) -> bool:
        self.visited.add(self.g.curr())

        x, y = self.g.want()
        if self.m.out_of_bounds(x, y):
            return False
        elif self.m.has_obstacle(x, y):
            self.g.turn()
            return True

        self.g.next()
        return True

    def reset(self):
        self.visited = set()
        self.g = Guard(self.g_init.x, self.g_init.y, self.g_init.d)
        

    def solve_part1(self):
        while self.next():
            pass
        return len(self.visited)

    def animate(self, visited=False):
        '''
        Just wanted to show kids what it looks like
        '''
        cls = lambda: print(chr(27) + "[2J")
        self.print_visited = visited

        cls()
        print('Watch this')
        sleep(1)

        cls()
        print(self)
        while self.next():
            cls()
            print(self)
            sleep(0.5)

    def __str__(self):
        out = [l.copy() for l in self.m]
        if self.print_visited:
            for t in self.visited:
                x, y = t
                out[y][x] = 'X'
        out[self.g.y][self.g.x] = self.g.__str__() 
        return  '\n'.join([''.join(line) for line in out])


def parse_input(lst) -> (Lab):
    g, m = None, None
    for y, l in enumerate(lst):
        if D_U in l:
            x = l.index('^')
            g = Guard(x, y, D_U)
            lst[y][x] = '.'
    m = Map(lst)
    return Lab(m, g)
                 

if __name__ == '__main__':
    lines = Input('input_test.txt').lines_as_lists()
    #lines = Input('input.txt').lines_as_lists()

    lab = parse_input(lines)

    #lab.animate(True)
    lab.animate()
    lab.reset()

    #part 1
    print('part 1:', lab.solve_part1())

    #part 2
    print('part 2:', '')

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

    def copy(self):
        return Guard(self.x, self.y, self.d)
        
    def __str__(self):
        return self.d


class Map(list):
    def __init__(self, l: list):
        super().__init__(l)

    def has_obstacle(self, x, y: int) -> bool:
        return self[y][x] == '#'

    def out_of_bounds(self, x, y):
        return (x < 0 or y < 0) or (x >= len(self[0]) or y >= len(self))

    def copy(self):
        return Map([l.copy() for l in self])


class Lab(object):
    def __init__(self, m: Map, g: Guard):
        self.m = m.copy()
        self.g = g.copy()
        self.visited = set()
        self.cycles = set()
        self.g_init = g
        self.m_init = m
        self.print_visited = False

    def next(self) -> (bool, bool):
        self.visited.add(self.g.curr())

        x, y = self.g.want()
        if self.m.out_of_bounds(x, y):
            return False, False

        elif self.m.has_obstacle(x, y):
            _x, _y = self.g.curr()
            t = (self.g.d, _x, _y)
            if t in self.cycles:
                # approached same obstacle
                # from same direction
                return False, True
            
            self.cycles.add(t)
            self.g.turn()
            return True, False

        self.g.next()
        return True, False

    def _reset(self):
        self.visited = set()
        self.cycles = set()
        self.g = self.g_init.copy()
        self.m = self.m_init.copy()
        

    def solve_part1(self) -> int:
        self._reset()
        while True:
            ok, _ = self.next()
            if not ok:
                break
        return len(self.visited)

    def solve_part2(self) -> int:
        self.solve_part1() # just filling visited 
        visited = self.visited.copy()
        cycle_count = 0
        for t in visited:
            if self._try_cycle(t):
                cycle_count += 1
        return cycle_count

    def _try_cycle(self, t: tuple[int]) -> bool:
        self._reset()
        x, y = t
        self.m[y][x] = '#'
        while True:
            ok, cycled = self.next()
            if cycled:
                return True
            if not ok:
                return False

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
            print(self.cycles)
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
    #lines = Input('input_test.txt').lines_as_lists()
    lines = Input('input.txt').lines_as_lists()

    lab = parse_input(lines)

    #lab.animate(True)
    #lab.animate()

    #part 1
    print('part 1:', lab.solve_part1())

    #part 2
    print('part 2:', lab.solve_part2())

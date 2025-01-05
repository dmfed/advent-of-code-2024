import sys
sys.path.append('../aoclib')

from aoclib import Input
import heapq
sys.setrecursionlimit(15000)

L = '<'
U = '^'
R = '>'
D = 'v'

EMPTY = '.'
WALL = '#'
START = 'S'
END = 'E'


class Maze:
    def __init__(self, lines: list[list[str]]):
        self.grid = lines
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == START:
                    self.s = (x, y)
                elif self.grid[y][x] == END:
                    self.e = (x, y)

    def __str__(self):
        grid = [r.copy() for r in self.grid]
        return '\n'.join(''.join(row) for row in grid)

    def start(self) -> tuple[int, int]:
        return self.s

    def end(self, pos: tuple[int, int]) -> bool:
        return self.e == pos

    def is_wall(self, pos) -> bool:
        x, y = pos
        return self.grid[y][x] == WALL


def search(m: Maze) -> int:
    x, y = m.start()
    state = (x, y, 1, 0)

    queue = []
    visited = set()
    heapq.heappush(queue, (0, state))
    visited.add(state)

    while queue:
        cost, state = heapq.heappop(queue)
        x, y, xd, yd = state

        if m.end((x, y)):
            return cost

        options = [
            # move forward
            (cost+1, (x+xd, y+yd, xd, yd)),
            # turn
            (cost+1000, (x, y, -yd, xd)),
            (cost+1000, (x, y, yd, -xd)),
        ]

        for opt in options:
            cost, state = opt
            x, y, _, _ = state
            if m.is_wall((x, y)):
                continue
            if state in visited:
                continue
            
            visited.add(state)
            heapq.heappush(queue, (cost, state))
    return -1
       
def solve1(lines: list[list[str]]):
    m = Maze(lines)
    res = search(m)
    return res


def solve2(lines: list[list[str]]):
    maze = Maze(lines)
    return ''


if __name__ == '__main__':
    lines = Input('input_test.txt').lines_as_lists()
    #part 1
    print('test part 1:', solve1(lines))
    #part 2
    print('test part 2:', solve2(lines))

    lines = Input('input_test2.txt').lines_as_lists()
    #part 1
    print('test 2 part 1:', solve1(lines))
    #part 2
    print('test 2 part 2:', solve2(lines))

    lines = Input('input.txt').lines_as_lists()
    #part 1
    print('part 1:', solve1(lines)) # 90460

    #part 2
    print('part 2:', solve2(lines))

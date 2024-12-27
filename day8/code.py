import sys
sys.path.append('../aoclib')

from aoclib import Input
import sys

sys.setrecursionlimit(10**6)

def find_pairs(field):
    pairs = set()
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == '.':
                continue
            for y2 in range(y, len(field)):
                for x2 in range(len(field[0])):
                    if x == x2 and y == y2:
                        continue
                    if field[y][x] == field[y2][x2]:
                        # this is a pair
                        pairs.add(((x, y), (x2, y2)))
    return pairs

def find_antinodes(pair: tuple[tuple[int]], field):
    p1, p2 = pair
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]

    one, two = (p1[0] - x_diff, p1[1] - y_diff), (p2[0] + x_diff, p2[1] + y_diff)

    nodes = []
    if out_of_bounds(one, field):
        one = None
    if out_of_bounds(two, field):
        two = None
        
    return one, two

            
def out_of_bounds(c, field):
    return c[0] < 0 or c[1] < 0 or c[0] >= len(field[0]) or c[1] >= len(field)


def solve1(field: list):
    pairs = find_pairs(field)
    antinodes = set()
    for p in pairs:
        one, two = find_antinodes(p, field)
        if one:
            antinodes.add(one)
        if two:
            antinodes.add(two)

    return len(antinodes)


def solve2(field: list):
    pairs = find_pairs(field)
    antinodes = set()
    for p in pairs:
        p1, p2 = p
        antinodes.add(p1)
        antinodes.add(p2)
        
        one, two = find_antinodes(p, field)
        run = True
        while run:
            _one, _two = None, None
            if one:
                antinodes.add(one)
                _one, _ = find_antinodes((one, p1), field)
            if two:
                antinodes.add(two)
                _, _two = find_antinodes((p2, two), field)

            if not _one and not _two:
                run = False
                continue

            if _one:
                p1 = one
                one = _one
                
            if _two:
                p2 = two
                two = _two                

    return len(antinodes)


if __name__ == '__main__':
    #field = Input('input_test2.txt').lines_as_lists()
    field = Input('input.txt').lines_as_lists()

    # print(find_pairs(field))

    #part 1
    print('part 1:', solve1(field))

    #part 2
    print('part 2:', solve2(field))

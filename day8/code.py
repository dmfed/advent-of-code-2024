import sys
sys.path.append('../aoclib')

from aoclib import Input

def find_pairs(field):
    '''suboptimal (shitty) code'''
    pairs = set()
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == '.':
                continue
            for y2 in range(len(field)):
                for x2 in range(len(field[0])):
                    if x == x2 and y == y2:
                        continue
                    if field[y][x] == field[y2][x2]:
                        # this is a pair
                        pairs.add((x, y, x2, y2))
    return pairs

def find_antinodes(pair, field):
    x, y, x2, y2 = pair
    x_diff = abs(x - x2)
    y_diff = abs(y - y2)

    one, two = None, None
    if x2 >= x and y2 >= y:
        one = (y-y_diff, x-x_diff)
        two = (y2+y_diff, x2+x_diff)
    elif x2 >= x and y2 < y:
        one = (y+y_diff, x-x_diff)
        two = (y2-y_diff, x2+x_diff)

    antinodes = []
    if one and not out_of_bounds(one, field):
        antinodes.append(one)
    if two and not out_of_bounds(two, field):
        antinodes.append(two)

    return antinodes

def out_of_bounds(c, field):
    return c[0] < 0 or c[1] < 0 or c[0] >= len(field[0]) or c[1] >= len(field)

def solve1(field: list):
    pairs = find_pairs(field)
    print(pairs)
    antinodes = set()
    for p in pairs:
        for anode in find_antinodes(p, field):
            antinodes.add(anode)
    return len(antinodes)


if __name__ == '__main__':
    #field = Input('input_test.txt').lines_as_lists()
    field = Input('input.txt').lines_as_lists()

    #part 1
    print('part 1:', solve1(field))

    #part 2
    print('part 2:', '')

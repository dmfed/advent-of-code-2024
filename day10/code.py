import sys
sys.path.append('../aoclib')

from aoclib import Input

def find_starting_points(field) -> list[tuple[int, int]]:
    points = []
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == 0:
                points.append((x, y))
    return points


def num_trails(point: tuple[int, int], curr: int, field: list[list[int]]) -> list[tuple[int, int]]:
    if out_of_bounds(point, field):
        return [None]
    
    x, y = point
    if field[y][x] != curr:
        # impossible path
        return [None]

    if curr == 9 and field[y][x] == curr:
        # goal
        return [point]

    curr += 1

    opts = list()

    opts.extend(num_trails((x+1, y), curr, field))
    opts.extend(num_trails((x-1, y), curr, field))
    opts.extend(num_trails((x, y+1), curr, field))
    opts.extend(num_trails((x, y-1), curr, field))
    
    return opts


def out_of_bounds(point: tuple[int, int], field: list[list[int]]) -> bool:
    x, y = point
    return y < 0 or y >= len(field) or x < 0 or x >= len(field[0])


def solve1(field: list[list[int]]) -> int:
    starts = find_starting_points(field)
    count = 0
    for p in starts:
        trails = num_trails(p, 0, field)
        count += sum([1 if n else 0 for n in set(trails)])
    return count

def solve2(field: list[list[int]]) -> int:
    starts = find_starting_points(field)
    count = 0
    for p in starts:
        trails = num_trails(p, 0, field)
        count += sum([1 if n else 0 for n in trails])
    return count

if __name__ == '__main__':
    #field = Input('input_test.txt').lines_split_as_ints()
    field = Input('input.txt').lines_split_as_ints()

    #part 1
    print('part 1:', solve1(field)) # 733

    #part 2
    print('part 2:', solve2(field)) # 1514

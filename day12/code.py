import sys
sys.path.append('../aoclib')

from aoclib import Input
from collections import defaultdict

def find_regions(grid: list[list[str]]):
    regions = []
    all_visited = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in all_visited:
                continue

            val = grid[y][x]
            region = set()
            search(val, (x, y), grid, region)

            regions.append((val, region))

            all_visited.update(region)

    return regions

        
def search(plot_type: str, plot: tuple[int,int], grid: list[list[str]], region: set):
    x, y = plot
    if out_ouf_bounds(plot, grid) or plot in region or not grid[y][x] == plot_type:
        return

    region.add(plot)
    search(plot_type, (x+1, y), grid, region)
    search(plot_type, (x-1, y), grid, region)
    search(plot_type, (x, y+1), grid, region)
    search(plot_type, (x, y-1), grid, region)

    return


def out_ouf_bounds(plot, grid) -> bool:
    x, y = plot
    return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)

def region_area_and_perimeter(plots: set[tuple[int, int]]) -> tuple[int, int]:
    a = len(plots)
    p = 0
    for plot in plots:
        x, y = plot
        if (x+1, y) not in plots:
            p += 1
        if (x-1, y) not in plots:
            p += 1
        if (x, y+1) not in plots:
            p += 1
        if (x, y-1) not in plots:
            p += 1
    return a, p


def region_num_sides(plots: set[tuple[int,int]]) -> int:
    n = 0 
    
    for p in plots:
        # outer corners
        x, y = p
        if (x, y-1) not in plots and (x+1, y) not in plots:
            n += 1
        if (x+1, y) not in plots and (x, y+1) not in plots:
            n += 1
        if (x, y+1) not in plots and (x-1, y) not in plots:
            n += 1
        if (x-1, y) not in plots and (x, y-1) not in plots:
            n += 1

    for p in plots:
        # inner corners
        x, y = p
        if (x, y-1) in plots and (x+1, y) in plots and (x+1, y-1) not in plots:
            n += 1
        if (x+1, y) in plots and (x, y+1) in plots and (x+1, y+1) not in plots:
            n += 1
        if (x, y+1) in plots and (x-1, y) in plots and (x-1, y+1) not in plots:
            n += 1
        if (x-1, y) in plots and (x, y-1) in plots and (x-1, y-1) not in plots:
            n += 1
            
    return n

def find_sides(c: tuple[int, int], plots: set[tuple[int, int]]):
    x, y = c
    hor = set()
    vert = set()

    _x, _y = x, y
    while (_x, _y) in plots:
        low = (x, y-1)
        high = (x, y+1)
        vert.add((x,y))
        while low and high:
            if low in plots:
                vert.add(low)
            else:
                low = None
            if high in plots:
                vert.add(high)
            else:
                high = None
    return vert, hor

def solve1(grid: list[list[str]]):
    regions = find_regions(grid)
    total = 0
    for r in regions:
        a, p = region_area_and_perimeter(r[1])
        total += a * p
    return total


def solve2(grid: list[list[str]]):
    regions = find_regions(grid)
    total = 0
    for r in regions:
        a, _ = region_area_and_perimeter(r[1])
        n = region_num_sides(r[1])
        total += a * n

    return total


if __name__ == '__main__':
    #grid = Input('input_test.txt').lines_as_lists()
    grid = Input('input.txt').lines_as_lists()

    #part 1
    print('part 1:', solve1(grid)) # 1402544

    #part 2
    print('part 2:', solve2(grid)) # 862486

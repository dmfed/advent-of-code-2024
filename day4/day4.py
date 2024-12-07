import sys
sys.path.append('../aoclib')

from aoclib import Input

# directions
D_R = 'r'
D_L = 'l'
D_U = 'u'
D_D = 'd'
D_UR = 'ur'
D_DR = 'dr'
D_UL = 'ul'
D_DL = 'dl' 
D_LIST = [D_R, D_L, D_U, D_D, D_UR, D_DR, D_UL, D_DL]

def search(word: str, depth: int, x, y: int, dir: str, field: list[list[str]]) -> bool:
    if depth == len(word)-1 and field[y][x] == word[depth]:
        return True
    elif field[y][x] != word[depth] or depth == len(word)-1:
        return False

    if dir == D_R:
        x += 1
    elif dir == D_L:
        x -= 1
    elif dir == D_U:
        y -= 1
    elif dir == D_D:
        y += 1
    elif dir == D_UR:
        y -= 1
        x += 1
    elif dir == D_DR:
        y += 1
        x += 1
    elif dir == D_UL:
        y -= 1
        x -= 1
    elif dir == D_DL:
        y += 1
        x -= 1
    if y >= len(field) or x >= len(field[0]) or y < 0 or x < 0:
        # out of bounds
        return False 

    return search(word, depth+1, x, y, dir, field)


def solve1(word, field) -> int:
    count = 0
    for y in range(len(field)):
        for x in range(len(field[0])):
            for dir in D_LIST:
                found = search(word, 0, x, y, dir, field)
                if found:
                    count +=1
    return count


if __name__ == '__main__':
    #field = Input('input_test.txt').lines_as_lists()
    field = Input('input.txt').lines_as_lists()

    #part 1
    print('part 1:', solve1('XMAS', field))

    #part 2
    #print('part 2:', solve2(raw))

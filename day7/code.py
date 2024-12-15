import sys
sys.path.append('../aoclib')

from aoclib import Input

def parse_input(lines: list):
    equations = list()
    for l in lines:
        s = l.split(':')
        eq = (int(s[0]), [int(x.strip()) for x in s[1].split()])
        equations.append(eq)    
    return equations

def solve1(eqs):
    return sum([e[0] if may_be_true(e[0], e[1]) else 0 for e in eqs]) 

def may_be_true(val: int, lst: list[int]) -> bool:
    if len(lst) == 1:
        return lst[0] == val

    if may_be_true(val, [lst[0]+lst[1], *lst[2:]]):
        return True
    elif may_be_true(val, [lst[0] * lst[1], *lst[2:]]):
        return True

    return False
        
if __name__ == '__main__':
    lines = Input('input_test.txt').lines()
    #lines = Input('input.txt').lines()

    eq = parse_input(lines)

    #part 1
    print('part 1:', solve1(eq))

    #part 2
    print('part 2:', '')

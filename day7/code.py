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

def _sum2(l: list[int]) -> list[int]:
    return [l[0] + l[1], *l[2:]]

def _mul2(l: list[int]) -> list[int]:
    return [l[0] * l[1], *l[2:]]

def _concat2(l: list[int]) -> list[int]:
    return [int(str(l[0]) + str(l[1])), *l[2:]]

def may_be_true(val: int, lst: list[int], funcs) -> bool:
    if len(lst) == 1:
        return lst[0] == val
    return any([may_be_true(val, f(lst), funcs) for f in funcs])

def solve1(eqs):
    funcs = [_sum2, _mul2]
    return sum([e[0] if may_be_true(e[0], e[1], funcs) else 0 for e in eqs]) 

def solve2(eqs):
    funcs = [_sum2, _mul2, _concat2]
    return sum([e[0] if may_be_true(e[0], e[1], funcs) else 0 for e in eqs]) 
    

if __name__ == '__main__':
    #lines = Input('input_test.txt').lines()
    lines = Input('input.txt').lines()

    eq = parse_input(lines)

    #part 1
    print('part 1:', solve1(eq))

    #part 2
    print('part 2:', solve2(eq))

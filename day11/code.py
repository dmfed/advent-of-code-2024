import sys
sys.path.append('../aoclib')

from aoclib import Input

def apply_rules(stones: dict[int, int]) -> dict[int, int]:
    new_stones = dict()
    for k in stones.keys():
        new_value = _apply_rules(k)
        for item in new_value:
            if item not in new_stones:
                new_stones[item] = 0
            new_stones[item] += stones[k]
    return new_stones

def _apply_rules(s: int) -> list[int]:
    res = list()
    if s == 0:
        res.append(1)
    elif  len(str(s))%2==0:
        _s = str(s)
        res.extend([int(_s[:len(_s)//2]), int(_s[len(_s)//2:])])
    else:
        res.append(s*2024)
    return res    


def solve(iter: int, stones: list[int]) -> int:
    s = dict(zip(stones, [1 for _ in range(len(stones))])) 
    for st in stones:
        s[st] = 1
    for i in range(iter):
        s = apply_rules(s)
    return sum(s.values())

if __name__ == '__main__':
    #stones = Input('input_test.txt').lines_as_int_lists()
    stones = Input('input.txt').lines_as_int_lists()

    #part 1
    print('part 1:', solve(25, stones[0])) # 216996

    #part 2
    print('part 2:', solve(75, stones[0])) # 257335372288947

import sys
sys.path.append('../aoclib')

from aoclib import Input
from collections import defaultdict

def parse_input(data: list[str]):
    rules = defaultdict(set)
    updates = []
    for line in data:
        if '|' in line:
            l, r = (int(n) for n in line.split('|'))
            rules[l].add(r)
            continue
        if line == '':
            continue
        l = [int(n) for n in line.split(',')]
        updates.append(l)

    return rules, updates

def update_is_correct(rules, upd):
    for i, x in enumerate(upd):
        for j, y in enumerate(upd):
            if i > j and y in rules[x]:
                return False
    return True

def fix_update(rules, upd):
    for i, x in enumerate(upd):
        for j, y in enumerate(upd):
            if i > j and y in rules[x]:
                upd[i], upd[j] = upd[j], upd[i]
    return upd

def solve1(rules, updates):
    count = 0
    for upd in updates:
        if update_is_correct(rules, upd):
            count += upd[len(upd) // 2]
    return count


def solve2(rules, updates):
    count = 0

    for upd in updates:
        if not update_is_correct(rules, upd):
            upd = fix_update(rules, upd)
            count += upd[len(upd) // 2]

    return count

        

if __name__ == '__main__':
    #lines = Input('input_test.txt').lines()
    lines = Input('input.txt').lines()
    rules, updates = parse_input(lines)

    #part 1
    print('part 1:', solve1(rules, updates))

    #part 2
    print('part 2:', solve2(rules, updates))

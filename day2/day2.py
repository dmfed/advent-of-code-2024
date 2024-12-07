import sys
sys.path.append('../aoclib')

from aoclib import Input

def is_safe_pair(a: int, b: int, min_diff=1, max_diff=3, inc=True):
    if b > a and not inc:
        return False
    if b < a and inc:
        return False

    diff = abs(a-b)
    return diff >= min_diff and diff <= max_diff

def is_safe_report(l: list, violations=0) -> bool:
    increasing = l[1] > l[0]
    found_violations = 0

    for i in range(len(l)-1):
        if not is_safe_pair(l[i], l[i+1], inc=increasing):
            found_violations += 1
      
    return found_violations <= violations
    
    
if __name__ == '__main__':
    #reports = Input('input_test.txt').lines_as_int_lists()
    reports = Input('input.txt').lines_as_int_lists()

    #part 1
    print('part 1:', sum([is_safe_report(r) for r in reports]))

    #part 2
    print('part 1:', sum([is_safe_report(r, violations=1) for r in reports]))

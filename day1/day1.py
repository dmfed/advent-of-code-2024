import sys
sys.path.append('../aoclib')

from aoclib import Input

if __name__ == '__main__':
    #lines = Input('input_test.txt').lines()
    lines = Input('input.txt').lines()

    left = sorted([int(n.split()[0].strip()) for n in lines])
    right = sorted([int(n.split()[1].strip()) for n in lines])

    # part 1
    s = sum([abs(left[i] - right[i]) for i in range(len(left))])

    print('part 1:', s)

    # part 2
    s2 = sum([n * right.count(n) for n in left])

    print('part 2:', s2)

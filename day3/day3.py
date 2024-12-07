import sys
sys.path.append('../aoclib')

from aoclib import Input
import re

def all_mul(s: list[str]) -> int:
    total = 0
    matches = re.findall(r'mul\((\d+),(\d+)\)', s)
    for m in matches:
        total += int(m[0]) * int(m[1])

    return total
    
class Tokenizer(object):
    regexp = re.compile(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))")
    def __init__(self, s: str):
        self._string = s
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        m = self.regexp.search(self._string)
        if not m:
            raise StopIteration

        self.count += 1

        self._string = self._string[m.end():]

        a, b = 0, 0

        if m.group(1).startswith('mul'):
            a = int(m.group(2))
            b = int(m.group(3))

        t = Token(m.group(1), a, b)
        return t


class Token(object):
    _do = "do()"
    _dont = "don't()"
    def __init__(self, s: str, a: int, b: int):
        self._value = s
        self.a = a
        self.b = b

    def do(self) -> bool:
        return self._value == self._do

    def dont(self) -> bool:
        return self._value == self._dont

    def mult(self) -> int:
        return self.a * self.b

    def __str__(self) -> str:
        return f'{self._value}, {self.a}, {self.b}'
     
def solve2(s: str) -> int:
    active = True
    total = 0
    tokens = Tokenizer(s)
    for t in tokens:
        if t.do():
            active = True
            continue
        elif t.dont():
            active = False
            continue

        if active:
            total += t.mult()

    return total


if __name__ == '__main__':
    #lines = Input('input_test2.txt').lines()
    raw = Input('input.txt').raw()

    #part 1
    print('part 1:', all_mul(raw))

    #part 2
    print('part 2:', solve2(raw))

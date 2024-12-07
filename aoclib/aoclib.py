class Input(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._raw = f.read()

    def raw(self):
        return self._raw

    def lines(self):
        return [l.strip() for l in self._raw.strip().split('\n')]

    def lines_as_int_lists(self):
        return [[int(n) for n in l.split()] for l in self.lines()]

    def lines_as_lists(self):
        return [list(l) for l in self.lines()]


class Input(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._lines = list(l.strip() for l in f.readlines())

    def lines(self):
        return self._lines

    def lines_as_int_lists(self):
        return [[int(n) for n in l.split()] for l in self._lines]


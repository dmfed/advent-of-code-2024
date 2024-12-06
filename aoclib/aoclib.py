class Input(object):
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self._lines = list(l.strip() for l in f.readlines())

    def lines(self):
        return self._lines


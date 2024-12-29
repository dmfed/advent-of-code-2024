import sys
sys.path.append('../aoclib')

from aoclib import Input

class FS(object):
    def __init__(self, s: str):
        self._initial = s
        counter = 0
        self.blocks = []
        for i in range(0, len(s), 2):
            file_len = int(s[i])
            self.blocks.extend([counter for _ in range(file_len)])

            if i+1 >= len(s):
                break

            space_len = int(s[i+1])
            self.blocks.extend(['.' for _ in range(space_len)])
            counter += 1
        self.free = 0

    def __str__(self):
        return ''.join([str(n) for n in self.blocks])

    def reset(self):
        self.__init__(self._initial)

    def defragment(self):
        for i in range(len(self.blocks)-1, -1, -1):
            if self.blocks[i] == '.':
                continue
            next = self._next_free()
            if not next or next >= i:
                break
            # swap
            self.blocks[next], self.blocks[i] = self.blocks[i], self.blocks[next]

    def smart_defragment(self):
        files = self._get_files()
        for file in files:
            for span in self._get_spans():
                file_len = file[2] - file[1]
                span_len = span[1] - span[0]
                if (span[1] - 1) >= file[1]:
                    break                    
                if file_len <= span_len:
                    self.blocks[span[0]:span[0]+file_len] = [file[0] for _ in range(file_len)]
                    self.blocks[file[1]:file[2]] = ['.' for _ in range(file_len)]
                    break

    def solve1(self):
        self.reset()
        self.defragment()
        return sum([x[0] * int(x[1]) if x[1] != '.' else 0 for x in enumerate(self.blocks)])

    def solve2(self):
        self.reset()
        self.smart_defragment()
        return sum([x[0] * int(x[1]) if x[1] != '.' else 0 for x in enumerate(self.blocks)])
        
                

    def _next_free(self, start=0) -> int:
        try:
            i = self.blocks.index('.', start)
            return i
        except Exception:
            return None

    def _get_files(self):
        files = []

        end, start = 0, 0

        i = len(self.blocks)-1
        while i > 0:
            if self.blocks[i] == '.':
                i -= 1
                continue
            end = i+1
            start = i
            for j in range(i, -1, -1):
                if self.blocks[j] != self.blocks[i]:
                    break
                start = j
            files.append((self.blocks[i], start, end))
            i = start-1

        return files
             
    def _get_spans(self):
        spans = []
        start = self._next_free()
        while start:
            end = start
            for i in range(start+1, len(self.blocks)):
                if self.blocks[i] != '.':
                    break
                end = i
            spans.append((start, end+1))
            start = self._next_free(end+1)
            
        return spans
        
            
        
            


if __name__ == '__main__':
    #s = Input('input_test.txt').raw()
    s = Input('input.txt').raw()

    fs = FS(s)

    #part 1
    #print('part 1:', fs.solve1())

    #part 2
    print('part 2:', fs.solve2())

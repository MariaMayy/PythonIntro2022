class Pushpull:
    pos = [0]
    def __init__(self, spos = 0):
        self.pos[0] = spos
        
    def __iter__(self):
        if (self.pos[0] > 0):
            return iter(range(self.pos[0]))
        else:
            return iter(range(0, self.pos[0], -1))

    def push(self, cur = 1):
        self.pos[0] += cur

    def pull(self, cur = 1):
        self.pos[0] -= cur

    def __str__(self):
        if (self.pos[0] < 0):
            return f'<{-self.pos[0]}<'
        elif (self.pos[0] > 0):
            return f'>{self.pos[0]}>'
        return f'<{self.pos[0]}>'
        

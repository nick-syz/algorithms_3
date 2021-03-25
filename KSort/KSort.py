# https://skillsmart.ru/algo/15-121-cm/i58fbc20d6.html

class ksort:

    def __init__(self):
        self.items = [None] * 1000
    
    def check(self, s):
        if len(s) == 3 and s[0] in 'abcdefgh' and \
                s[1].isnumeric() and s[2].isnumeric():
            return True
        return False

    def index(self, s):
        if self.check(s):
            return (ord(s[0])-97)*37 + int(s[1])*7 + int(s[2])
        return -1

    def add(self, s):
        if self.check(s):
            i = self.index(s)
            while i >= len(self.items):
                self.items.append(None)
            self.items[i] = s
            return True
        return False

# https://skillsmart.ru/algo/15-121-cm/fe994e3320.html

class BinarySearch:

    def __init__(self, array):
        self.Array = array
        self.Left = 0
        self.Right = len(array)-1
        self.Status = 0

    def Step(self, N):
        middle = (self.Left+self.Right+1)//2
        if N == self.Array[middle]:
            self.Status = 1    
            return
        if N > self.Array[middle]:
            self.Left = middle + 1
        else:
            self.Right = middle - 1
        if self.Left > self.Right:
            self.Status = -1
            return
        if self.Right-self.Left <= 1:
            if N in (self.Array[self.Left], self.Array[self.Right]):
                self.Status = 1
                return
            self.Status = -1

    def GetResult(self):
        return self.Status

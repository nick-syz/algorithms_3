# https://skillsmart.ru/algo/15-121-cm/fe994e3320.html

class BinarySearch:

    def __init__(self, array):
        self.Array = array
        self.Left = 0
        self.Right = len(array)-1
        self.Status = None

    def Step(self, N):
        middle = self.Array[(self.Left+self.Right+1)//2]
        if N == middle:
            self.Status = 1    
        else:
            if N > middle:
                self.Left = (self.Left+self.Right)//2 + 1
            else:
                self.Right = (self.Left+self.Right)//2 - 1
            if N in (self.Array[self.Right], self.Array[self.Left]):
                self.Status = 1
            elif self.Left == self.Right:
                self.Status = -1
            else:
                self.Status = 0

    def GetResult(self):
        return self.Status

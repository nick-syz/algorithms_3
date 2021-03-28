# https://skillsmart.ru/algo/15-121-cm/fe994e3320.html
# https://skillsmart.ru/algo/15-121-cm/u518d18776.html

class BinarySearch:

    def __init__(self, array):
        self.Array = array
        self.Left = 0
        self.Right = len(array)-1
        self.Status = 0
    
    def Step(self, N):
        if self.Status == 0:
            middle = (self.Left+self.Right) // 2
            if self.Left > self.Right:
                self.Status = -1
                return
            if N == self.Array[middle]:
                self.Status = 1
            elif N > self.Array[middle]:
                self.Left = middle + 1
            else:
                self.Right = middle - 1
            if self.Left > self.Right:
                self.Status = -1
            elif self.Right-self.Left <= 1:
                if N in (self.Array[self.Left], self.Array[self.Right]):
                    self.Status = 1
                    return
                self.Status = -1
    
    def GetResult(self):
        return self.Status

def GallopingSearch(arr, N, i=1):
    j = 2**i-2
    if j < len(arr)-1:
        if arr[j] == N:
            return True
        if arr[j] < N:
            return GallopingSearch(arr, N, i+1)
    else:
        j = len(arr)-1
    search = BinarySearch(arr)
    search.Left = 2**(i-1)-1
    search.Right = j
    while search.Status == 0:
        search.Step(N)
    if search.Status == -1:
        return False
    else:
        return True

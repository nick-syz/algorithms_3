# https://skillsmart.ru/algo/15-121-cm/e858048f95.html

def QuickSort(array, left, right):
    if left < right:
        l = left
        r = right 
        N = len(array[l:r+1]) // 2 + l
        while True:
            if array[l] < array[N]:
                l += 1
            if array[r] > array[N]:
                r -= 1
            if l == r-1 and array[l] > array[r]:
                array[l], array[r] = array[r], array[l]
                return QuickSort(array, left, right)
            if l == r or (l == r-1 and array[l] < array[r]):
                break
            if array[l] >= array[N] and array[r] <= array[N]:
                array[l], array[r] = array[r], array[l]
                if l == N:
                    N = r
                elif r == N:
                    N = l
        if N-1 >= 0:
            QuickSort(array, left, N-1)
        if N+1 < len(array):
            QuickSort(array, N+1, right)

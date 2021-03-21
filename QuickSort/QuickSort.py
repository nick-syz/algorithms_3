# https://skillsmart.ru/algo/15-121-cm/e858048f95.html

def QuickSort(array, left, right):
    if left < right and left >= 0 and right < len(array):
        i = left
        j = right 
        N = len(array[i:j+1])//2 + i
        while True:
            if array[i] < array[N]:
                i += 1
            if array[j] > array[N]:
                j -= 1
            if i == j-1 and array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                return QuickSort(array, left, right)
            if i == j or (i == j-1 and array[i] < array[j]):
                break
            if array[i] >= array[N] and array[j] <= array[N]:
                array[i], array[j] = array[j], array[i]
                if i == N:
                    N = j
                elif j == N:
                    N = i
        QuickSort(array, left, N-1)
        QuickSort(array, N+1, right)

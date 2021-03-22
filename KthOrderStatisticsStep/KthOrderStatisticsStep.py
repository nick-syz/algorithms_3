# https://skillsmart.ru/algo/15-121-cm/e63d022184.html

def ArrayChunk(array, left, right):
    i = left
    j = right
    N = (i + j) // 2
    while True:
        if array[i] < array[N]:
            i += 1
        if array[j] > array[N]:
            j -= 1
        if i == j-1 and array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
            return ArrayChunk(array, left, right)
        if i == j or (i == j-1 and array[i] < array[j]):
            return N
        if array[i] >= array[N] and array[j] <= array[N]:
            array[i], array[j] = array[j], array[i]
            if i == N:
                N = j
            elif j == N:
                N = i

def KthOrderStatisticsStep(Array, L, R, k):
    N = ArrayChunk(Array, L, R)
    if N != k:
        if N < k:
            return KthOrderStatisticsStep(Array, N+1, R, k)
        else:
            return KthOrderStatisticsStep(Array, L, N-1, k)
    return [L, R]

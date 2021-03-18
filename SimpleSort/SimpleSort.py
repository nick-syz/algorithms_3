# https://skillsmart.ru/algo/15-121-cm/a94814c2b9.html

def SelectionSortStep(array, i):
    j = i
    for k in range(i, len(array)):
        if array[k] < array[j]:
            j = k
    array[j], array[i] = array[i], array[j]

def BubbleSortStep(array):
    changed = False
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            changes = True
    return changed

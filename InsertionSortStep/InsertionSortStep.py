# https://skillsmart.ru/algo/15-121-cm/a94814c2b9.html

def InsertionSortStep(array, step, i):
    j = i
    for k in range(i, len(array), step):
        if array[k] < array[j]:
            j = k
    array[i], array[j] = array[j], array[i]

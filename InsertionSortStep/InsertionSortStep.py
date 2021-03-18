# https://skillsmart.ru/algo/15-121-cm/a94814c2b9.html

def InsertionSortStep(array, step, i):
    for j in range(i, len(array), step):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

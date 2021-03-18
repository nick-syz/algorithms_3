# https://skillsmart.ru/algo/15-121-cm/a94814c2b9.html

def InsertionSortStep(array, step, i):
    for s in range(i+step, len(array), step):
        for j in range(s, i+step-1, -step):
            if array[j] < array[j-step]:
                array[j], array[j-step] = array[j-step], array[j]

# https://skillsmart.ru/algo/15-121-cm/a3d84b8cab.html

def InsertionSortStep(array, step, i):
    for s in range(i+step, len(array), step):
        for j in range(s, i+step-1, -step):
            if array[j] < array[j-step]:
                array[j], array[j-step] = array[j-step], array[j]

def KnuthSequence(array_size, k_seq=[], i=1):
    if array_size >= i:
        KnuthSequence(array_size, k_seq, 3*i+1)
        k_seq.append(i)
    return k_seq

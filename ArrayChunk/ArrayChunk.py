# https://skillsmart.ru/algo/15-121-cm/r71p8f1a17.html

def ArrayChunk(array):
    middle_index = len(array)//2
    start_index = 0
    end_index = len(array)-1
    while True:
        if array[start_index] < array[middle_index]:
            start_index += 1
        if array[end_index] > array[middle_index]:
            end_index -= 1
        if start_index == end_index-1 and array[start_index] > array[end_index]:
            array[start_index], array[end_index] = array[end_index], array[start_index]
            return ArrayChunk(array)
        if start_index == end_index or (start_index == end_index-1 and array[start_index] < array[end_index]):
            return middle_index
        if array[start_index] >= array[middle_index] and array[end_index] <= array[middle_index]:
            array[start_index], array[end_index] = array[end_index], array[start_index]
            if start_index == middle_index:
                middle_index = end_index
            elif end_index == middle_index:
                middle_index = start_index

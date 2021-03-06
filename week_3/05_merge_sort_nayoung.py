# https://nazero.tistory.com/81
# 병합정렬

array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array) <= 1:
        return array
    array_len_half = len(array) // 2
    merge_left = merge_sort(array[:array_len_half])
    merge_right = merge_sort(array[array_len_half:])
    return merge(merge_left, merge_right)


def merge(array1, array2):
    merge_array = []
    array1_index = 0
    array2_index = 0
    array1_len = len(array1)
    array2_len = len(array2)
    while array1_index <= array1_len - 1 and array2_index <= array2_len - 1:
        if array1[array1_index] < array2[array2_index]:
            merge_array.append(array1[array1_index])
            array1_index += 1
        else:
            merge_array.append(array2[array2_index])
            array2_index += 1
    # array2가 merge_array에 append를 모두 했음에도 불구하고 array1의 값들이 남아있는 상황
    if array1_index > array1_len - 1:
        while array2_index <= array2_len - 1:
            merge_array.append(array2[array2_index])
            array2_index += 1
    # array1가 merge_array에 append를 모두 했음에도 불구하고 array2의 값들이 남아있는 상황
    if array2_index > array2_len - 1:
        while array1_index <= array1_len - 1:
            merge_array.append(array1[array1_index])
            array1_index += 1
    return merge_array


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8]

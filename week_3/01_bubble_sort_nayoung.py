input = [4, 6, 2, 9, 1]


def bubble_sort(array):   #O(N^2)
    for i in range(len(array)-1):   # N의 길이만큼 반복
        for j in range(len(array)-1-i):   # N의 길이만큼 반복
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
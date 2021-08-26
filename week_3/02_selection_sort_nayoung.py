# https://nazero.tistory.com/78
# 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 선택 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]


def selection_sort(array):
    for current_index in range(len(array)-1):
        min_number = array[current_index+1]
        min_index = current_index+1
        for i in range(current_index+1, len(array)):
            if array[i] < min_number:
                min_number = array[i]
                min_index = i
        array[current_index], array[min_index] = array[min_index], array[current_index]

    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!
# https://nazero.tistory.com/70
# 1~16까지 오름차순으로 정렬되어있는 배열 중에서 14 찾기

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 이진탐색
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    count = 0
    while current_min <= current_max:
        current_guess = (current_min + current_max) // 2
        count += 1
        if array[current_guess] == target:
            print("시도한 횟수: ", count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
    print("시도한 횟수: ", count)
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
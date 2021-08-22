# https://nazero.tistory.com/70
# 1~16까지 오름차순으로 정렬되어있는 배열 중에서 14 찾기

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 순차탐색
def is_existing_target_number_sequential(target, array):
    find_count = 0
    for number in array:
        find_count += 1
        if target == number:
            print("시도한 횟수:", find_count)  # 14
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True

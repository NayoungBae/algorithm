# https://nazero.tistory.com/70
# 1~16까지 오름차순으로 정렬되어있는 배열 중에서 14 찾기

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# 이진탐색
def is_existing_target_number_binary(target, array):
    min_num = array[0]
    max_num = array[-1]
    try_num = 0
    count = 0
    if target > len(array):
        return "None!!"
    while target != try_num:
        try_num = (min_num + max_num) // 2
        count += 1
        if try_num < target:
            min_num = try_num + 1
        elif try_num > target:
            max_num = try_num - 1
    print("시도한 횟수: ", count)
    return try_num


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

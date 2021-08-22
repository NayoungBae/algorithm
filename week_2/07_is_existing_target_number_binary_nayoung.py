# 다음과 같이 숫자로 이루어진 배열이 있을 때, 2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    # 나름 선택정렬 생각하고 해본건데..
    for i in range(len(finding_numbers)):
        min_number = numbers[i]
        min_number_index = i
        for j in range(i + 1, len(finding_numbers)):
            if numbers[j] < min_number:
                min_number = numbers[j]
                min_number_index = j
        if numbers[i] > numbers[min_number_index]:
            temp = numbers[i]
            numbers[i] = numbers[min_number_index]
            numbers[min_number_index] = temp

    min_index = 0
    max_index = len(finding_numbers) - 1
    guess_index = (min_index + max_index) // 2
    while min_index <= max_index:
        if numbers[guess_index] == target:
            return True
        elif numbers[guess_index] < target:
            min_index = guess_index + 1
        else:
            max_index = guess_index - 1
        guess_index = (min_index + max_index) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)

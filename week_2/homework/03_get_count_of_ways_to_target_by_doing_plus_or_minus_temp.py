# https://nazero.tistory.com/75
# 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
# numbers = [1, 1, 1, 1, 1]
# target_number = 3


numbers = [2, 3, 1]
target_number = 0

result = []  # 모든 경우의 수를 담기 위한 변수


# 모든 경우의 수 구하는 함수
# Arguments
# array: 음이 아닌 정수들로 이루어진 배열
# current_index: array의 현재 위치(인덱스)
# current_cal: 현재의 합
# all_ways: 모든 경우의수(관리하기 위한 배열)/ result 배열을 전달할것임
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_cal, all_ways):
    # print("current_index: " + str(current_index) + ", current_cal: " + str(current_cal))
    if current_index == len(array):
        # print("all_ways.append(current_cal)")
        all_ways.append(current_cal)
        return
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_cal + array[current_index], all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_cal - array[current_index], all_ways)


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    return 5


print(get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result))
print(result)
# print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!

# 문제가 축소되는 과정에서는 재귀함수로 해결할 수 있다
# 헷갈리는 게 있다면 모든 경우의 수를 다 써보고 시도해보자

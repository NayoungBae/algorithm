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
numbers = [1, 1, 1, 1, 1]
target_number = 3


#############################################################################################

# 먼저 좀 더 쉬운 숫자로 생각
# numbers = [2, 3, 1]
# target_number = 0

# +2 +3 +1 = 6              +++
# +2 +3 -1 = 4              ++-
# +2 -3 +1 = 0    #타겟!     +-+
# +2 -3 -1 = -2             +--
# -2 +3 +1 = 2              -++
# -2 +3 -1 = 0    #타겟!     -+-
# -2 -3 +1 = -4             --+
# -2 -3 -1 = -6             ---

# 반복되는 구조를 축소할 수 있는 방법은
# 앞의 두 개의 연산자는 고정시키고
# 뒤의 연산자를 + 또는 -으로 바꾸면
# 2가지의 경우의 수가 추가적으로 생긴다

# 마지막의 원소를 뺄지/더할지에 따라 2가지 방법이 추가된다

# 결론) N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N -1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 된다

result_count = 0


# Arguments
# array: 음이 아닌 정수들로 이루어진 배열
# target: 만드려고 하는 수
# current_index: array의 현재 위치(인덱스)
# current_cal: 현재의 합
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_cal):
    if current_index == len(array):
        if current_cal == target:
            global result_count     # global: 내부에서 외부 변수를 쓰겠다
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_cal + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_cal - array[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result_count)  # 5를 반환해야 합니다!

# 0 , 문자열, character 같은 변하지 않는 primitive type의 경우는
# 파이썬 내부에서 파라미터로 넘기면
# 그 값을 복제해서 새로운 값을  생성함

# 문제가 축소되는 과정에서는 재귀함수로 해결할 수 있다
# 헷갈리는 게 있다면 모든 경우의 수를 다 써보고 시도해보자

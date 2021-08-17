# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자를 모두 0, 혹은 모두 1로 같게 만들어야 한다.
# 할 수 있는 행동은 연속된 하나의 숫자를 잡고 모두 뒤집는 것 이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.

# 규칙성 파악하기
# 모두 0으로 만드는 방법에서 최소로 뒤집는 횟수: count_to_all_zero
# 0 -> 1로 문자열이 전환되는 순간 count_to_all_zero += 1
# 모두 1로 만드는 방법에서 최소로 뒤집는 횟수: count_to_all_one
# 1 -> 0으로 문자열이 전환되는 순간 count_to_all_one += 1

# 1) 뒤집어질 때, 즉 0 -> 1 또는 1 -> 0으로 바뀔 때 횟수 추가
# 2) 첫 번째 원소가 0인지 1인지에 따라서 횟수 추가

input = "1100110011"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    if string[0] == "1":
        count_to_all_zero += 1
    elif string[0] == "0":
        count_to_all_one += 1
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == "1":
                count_to_all_zero += 1
            elif string[i + 1] == "0":
                count_to_all_one += 1
    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

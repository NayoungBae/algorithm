# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

input = 20


# 소수는 자기 자신과 1 외에는 나누어 떨어지지 않음 이걸 증명하면 됨
# -> 자기 자신과 1 이외의 숫자로 나누어 떨어지면 소수가 아니다
def find_prime_list_under_number(number):
    prime_array = []
    for num in range(2, number + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_array.append(num)

    return prime_array


result = find_prime_list_under_number(input)
print(result)

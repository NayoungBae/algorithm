# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

input = 20


# 소수는 자기 자신과 1 외에는 나누어 떨어지지 않음 이걸 증명하면 됨
# -> 자기 자신과 1 이외의 숫자로 나누어 떨어지면 소수가 아니다

# 모든 숫자 일일이 나누지 말고 num-1 소수로만 나누자 / prime_array에 2~num-1 소수만 담겨있음

# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다
# -> 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는 반드시 N의 제곱근 이하이다
def find_prime_list_under_number(number):
    prime_array = []
    for num in range(2, number + 1):
        for i in prime_array:  # for i in range(2, num): #2~num-1 -> 2~num-1이하의 소수
            if num % i == 0 and i * i <= num:
                break
        else:
            prime_array.append(num)

    return prime_array


result = find_prime_list_under_number(input)
print(result)

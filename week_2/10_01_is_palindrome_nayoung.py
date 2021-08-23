# https://nazero.tistory.com/72
# 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.

input = "abcba"


def is_palindrome(string):
    for i in range(len(string)):
        if string[i] == string[(len(string) - 1) - i]:
            continue
        else:
            return False

    return True


print(is_palindrome(input))  # True

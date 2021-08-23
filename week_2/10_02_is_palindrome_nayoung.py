# https://nazero.tistory.com/72
# 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.

input = "abcba"


def is_palindrome(string):
    n = len(string)
    if n <= 1:
        return True
    if string[0] == string[-1]:
        string = string[1:-1]
        return is_palindrome(string)
    else:
        return False


print(is_palindrome(input))  # True

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어
# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.
# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.


# [1]
# 1. ( 괄호가 열림                                         stack = ["("]
# 2. ( ( 괄호 또 열림                                      stack = ["(", "("]
# 3. ) 괄호가 닫힘! 그러면 아까 열린 것 중에 현재 열린 괄호는 (   stack = ["("]
# 4. ) 괄호가 닫힘! 그러면 아까 열린 것 중에 현재 열린 괄호는     stack = []
# 5. ( 괄호가 열림                                          stack = ["("]
# 6. ) 괄호가 닫힘! 그러면 아까 열린 것 중에 현재 열린 괄호는      stack = []


s = "(())()"


def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            if len(stack) == 0:  # 스택 비어있으면 올바르지않은 상황
                return False
            else:
                stack.pop()      # 스택에서 빼기

    if len(stack) != 0:          # 스택이 비어있지 않다면
        return False
    else:                        # 비어있다면
        return True


print(is_correct_parenthesis(s))  # True

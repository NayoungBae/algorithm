# 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.

input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if char.isalpha():
            index = ord(char) - ord('a')
            alphabet_occurrence_array[index] += 1

    not_repeating_character_array = []
    for i in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[i]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(i + ord('a')))

    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"


result = find_not_repeating_character(input)
print(result)

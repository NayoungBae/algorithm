input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    max_count = 0
    occurred_alphabet_count = [0] * 26
    for alphabet in string:
        if alphabet.isalpha():
            index = ord(alphabet) - ord('a')
            occurred_alphabet_count[index] += 1

    for num in occurred_alphabet_count:
        if num > max_count:
            max_count = num
            max_index = occurred_alphabet_count.index(max_count)
        ascii_num = max_index + ord('a')
    return chr(ascii_num)


result = find_max_occurred_alphabet(input)
print(result)
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for alphabet in string:
        if alphabet.isalpha():                      #isalpha: 알파벳인지 아닌지 판단. T/F
            index = ord(alphabet) - ord('a')        #ord: ASCII Code로 바꿔줌
            alphabet_occurrence_array[index] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}
    for key in all_array:
        dict[key] = True        # 키가 중요한거니까 아무 값이나 넣어도 상관 없음

    for key in present_array:   # dict에서 key 를 하나씩 없앰
        del dict[key]

    for key in dict.keys():
        return key              # 한 명 밖에 없으니 key 중에 하나를 바로 반환


print(get_absent_student(all_students, present_students))
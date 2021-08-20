class Person:
    # __init__ : 생성자 설정
    # self는 매개변수로 무조건 존재해야함!!
    def __init__(self, param_name):  # self: 생성자나 함수 만들 때 인자에 자기자신(클래스)을 넘겨주게 됨
        print("Person constructor!", self)
        self.name = param_name  # 내(Person 클래스) 안에다가 name이라는 변수를 만들어서 param_name의 값을 저장

    def talk(self):
        print("안녕하세요! 제 이름은", self.name, "입니다")

# Person() : Person 클래스의 생성자
person_1 = Person("라이언")  # 생성자가 호출되는 순간 클래스 내의 init 함수가 호출됨
print(person_1)  # <__main__.Person object at 0x00000189CDEF11C0>
print(person_1.name)  # 라이언  # 생성자를 통해 param_name이 클래스 내부에 self.name에 저장되어 self.name 출력
person_1.talk()

print()

person_2 = Person("춘식이")
print(person_2)  # <__main__.Person object at 0x00000189CDEF11F0>
print(person_2.name)  # 춘식이  # 생성자를 통해 param_name이 클래스 내부에 self.name에 저장되어 self.name 출력
person_2.talk()

# "클래스를 이용하면 유사한 행동이나 데이터를 쌓을 수 있게 구조를 쉽게 만들 수 있다"
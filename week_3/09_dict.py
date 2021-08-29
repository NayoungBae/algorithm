class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))


# 하지만 hash(key) % len(self.items) 을 할 경우 같은 값이 나올 수가 있음
# 그럴 경우 그 위치에 값이 덮어 씌워지는데 이걸 해결하기 위해
# Linked List를 사용할 것임
# ex) self.items[7] = [("aaa", "test")] -> [("bbb", "test11")]
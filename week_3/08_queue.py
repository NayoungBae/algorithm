class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)  # 새 노드 생성
        if self.is_empty():  # head 또는 tail이 비었는지 안 비었는지에 따라 예외처리
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node  # 현재 tail의 다음 노드가 새 노드가 됨
        self.tail = new_node  # tail을 new_node로 변경

    def dequeue(self):
        if self.is_empty():  # head와 tail이 비어있는 경우 예외처리
            return "Queue is empty"
        delete_node = self.head  # 반환하기 위해 미리 저장
        self.head = self.head.next  # head의 위치 변경
        return delete_node.data

    def peek(self):
        if self.is_empty():  # 예외처리
            return "Queue is empty"
        return self.head.data  # head 노드 반환

    def is_empty(self):
        return self.head is None  # head가 비었는지 아닌지만 반환


queue = Queue()
queue.enqueue(3)
print(queue.peek())         # 3
queue.enqueue(4)
print(queue.peek())         # 3
queue.enqueue(5)
print(queue.peek())         # 3
print(queue.dequeue())      # 3
print(queue.peek())         # 4
print(queue.is_empty())     # False
print(queue.dequeue())      # 4
print(queue.dequeue())      # 5
print(queue.is_empty())     # True
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node = Node(4)
node.next = first_node  # node의 next 변수에 first_node의 주소값 저장
print(node)  # <__main__.Node object at 0x00000298964E0FD0> <- node의 주소값
print(node.data)  # 3
print(node.next)  # <__main__.Node object at 0x00000298964E0F10> <- first_node의 주소값
print(node.next.data)  # 4

# 위처럼 매번 다음노드의 주소값을 저장하는 행위를 하면 객체 생성하는 게 엄청 많으면 일일이 다 할것인가?!!! 난 못해
print("-----------------------------------")


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)  # 인수 data의 값을 가지고 있는 노드를 head에 저장

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)

    # 노드들의 값들을 전부 출력
    def print_all(self):
        if self.head is None:
            print("Node is None")
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList(3)
print(linked_list)
print(linked_list.head)
print(linked_list.head.next)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()

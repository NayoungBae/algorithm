# https://nazero.tistory.com/73
# 링크드 리스트의 끝에서 K번째 값을 반환하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        node_array = []
        current_node = self.head
        node_array.append(current_node)
        while current_node.next is not None:
            current_node = current_node.next
            node_array.append(current_node)
        array_len = len(node_array)
        print(node_array)
        return node_array[array_len - k]


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
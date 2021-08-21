class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)

    def print_all(self):
        if self.head is None:
            print("Node is None")
            return

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def get_node(self, index):
        current_index = 0
        current_node = self.head
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1
        return "Node is None!!"

    # index 번째 원소값을 추가
    def add_node(self, index, data):
        current_index = 0
        current_node = self.head
        while current_index < index - 1:
            current_node = current_node.next
            current_index += 1
        next_node = current_node.next
        current_node.next = Node(data)
        current_node.next.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()   # 5 -> 12
print()
linked_list.add_node(1, 3)
linked_list.print_all()   # 5 -> 3 -> 12


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
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        return current_node

    # index 번째 원소값을 추가
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def get_node_length(self):
        count = 0
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
        return count

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 6)
linked_list.print_all()  # 6 -> 5 -> 12
print()
linked_list.delete_node(0)
linked_list.print_all()  # 5 -> 12

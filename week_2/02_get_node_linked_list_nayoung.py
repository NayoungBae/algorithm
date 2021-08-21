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
        return "None!!"


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1).data)   # 12

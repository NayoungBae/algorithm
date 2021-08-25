# https://nazero.tistory.com/73
# 링크드 리스트의 끝에서 K번째 값을 반환하시오.

# 1. 노드를 두 개 잡는다.
# 2. 한 노드를 다른 노드보다 k 만큼 떨어지게 한다.
# 3. 그리고 계속 한 칸씩 같이 이동한다.
# 4. 만약 더 빠른 노드가 끝에 도달했다면
#    느린 노드는 끝에서 k 만큼 떨어진 노드가 되므로
#    바로 반환하자.
# 빠른노드: O(N), 느린노드:O(N-k)

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
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!


# 01_01과 01_02의 시간복잡도는 동일함. 02에서 01보다 개선된건 없음 코드 길이만 줄었을 뿐
# 시간 복잡도를 분석하기 위해서는 코드에서 실행된 연산량을 통해 추정하는 게 더 올바른 생각의 흐름이다
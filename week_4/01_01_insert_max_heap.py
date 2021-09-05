class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 1. 새 노드를 맨 끝에 추가
    # 2. 지금 넣은 새 노드를 부모와 비교. 만약 부모보다 크다면 교체
    # 3. 이 과정을 꼭대기까지 반복
    def insert(self, value):
        self.items.append(value)
        current_index = len(self.items) - 1

        while current_index > 1:    # 최상위 노드로 갈때까지 반복
            parent_index = current_index // 2
            if self.items[current_index] > self.items[parent_index]:
                self.items[current_index], self.items[parent_index] = self.items[parent_index], self.items[current_index]
                current_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3]
 #     9
 #   4   2
 # 3


 # 레벨이 0이 될 때까지 값을 계속 비교
 # 완전 이진트리의 높이는 O(log(N))
 # 높이만큼 올라가는게 최대의 길이니까
 # 반복하는 최대 횟수도 O(log(N))
 # -> max 힙의 원소 추가는 O(log(N)) 만큼의 시간복잡도를 가짐
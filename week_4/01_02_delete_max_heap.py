class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 1. 루트 노드와 맨 끝에 있는 원소 교채
    # 2. 맨 뒤에 있는 원소(원래 루트 노드)를 삭제. 끝에 반환해야하니까 저장해둠
    # 3. 변경된 노드와 자식 노드들을 비고. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿈
    # 4. 두 자식 노드보다 부모 노드가 더 크거나
    #    가장 바닥에 도달하지 않을 떄까지(:자식이 더이상 없다) 3.을 반복
    # 5. 2.에서 제거한 원래 루트 노드 반환
    def delete(self):
        # 1.
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # 2.
        prev_max = self.items.pop()

        # 3.
        current_index = 1   # 루트노드
        while current_index <= len(self.items) - 1:     # 노드들의 인덱스에서 벗어나지 않을 때까지 반복
            left_child_index = current_index * 2
            right_child_index = current_index * 2 + 1
            max_index = current_index

            # 왼쪽 자식이 있을 경우(인덱스에서 벗어나지 않은 경우) && 부모노드 값보다 더 클 경우
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            # 오른쪽 자식이 있을 경우(인덱스에서 벗어나지 않은 경우) && 부모노드 값보다 더 클 경우
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            # 부모노드가 자식노드들보다 크다라는 말
            if max_index == current_index:
                break

            self.items[current_index], self.items[max_index] = self.items[max_index], self.items[current_index]
            current_index = max_index

        return prev_max  # 8 반환


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]


# 원소를 최대값에 빠르게 추가하거나 삭제하는 문제에 사용하면 좋음
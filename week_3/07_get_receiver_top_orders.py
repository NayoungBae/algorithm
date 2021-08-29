top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    array = [0] * len(heights)
    while heights:  # heights가 있는 동안 반복
        height = heights.pop()
        for idx in range(len(heights)-1, 0, -1):
            if heights[idx] > height:
                array[len(heights)] = idx + 1
                break
    return array


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4]
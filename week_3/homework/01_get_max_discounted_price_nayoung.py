# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.


shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array


def get_max_discounted_price(prices, coupons):
    prices = insert_sort(prices)
    coupons = insert_sort(coupons)
    prices_index = len(prices)-1
    coupons_index = len(coupons)-1
    discounted_sum = 0
    while prices_index >= 0 and coupons_index >= 0:
        discounted_sum += int(prices[prices_index] * (1 - coupons[coupons_index] * 0.01))
        prices_index -= 1
        coupons_index -= 1
    while prices_index >= 0:
        discounted_sum += prices[prices_index]
        prices_index -= 1
    return discounted_sum


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000

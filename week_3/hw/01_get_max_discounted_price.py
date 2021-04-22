shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    # 가격 및 쿠폰들을 정렬하고, 가장 큰 가격에 가장 할인율이 큰 쿠폰을 적용한다.
    prices = merge_sort(prices)
    coupons = merge_sort(coupons)

    result = []
    while coupons:
        discount_price = prices[-1] * ((100 - coupons[-1])/100)
        result.append(discount_price)
        del prices[-1]
        del coupons[-1]

        if not prices :
            break
    result.extend(prices)

    return int(sum(result))


def merge_sort(array) :
    if len(array) <= 1 :
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return merge(left_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while len(result) < len(array1) + len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

        if array1_index > len(array1) - 1:
            result.extend(array2[array2_index:])
        elif array2_index > len(array2) - 1:
            result.extend(array1[array1_index:])
    return result


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.

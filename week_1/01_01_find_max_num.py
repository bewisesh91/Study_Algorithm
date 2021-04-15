input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]
    for i in array:
        if i > max_num:
            max_num = i
    return max_num


result = find_max_num(input)
print(result)

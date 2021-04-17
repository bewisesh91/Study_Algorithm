finding_target = 11
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# def is_existing_target_number_binary(target, array):
#     # 구현해보세요!
#     first = finding_numbers[0]
#     last = finding_numbers[-1]
#     mid = (first+last) // 2
#
#     while target != mid :
#         if target < mid :
#             last = mid
#             mid = (first+last) // 2
#         elif target > mid :
#             first = mid + 1
#             mid = (first + last) // 2
#     return mid


def is_existing_target_number_binary(target, array):
    current_min_index = 0
    current_max_index = len(array) - 1
    current_mid_index = (current_min_index + current_max_index) // 2

    while current_min_index <= current_max_index:
        if array[current_mid_index] == target:
            return True
        elif array[current_mid_index] < target:
            current_min_index = current_mid_index + 1
        else:
            current_max_index = current_mid_index - 1
        current_mid_index = (current_min_index + current_max_index) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

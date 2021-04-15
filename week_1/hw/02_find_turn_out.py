input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    all_zero = 0
    all_one = 0

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '1':
                all_zero += 1
            elif string[i + 1] == '0':
                all_one += 1

    if string[0] == '0':
        all_one += 1
    elif string[0] == '1':
        all_zero += 1

    print(all_zero, all_one)
    return min(all_zero, all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

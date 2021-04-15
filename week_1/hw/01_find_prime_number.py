input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    result =[]
    for i in range(2, number) :
        count = 0
        for j in range(1, i+1) :
            if i % j == 0 :
                count += 1
        if count == 2 :
            result.append(i)
    return result


result = find_prime_list_under_number(input)
print(result)
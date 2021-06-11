def linear_search(element, list) :
    for i in range(len(list)) :
        if list[i] == element :
            return i
    return None

ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'찾고자 하는 element 3의 인덱스는 {linear_search(3, ex_list)} 입니다.')



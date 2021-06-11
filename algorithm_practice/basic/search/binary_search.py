def binary_search(element, list) :
    first_index = 0
    last_index = len(list) - 1
    
    while first_index <= last_index :
        mid_index = (first_index + last_index) // 2
        if element > list[mid_index] :
            first_index = mid_index + 1
        elif element < list[mid_index] :
            last_index = mid_index - 1
        else :
            return mid_index
    return None

ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'찾고자 하는 element 9의 인덱스는 {binary_search(9, ex_list)} 입니다.')


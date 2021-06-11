def merge(list1, list2) :
    i = 0
    j = 0
    merged_list = []
    
    while i < len(list1) and j <len(list2) :
        if list1[i] > list2[j] :
            merged_list.append(list1[i])
            i += 1
        else :
            merged_list.append(list2[j])
            j += 1

    if i == len(list1) :
        merged_list += list2[j:]
    elif j == len(list2) :
        merged_list += list1[i:]

    return merged_list


def merge_sort(list) :
    if len(list) < 2 :
        return list
    else :
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        return merge(merge_sort(left), merge_sort(right))

ex_list = [10, 3, 2, 4, 5, 6, 9, 7, 1, 8]
print(merge_sort(ex_list))




input = [4, 6, 2, 9, 1]


# 숫자 하나 씩 비교하는 과정에서 가장 큰 숫자를 맨 오른쪽에 배치하는 과정을 반복
def bubble_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i) : # i를 빼주는 이유는 맨 마지막은 이미 정렬되어 있는 것이기 때문
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
def swap(tree, index_1, index_2):
    tree[index_1], tree[index_2] = tree[index_2], tree[index_1]

def heapify(tree, index, tree_size):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  

    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다

def heapsort(tree):
    tree_size = len(tree)

    # 전체 tree 구조를 heap 상태로 만든다.
    for index in range(tree_size, 0, -1) :
        heapify(tree, index, tree_size)

    #    
    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)
        heapify(tree, 1, i)

# 실행 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)
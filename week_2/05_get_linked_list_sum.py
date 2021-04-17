class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head
    cur1_result = ''
    cur2_result = ''
    while cur1 is not None:
        cur1_result += str(cur1.data)
        cur1 = cur1.next
    while cur2 is not None:
        cur2_result += str(cur2.data)
        cur2 = cur2.next

    return int(cur1_result) + int(cur2_result)


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    cur1 = linked_list_1.head
    cur2 = linked_list_2.head
    cur1_result = 0
    cur2_result = 0
    while cur1 is not None:
        cur1_result = cur1_result * 10 + cur1.data
        cur1 = cur1.next
    while cur2 is not None:
        cur2_result = cur2_result * 10 + cur2.data
        cur2 = cur2.next

    return cur1_result + cur2_result


def get_linked_list_sum_helper(linked_list):
    cur = linked_list.head
    result = 0
    while cur is not None:
        result = result * 10 + cur.data
        cur = cur.next
    return result


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum1 = get_linked_list_sum_helper(linked_list_1)
    sum2 = get_linked_list_sum_helper(linked_list_2)
    return sum1 + sum2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))

# linked list 만들기

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # linked list 마지막 원소 뒤에 새로운 원소 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        result = []
        while cur is not None:
            print(cur.data)
            result.append(cur.data)
            cur = cur.next
        return result


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
print(linked_list.print_all())


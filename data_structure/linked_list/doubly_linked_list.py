class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None

class LinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None

    # 데이터 탐색 메소드
    def find_node_with_index(self, index) :
        iterator = self.head

        for i in range(index) :
            iterator = iterator.next
        
        return iterator

    def find_node_with_data(self, data) :
        iterator = self.head

        while iterator is not None :
            if iterator.data == data :
                return iterator
            else :
                iterator = iterator.next

        return None

    # 데이터 삽입 메소드
    def prepend(self, data) :
        new_node = Node(data)

        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, previous_node, data) :
        new_node = Node(data)

        if previous_node is self.tail :
            previous_node.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else :
            new_node.next = previous_node.next
            new_node.prev = previous_node
            previous_node.next.prev = new_node
            previous_node.next = new_node
    
    def append(self, data) :
        new_node = Node(data) 

        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # 데이터 삭제 메소드
    def delete(self, node_to_delete) :
        if node_to_delete is self.head and node_to_delete is self.tail :
            self.head = None
            self.tail = None
        elif node_to_delete is self.head :
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail :
            self.tail = self.tail.prev
            self.tail.next = None
        else :
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.data

        
    def __str__(self) :
        res_str = "|"

        iterator = self.head

        while iterator is not None :
            res_str += f' {iterator.data} |'
            iterator = iterator.next

        return res_str

            
                


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스

class LinkedList:
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def find_node_with_key(self, key):
        iterator = self.head   # 링크드 리스트를 돌기 위해 필요한 노드 변수
    
        while iterator is not None:
            if iterator.key == key:
                return iterator
            else :
                iterator = iterator.next
        
        return None
    
    def append(self, key, value):
        new_node = Node(key, value)
    
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node  
    
    def delete(self, node_to_delete):    
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None
    
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
    
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
    
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
    
    def __str__(self):
        res_str = ""
    
        iterator = self.head
    
        while iterator is not None:
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next 
    
        return res_str


class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for i in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        return hash(key) % self._capacity

    def _get_linked_list_for_key(self, key):
        hashed_index = self._hash_function(key)
        return self._table[hashed_index]

    def _look_up_node(self, key):
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        return self._look_up_node(key).value

    def insert(self, key, value):
        existing_node = self._look_up_node(key)  

        if existing_node is not None:
            existing_node.value = value  
        else:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)

    def delete_by_key(self, key):
        node_to_delete = self._look_up_node(key)
        
        if node_to_delete is not None:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.delete(node_to_delete)

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]



test_scores = HashTable(50) # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

# 학생들 시험 점수 삭제
test_scores.delete_by_key("태호")
test_scores.delete_by_key("지웅")
test_scores.delete_by_key("신의")
test_scores.delete_by_key("현승")
test_scores.delete_by_key("규식")

print(test_scores)
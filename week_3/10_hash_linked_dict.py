class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k :
                return v


class LinkedDict:
    def __init__(self):
        self.itmes = []
        for i in range(8) :
            self.itmes.append(LinkedTuple())        # 리스트안에 튜플 8개를 만든다.

    def put(self, key, value):
        index = hash(key) % len(self.items)         # 같은 index안에 여러 값이 들어갈 수 있다.
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        self.items[index].get(key)

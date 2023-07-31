class HashTable:

    def __init__(self, capacity=20):
        self.capacity = capacity
        self.size = 0
        self.table = []
        for _ in range(capacity):
            self.table.append([])

    def key_hash(self, key):
        return int(key) % self.capacity

    def put(self, key, value):
        index = self.key_hash(key)
        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                kv_pair[1] = value
                return
        self.table[index].append([key, value])
        self.size += 1

    def get(self, key):
        index = self.key_hash(key)
        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                return kv_pair[1]
        return None

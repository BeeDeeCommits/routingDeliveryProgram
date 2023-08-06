class HashTable:
    # Method/Constructor to initialize a Hashtable object
    def __init__(self, capacity=30):
        self.capacity = capacity
        self.size = 0
        self.table = []
        for _ in range(capacity):
            self.table.append([])

    # Calculate the index/bucket where the key-value pair should be stored in the table
    def key_hash(self, key):
        return int(key) % self.capacity

    # Insert a key-value pair into the table
    def put(self, key, value):
        # Check if the load factor exceeds threshold(70%)
        load_factor = self.size / self.capacity
        # If it does, resize the hash table by double its capacity
        if load_factor > 0.7:
            new_capacity = self.capacity * 2
            self.resize(new_capacity)
        # Calculate the index/bucket where the key-value pair should be stored in the table
        index = self.key_hash(key)
        # If the key is valid, update the value associated with the key
        for kv_pair in self.table[index]:
            if kv_pair[0] == key:
                kv_pair[1] = value
                return
        self.table[index].append([key, value])
        self.size += 1

    def get(self, key):
        # Calculate the index/bucket where the key-value pair should be stored in the table
        index = self.key_hash(key)
        # Loop through the key-value pairs at the calculated index/bucket
        # (Only one pair exists in this hashtable per bucket; There is no chaining)
        for kv_pair in self.table[index]:
            if kv_pair[0] == key:  # If the key of the current key-value pair matches the given key
                return kv_pair[1]  # Return the value associated with the given key
        #  If the key is not found in the table, return None
        return None

    # Method to resize table when load factor is over threshold(More than a certain percentage of the table is occupied)
    def resize(self, new_capacity):
        # save the state of the old table
        old_table = self.table
        # update the capacity to be the new capacity
        self.capacity = new_capacity
        # clear the old table
        self.table = []
        for _ in range(new_capacity):
            self.table.append([])
        # Rehash and move the existing key-value pairs to the new hash table
        for bucket in old_table:
            for kv_pair in bucket:
                key = kv_pair[0]
                value = kv_pair[1]
                new_index = self.key_hash(key)
                self.table[new_index].append([key, value])

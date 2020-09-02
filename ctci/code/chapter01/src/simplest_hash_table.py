# Some code taken from 
# http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/


# Uses linear probing
class LPHashTable:
    def __init__(self, size=10):
        self.hash_table = [None] * size

    def hash_func(self, key):
        return key % len(self.hash_table)

    def insert(self, key, val):
        starting_place = self.hash_func(key)
        for i in range(len(self.hash_table)):
            slot = (starting_place + i) % len(self.hash_table)
            if self.hash_table[slot] is None:
                self.hash_table[slot] = val
                return
        raise IndexError

    def search(self, key, val):
        starting_place = self.hash_func(key)
        for i in range(len(self.hash_table)):
            slot = (starting_place + i) % len(self.hash_table)
            if self.hash_table[slot] == val:
                return True
            if self.hash_table[slot] is None:
                return False
        return False


# Uses chaining
class ChainHashTable:
    def __init__(self, size=10):
        self.hash_table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % len(self.hash_table)

    def insert(self, key, val):
        hash_key = self.hash_func(key)
        self.hash_table[hash_key].append(val)

    def search(self, key, val):
        hash_key = self.hash_func(key)
        bucket = self.hash_table[hash_key]
        for i in bucket:
            if i == val:
                return True
        return False


# Uses standard library hash function
class StandardHashTable:
    def __init__(self, size=10):
        self.hash_table = [[] for _ in range(size)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]    
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True 
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = hash(key) % len(self.hash_table)    
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = hash(key) % len(self.hash_table)    
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv 
            if key == k:
                key_exists = True 
                break
        if key_exists:
            del bucket[i]

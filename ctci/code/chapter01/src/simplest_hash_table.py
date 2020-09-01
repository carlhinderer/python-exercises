# Some code taken from 
# http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/


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

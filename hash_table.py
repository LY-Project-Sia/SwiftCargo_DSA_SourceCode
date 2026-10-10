"""
Task 3.1: Hash Table with Separate Chaining and Open Addressing
"""
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for kv in self.table[idx]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[idx].append([key, value])

if __name__ == "__main__":
    S = 7148
    # Smallest prime greater than 1000 + S = 8148
    m = 8159
    print(f"--- TASK 3.1: HASH TABLE (m = {m}) ---")
    ht = HashTableChaining(m)
    for i in range(5000):
        ht.insert(f"SC2026{i:06d}", f"Parcel_{i}")
    print("Inserted 5,000 tracking numbers successfully into Separate Chaining Hash Table.")
    print("Task 3.1 executed successfully.\n")

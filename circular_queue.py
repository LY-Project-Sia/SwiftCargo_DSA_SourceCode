"""
Task 2.2: Queue - Fair Rider Dispatch (Circular Queue with Priority)
"""
class CircularPriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0

    def enqueue(self, parcel_id, priority="Standard"):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue parcel.")
            return False
        
        item = (parcel_id, priority)
        if priority == "Same-Day":
            # Insert with priority handling (simulate front placement for same-day)
            self.head = (self.head - 1 + self.capacity) % self.capacity
            self.queue[self.head] = item
        else:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        print(f"Enqueued [{priority}]: {parcel_id}")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! No parcels to dispatch.")
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        print(f"Dispatched: {item}")
        return item

if __name__ == "__main__":
    S = 7148
    capacity = 20 + (S % 30)
    print(f"--- TASK 2.2: CIRCULAR PRIORITY QUEUE (Capacity = {capacity}) ---")
    cpq = CircularPriorityQueue(capacity)
    
    parcels = [("SC001", "Standard"), ("SC002", "Same-Day"), ("SC003", "Standard"),
               ("SC004", "Same-Day"), ("SC005", "Standard"), ("SC006", "Standard"),
               ("SC007", "Same-Day"), ("SC008", "Standard"), ("SC009", "Standard"),
               ("SC010", "Same-Day"), ("SC011", "Standard"), ("SC012", "Standard"),
               ("SC013", "Same-Day"), ("SC014", "Standard"), ("SC015", "Standard")]
            
    for pid, prio in parcels:
        cpq.enqueue(pid, prio)
    
    print("\nDequeuing 5 parcels:")
    for _ in range(5):
        cpq.dequeue()
    print("Task 2.2 executed successfully.\n")

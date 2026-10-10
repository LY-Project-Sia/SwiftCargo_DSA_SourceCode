"""
Task 2.3: Linked List - Truck Manifest with Cycle Detection
"""
class Node:
    def __init__(self, tracking_no):
        self.tracking_no = tracking_no
        self.next = None
        self.prev = None

class DoublyLinkedListManifest:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, tracking_no):
        new_node = Node(tracking_no)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def detect_cycle(self):
        """Floyd's Cycle-Finding Algorithm (Tortoise and Hare)"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def reverse_in_place(self):
        curr = self.head
        self.tail = curr
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            curr.prev = next_node
            prev = curr
            curr = next_node
        if prev:
            self.head = prev

if __name__ == "__main__":
    print("--- TASK 2.3: DOUBLY LINKED LIST MANIFEST ---")
    manifest = DoublyLinkedListManifest()
    for i in range(1, 11):
        manifest.insert_tail(f"SC2026{i:04d}")
    
    print(f"Cycle detected in manifest: {manifest.detect_cycle()}")
    manifest.reverse_in_place()
    print("Manifest reversed successfully.")
    print("Task 2.3 executed successfully.\n")

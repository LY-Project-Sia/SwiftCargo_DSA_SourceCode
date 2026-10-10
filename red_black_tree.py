"""
Task 3.2 & 3.3: Customer BST and Red-Black Tree
"""
class Node:
    def __init__(self, surname):
        self.surname = surname
        self.left = None
        self.right = None

def insert_bst(root, surname):
    if not root:
        return Node(surname)
    if surname < root.surname:
        root.left = insert_bst(root.left, surname)
    elif surname > root.surname:
        root.right = insert_bst(root.right, surname)
    return root

def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

if __name__ == "__main__":
    print("--- TASK 3.2: CUSTOMER BST DEGRADATION ---")
    surnames = ["Abad", "Bautista", "Cruz", "Dela Cruz", "Espiritu", 
                "Flores", "Garcia", "Hernandez", "Ilagan", "Jimenez"]
    
    root_sorted = None
    for name in surnames:
        root_sorted = insert_bst(root_sorted, name)
    print(f"Height of strictly sorted BST (Degraded): {get_height(root_sorted)}")
    print("Task 3 executed successfully.\n")

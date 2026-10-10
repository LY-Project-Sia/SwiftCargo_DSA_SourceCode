"""
Task 2.1: Stack - Undo/Redo in the Encoding App
"""
class EncodingStack:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def perform_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()  # Clear redo on new action
        print(f"Action Performed: {action}")

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            print(f"Undo: Rolled back '{action}'")
        else:
            print("Undo stack is empty.")

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            print(f"Redo: Reapplied '{action}'")
        else:
            print("Redo stack is empty.")

if __name__ == "__main__":
    print("--- TASK 2.1: STACK UNDO/REDO ---")
    app = EncodingStack()
    actions = ["ADD P1", "EDIT P1 Address", "ADD P2", "DELETE P2", "ADD P3", 
               "EDIT P3 Weight", "ADD P4", "EDIT P1 Name", "ADD P5", "EDIT P2 Address"]
    for act in actions[:10 + (7148 % 10)]:
        app.perform_action(act)
    
    print("\nExecuting 3 undos and 1 redo:")
    app.undo()
    app.undo()
    app.undo()
    app.redo()
    print("Task 2.1 executed successfully.\n")

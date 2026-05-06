class Stack:
    def __init__(self):
        # Initializes an empty list to hold stack elements
        self.items = []
    def is_empty(self):
        # Returns True if the stack is empty; otherwise, False
        return len(self.items) == 0
    def push(self, item):
        # Adds item to the end of the list (top of the stack)
        self.items.append(item)
    def pop(self):
        # Removes and returns the last item (top of the stack), if not empty
        return self.items.pop() if not self.is_empty() else None
    def peek(self):
        # Returns the last item without removing it, if not empty
        return self.items[-1] if not self.is_empty() else None
    def size(self):
        # Returns the number of items in the stack
        return len(self.items)

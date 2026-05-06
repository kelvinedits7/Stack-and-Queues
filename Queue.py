class Queue:
    def __init__(self):
        # Initializes an empty list to hold queue elements
        self.items = []
    def is_empty(self):
        # Returns True if the queue is empty; otherwise, False
        return len(self.items) == 0
    def enqueue(self, item):
        # Adds an item to the end of the list (end of the queue)
        self.items.append(item)
    def dequeue(self):
        # Removes and returns the first item (front of the queue), if not empty
        return self.items.pop(0) if not self.is_empty() else None
    def size(self):
        # Returns the number of items in the queue
        return len(self.items)

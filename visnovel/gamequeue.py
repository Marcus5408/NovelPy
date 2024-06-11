from collections import deque


class GameQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        # Add an item to the end of the queue.
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the item from the start of the queue.
        if self.is_empty():
            return None
        return self.queue.popleft()

    def peek(self):
        # Return the item at the start of the queue without removing it.
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        # Check if the queue is empty.
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue.
        return len(self.queue)

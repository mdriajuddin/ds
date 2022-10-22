# Implementation of the Stack ADT using a Python list.

class Stack:
    # Create an empty stack.
    def __init__(self):
        self._theItems = list()
    
    # Returns True if the stack is emptu or False otherwise.
    def isEmpty(self):
        return len(self._theItems) == 0
    
    # Returns the number of items in the stack.
    def peek(self):
        assert not self.isEmpty(), "Cannot pop form an empty stack"
        return self._theItems.pop()
    
    # Psuh an item onto the top of the stack.
    def push(self, item):
        self._theItems.append(item)
        



































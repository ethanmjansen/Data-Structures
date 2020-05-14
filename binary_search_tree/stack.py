"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import LinkedList

class Array_Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.insert(self.size + 1, value)

    def pop(self):
        if self.size == 0:
            pass
        else:
            value = self.storage.pop()
            self.size -= 1
            return value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if not self.storage.head:
            self.size ==0
        else:
            self.size -= 1
            return self.storage.remove_head()

""" The difference between the two is that an array can use python functions and a 
linked list has to be implemented as a class."""
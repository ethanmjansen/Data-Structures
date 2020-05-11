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

class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class Stack:
    def __init__(self):
        # first node in the list 
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head:
            self.size += 1
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it
            self.size += 1 
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list 
            current.set_next(new_node)

    def pop(self):
        # If linked list is empty
        if self.head == None:
            return None

        # If linked list is not empty
        current = self.head

        previous_node = None

        while current.get_next():
            previous_node = current
            current = current.get_next()

        if previous_node:
            previous_node.next_node = None

        else:
            self.head = None
        
        self.size -= 1
        value = current.get_value()
        return value
                

""" The difference between the two is that an array can use python functions and a 
linked list has to be implemented as a class."""
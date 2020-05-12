class Node:
    
    def __init__(self,value=None,next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_data(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_node):
        self.next_node = new_node

class LinkedList:
    
    def __init__(self,head=None):
        self.head = head
        self.size = 0
        self.tail = self.size + 1

    def insert_head(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def add_to_tail(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(self, value)
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

    def remove_head(self):
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

    def contains(self, value):
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            else:
                current = current.get_next()
        return False

    def get_max(self):
        pass
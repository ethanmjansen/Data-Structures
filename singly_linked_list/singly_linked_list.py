class Node:
    
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self,new_node):
        self.next = new_node

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def contains(self, value):
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            else:
                current = current.get_next()
        return False

    def remove_head(self):
        current = self.head

        if not self.head and not self.tail:
            return None
        else: 
            value = self.head.value
            self.head = self.head.next
            self.tail = current.next
            return value

    def get_max(self):
        current = self.head      
        max = 0

        if current == None:
            return None
        else:
            while (current != None):  
                if (max < current.get_value()): 
                    max = current.get_value()
                current = current.get_next()

        return max

    def print_list(self):
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.get_value())
            current = current.get_next()
        print(self.temp) 


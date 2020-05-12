class Node:
    
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_node):
        self.next_node = new_node

class LinkedList():

    def __init__(self):
        self.head = None
        
    def insert_head(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        current = self.head
        if current is None:
            self.head = new_node
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)
        self.tail = new_node

    def contains(self, value):
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            else:
                current = current.get_next()
        return False

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.get_value() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                break
            else:
                prev = current
                current = current.get_next()

    def remove_head(self):
        current = self.head

        if not self.head:
            return None
        else: 
            value = self.head.get_value()
            self.head = self.head.get_next()
            while current.get_next():
                current = current.get_next()
            self.tail = current.get_next()
            return value

    def remove_tail(self):
        current = self.head
        previous_node = None
        
        if self.head == None:
            return None

        while current.get_next():
            previous_node = current
            current = current.get_next()

        if previous_node:
            previous_node.next_node = None
        else:
            self.head = None

        value = current.get_value()
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

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(10)
    linked_list.add_to_tail(9)
    linked_list.add_to_tail(40)
    linked_list.add_to_tail(59)
    linked_list.print_list()
    linked_list.remove_head()
    linked_list.print_list()
    linked_list.remove_tail()
    linked_list.print_list()
    linked_list.get_max()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LL:
    def __init__(self):
        self.head = None
    # insert at the beginning
    def insert_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    # insert at the end
    def insert_end(self, data):
        ne = Node(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = ne
    # insert at the specific position  
    def insert_position(self, data, position):
        np = Node(data)
        node = self.head
        for i in range(position-1):
            node = node.next
        np.data = data
        np.next = node.next
        node.next = np
        
    
    def display(self):
        node = self.head
        if node is None:
            print("list is empty")
        else:
            while node:
                print(node.data, ">>", end = '')
                node = node.next
                if node == self.head:
                    break
                 
        
        
n = LL()
n.head = Node(1)
n2 = Node(2)
n.head.next = n2
third = Node(3)
n2.next = third
third.next = n.head
# n.insert_beginning(0)
# n.insert_end(7)
# n.insert_position(8, 3)
n.display()




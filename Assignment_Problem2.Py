# Intializing the node of singly linked list  
class Node:  
    def __init__(self,data):  
        self.data = data 
        self.next = None  
          
class SortedLinkedList:  
    #Representing the head and next of given singly linked list  
    def __init__(self):  
        self.head = None  
        self.next = None  
          
    #Creating  addNode() function to add newly created nodes 
    def addNode(self, data):  
        #Create a new node  
        new_Node = Node(data)  
          
        #Checks if the list is empty  
        if(self.head == None):  
            # if list is empty the newly create node added in the list
            self.head = new_Node  
            self.next = new_Node  
        else:  
            #Otherwise, new node will be take place after next such that next's next will point to new_Node  
            self.next.next = new_Node  
            #new_Node will become new next of the list  
            self.next = new_Node  
              
    # This method will sort the linked list 
    def SortedLinkedList(self):  
        #Node current will point to head  
        current = self.head  
        index = None  
        # check whether list is empty or not
        if(self.head == None):  
            return  
        else:  
            while(current != None):  
                #Node index will point to node next to current  
                index = current.next
                  
                while(index != None):  
                    # If current node's data is greater than index's node data, swap the data between them  
                    if(current.data > index.data):  
                        temp = current.data
                        current.data = index.data  
                        index.data = temp  
                    index = index.next  
                current = current.next  
                  
    # This function will display the original and linked list
    def display_list(self):  
        #Node current will point to head  
        current = self.head  
        if(self.head == None):  
            print("List is empty")  
            return  
        while(current != None):  
            print(current.data, '-', end = ' ')  
            current = current.next  
        print("")
   
NewList = SortedLinkedList()  
          
#Adds data to the list  
NewList.addNode(4)  
NewList.addNode(2)  
NewList.addNode(1)  
NewList.addNode(3)  
 
   

print("Original list: ")  
NewList.display_list()  
  
 
NewList.SortedLinkedList()  
   
print("Sorted list: ")  
NewList.display_list()  

# Output:
#Original list: 
# 4 - 2 - 1 - 3 - 
# Sorted list:
# 1 - 2 - 3 - 4 -
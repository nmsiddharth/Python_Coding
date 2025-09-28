class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self,data):      # Adding node at end
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node  
            self.tail = new_node
            self.length+=1    
            
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head     # Here new_node's next is pointing to current head.
        self.head = new_node    
        if self.tail == None:    # If list is empty
            self.tail = new_node
        self.length+=1
        
        
    def insert(self,index,data):
        new_node = Node(data)
        i = 0
        temp = self.head   # used for traversing through the list
        
        if index>=self.length:
            self.append(data)
            return
        
        if index==0:
            self.prepend(data)
            return
        
        while i<self.length:
            if i == index-1:
                new_node.next = temp.next   # znew node.next is refernce to temp's next            5
                temp.next = new_node        # temp.next is refering to new_node          1 -> 2 ->   3 -> 4 ->
                self.length+=1                                              # Here 2 is temp and 3 is temp.next
                break                                                      # But when 5 is inserted new_node.next becomes 3 and temp.next becomes 5
            temp = temp.next                                                    #       1 -> 2 -> 5 -> 3 -> 4 ->
            i+=1        
    
    
    def remove(self,index):
        temp = self.head
        i=0
        if index>=self.length:
            print("Entered wrong index")
            return # Added return to prevent further execution after error
        
        if index == 0: # Correctly handles removing the head
            self.head = self.head.next
            self.length -= 1   
            # Missing tail update if the list becomes empty
        if self.length == 0:
            self.tail = None
            return     

        while i<self.length: # Loop for middle/end removal
            if i == index-1:
                # Check if we are removing the tail
                if temp.next == self.tail:
                    self.tail = temp # Update tail to the node before the removed one
                temp.next = temp.next.next # Bypass the node to be removed
                self.length-=1
                break
            i+=1
            temp = temp.next                      
            
                
    def get(self,index):
        if self.head is None:
            print("Empty List")
            return None
            
        if index>=self.length:
            print("Error: Index out of range!")
            return None
        
        temp = self.head
        
        for i in range(index):
            temp = temp.next  
        print(temp.data)           
            
            
    def display(self):
        temp = self.head   # We should use temporary pointer to traverse the list, if not used at the end this function, self.head becomes None even though there are elements in the list.
        while temp!=None:
            print(temp.data,end=" -> ")
            temp = temp.next   # Incrementing the pointer 
        print(end="Null")
        print()
        
        
        
l = Linkedlist()        
l.append(10)
l.display()
l.append(5)
l.display()
l.append(7)
l.display()
l.prepend(2)
l.display()
l.insert(2,4)
l.display()
l.remove(2)
l.display()
l.get(0)
l.display()

          

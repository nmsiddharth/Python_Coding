class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#  Creating Nodes
node1 = Node(10)
node2 = Node(20)        
node3 = Node(30)        
node4 = Node(40)        
node5 = Node(50)  

# Linking the Nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Delete Node where data = 30
head = node1
current = head

while current.next.data != 30:
    current = current.next
current.next = current.next.next

current = head

# Printing the updated linked list
while current is not None:
    print(current.data,end='->')
    current = current.next
print('None')
    
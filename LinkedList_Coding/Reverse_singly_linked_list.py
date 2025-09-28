class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Reversing Linked List Logic using 3 pointers
    def reverse_list(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  # Set the new head of the list
        return self.head
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# --- Example Usage ---

# Manually creating the linked list
head_node = Node(1)
head_node.next = Node(2)
head_node.next.next = Node(3)
head_node.next.next.next = Node(4)
head_node.next.next.next.next = Node(5)

# Creating a LinkedList object and setting its head
my_list = LinkedList()
my_list.head = head_node

print("Original list:")
my_list.print_list()

# Reversing the list
my_list.reverse_list(my_list.head)

print("Reversed list:")
my_list.print_list()
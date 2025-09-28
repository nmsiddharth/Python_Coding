class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def display(self):
        temp = self.head
        if temp is None:
            print("Null")
            return
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

    def reverse(self):
        # Handle empty or single-node list
        if self.head is None or self.head.next is None:
            return

        original_head = self.head # Will become the new tail
        
        prev = None
        current = self.head
        next_node = None 

        while current is not None:
            next_node = current.next  # 1. Store next node
            current.next = prev       # 2. Reverse current node's pointer
            prev = current            # 3. Move prev one step forward
            current = next_node       # 4. Move current one step forward

        # Update head and tail of the LinkedList object
        self.head = prev           # The 'prev' pointer is now the new head
        self.tail = original_head  # The original head is now the new tail
        
        # Ensure the new tail points to Null.
        # This check is important because if original_head was None, original_head.next would error.
        # However, the initial check `if self.head is None or self.head.next is None`
        # handles empty and single-node lists, so original_head will always exist here.
        self.tail.next = None 


# --- How you would use it ---
my_list = LinkedList() # Correct way to instantiate your current LinkedList class
my_list.append(1)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print("Original List:")
my_list.display() # Expected output: 1 -> 3 -> 4 -> 5 -> Null

my_list.reverse() # CALL THE METHOD DIRECTLY ON YOUR LinkedList INSTANCE

print("Reversed List:")
my_list.display() # Expected output: 5 -> 4 -> 3 -> 1 -> Null
# 1. Define the ListNode class
class ListNode:
    # Constructor for the ListNode class.
    def __init__(self, val=0, next=None):
        # 'val' stores the data of the node. It defaults to 0.
        self.val = val
        # 'next' is a pointer to the next node in the list. It defaults to None.
        self.next = next

# 2. Function to convert a Python list to a linked list
def create_linked_list(arr):
    # Check if the input array is empty. If so, return None for an empty linked list.
    if not arr:
        return None
    # Create the head of the linked list with the first element of the array.
    head = ListNode(arr[0])
    # Create a pointer 'current' to build the list, initially at the head.
    current = head
    # Loop through the rest of the array elements (from the second element onwards).
    for i in range(1, len(arr)):
        # Create a new node for the current element and link it to the 'current' node.
        current.next = ListNode(arr[i])
        # Move the 'current' pointer to the new node to prepare for the next link.
        current = current.next
    # Return the head of the newly created linked list.
    return head

# 3. The main function to merge two sorted linked lists
def mergeTwoLists(l1, l2):
    # Create a dummy node. This node simplifies the logic by serving as a fixed starting point.
    dummy = ListNode(0)
    # The 'current' pointer will be used to build the new list, starting at the dummy node.
    current = dummy
    
    # Loop as long as there are nodes in both linked lists.
    while l1 and l2:
        # Compare the values of the nodes pointed to by l1 and l2.
        if l1.val <= l2.val:
            # If l1's value is smaller, append l1's node to the merged list.
            current.next = l1
            # Move the l1 pointer to its next node.
            l1 = l1.next
        else:
            # If l2's value is smaller, append l2's node.
            current.next = l2
            # Move the l2 pointer to its next node.
            l2 = l2.next
        
        # After a node is appended, move the 'current' pointer forward to the new tail.
        current = current.next
        
    # After the loop, one list might have remaining nodes.
    if l1:
        # If l1 is not empty, append the rest of l1 to the merged list.
        current.next = l1
    elif l2:
        # If l2 is not empty, append the rest of l2 to the merged list.
        current.next = l2

    # Return the head of the final merged list, which is the node after the dummy node.
    return dummy.next

# 4. Create the linked lists from the input data
l1_list = [1, 2, 4]
l2_list = [1, 2, 3]

# Call the helper function to convert the lists into linked lists.
linked_list1 = create_linked_list(l1_list)
linked_list2 = create_linked_list(l2_list)

# 5. Call the merging function
# 'merged_head' will be the head of the final sorted linked list.
merged_head = mergeTwoLists(linked_list1, linked_list2)

# 6. Helper function to print the linked list
def print_linked_list(head):
    # Initialize an empty list to store the values.
    vals = []
    # Use a 'current' pointer to traverse the linked list from the head.
    current = head
    # Loop until the end of the list (when current becomes None).
    while current:
        # Append the value of the current node to the list.
        vals.append(current.val)
        # Move to the next node.
        current = current.next
    # Print the collected values as a list.
    print(vals)

# Output the result.
print("Merged Linked List:")
print_linked_list(merged_head)
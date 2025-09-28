# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        '''
        >> If fast.next is None, then doing fast.next.next would raise an error — because you're trying to access .next on a NoneType.
        >> So the condition while fast and fast.next: ensures:
            - fast is not None
            - fast.next is not None
        >> Only then is it safe to do fast = fast.next.next.
        '''
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

node1 = Node(3)
node2 = Node(2)        
node3 = Node(0)        
node4 = Node(-4)          

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

out = Solution()

print(out.hasCycle(node1))
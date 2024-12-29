"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head: 
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        prev, cur = head, head.next
        while True:
            if prev.val <= insertVal <= cur.val:
                break
            if prev.val > cur.val and (prev.val <= insertVal or insertVal <= cur.val):
                break
            
            prev = cur
            cur = cur.next
            if cur == head:
                break
        
        new_node = Node(insertVal)
        prev.next, new_node.next = new_node, cur
        return head
        
            

    
        
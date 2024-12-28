"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        cur = head

        while cur:
            if cur.child:
                child_node = cur.child
                child_node.prev = cur

                while child_node.next:
                    child_node = child_node.next
                
                if cur.next:
                    child_node.next = cur.next
                    cur.next.prev = child_node
                
                cur.next = cur.child
                cur.child = None
            
            cur = cur .next
        
        return head
                    

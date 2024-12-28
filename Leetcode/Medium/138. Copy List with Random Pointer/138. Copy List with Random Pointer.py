"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        hashmap = {}

        cur = head
        dummy = Node(0)
        ptr = dummy

        while cur:
            ptr.next = Node(cur.val)
            hashmap[cur] = ptr.next
            
            cur, ptr = cur.next, ptr.next

        cur = head
        ptr = dummy.next
        while cur:
            ptr.random = hashmap[cur.random] if cur.random else None
            cur, ptr = cur.next, ptr.next
        
        return dummy.next
        

        

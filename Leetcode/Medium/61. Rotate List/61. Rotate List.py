# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        size = 0
        curr = head
        tail = None
        while curr:
            tail = curr
            size += 1
            curr = curr.next
        
        if size == 0: return head
        k %= size
        if k == 0: return head
        fast = slow = head
        for i in range(k):
            fast = fast.next
        
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = None
        tail.next = head
        head = slow
        return head
        



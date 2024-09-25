# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        prev = None
        for i in range(n):
            curr = curr.next
        tmp = dummy
        prev = None
        while curr:
            curr = curr.next
            prev = tmp
            tmp = tmp.next
        prev.next = tmp.next
        return dummy.next
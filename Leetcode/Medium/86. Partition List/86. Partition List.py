# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode()
        right_dummy = ListNode()

        l = left_dummy
        r = right_dummy

        curr = head
        while curr:
            if curr.val < x:
                l.next = curr
                l = l.next
            else:
                r.next = curr
                r = r.next
            curr = curr.next
        r.next = None
        l.next = right_dummy.next
        return left_dummy.next

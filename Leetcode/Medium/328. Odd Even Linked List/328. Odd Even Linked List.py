# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        cur_odd, cur_even, headEven = head, head.next, head.next

        while cur_even and cur_even.next:
            next_odd = cur_even.next
            cur_odd.next = next_odd
            cur_even.next = next_odd.next

            cur_even = cur_even.next
            cur_odd = next_odd

        cur_odd.next = headEven
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.

        0 -> 1 -> 2 -> 3

        fast None (null Pointer)

        0 -> 3 -> 1 -> 2

        """
        if not head or not head.next: return head
        fast, slow = head, head 
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            prev = slow
            slow = slow.next
        prev.next = None
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        head1 = head
        head2 = prev
        dummy = ListNode()
        curr = dummy
        cnt = 0
        while head1 or head2:
            if not head2:
                curr.next = head1
                break
            curr.next = head1
            head1 = head1.next
            curr = curr.next
            curr.next = head2
            head2 = head2.next
            curr = curr.next
        head = dummy.next
        
        
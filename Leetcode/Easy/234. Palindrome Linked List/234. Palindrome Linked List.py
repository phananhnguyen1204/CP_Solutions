# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            nextNode = slow.next
            fast = fast.next.next
            slow.next = prev
            prev = slow
            slow = nextNode
        if fast:
            slow = slow.next
        while slow:
            if prev.val != slow.val: return False
            prev = prev.next
            slow = slow.next
        return True
        
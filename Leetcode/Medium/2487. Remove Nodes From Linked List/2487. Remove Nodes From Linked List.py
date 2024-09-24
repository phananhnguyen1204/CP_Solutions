# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        8   ->   9 -> 13 -> 2 -> 5
                 prev curr
        '''
        def reverse(head):
            prev, curr = None, head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        head = reverse(head)
        prev, curr = None, head
        while curr:
            if prev and prev.val > curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return reverse(head)
            
            
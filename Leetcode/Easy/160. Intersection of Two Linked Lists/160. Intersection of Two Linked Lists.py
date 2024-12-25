# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return None
        curA = headA
        curB = headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA




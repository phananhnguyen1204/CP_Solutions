# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        '''
        10 1 13 5
        '''
        start, end = list1, list1
        for i in range(b):
            if i == a - 1:
                start = end
            end = end.next
        end = end.next
        prev = start
        start.next = list2
        while list2:
            prev = list2
            list2 = list2.next
        prev.next = end
        return list1


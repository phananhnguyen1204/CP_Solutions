# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        
        while q:
            size = len(q)
            if level % 2 == 1:
                l, r = 0, size - 1
                while l <= r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1

            for _ in range(size):
                curr_node = q.popleft()

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            level += 1
        
        return root
        
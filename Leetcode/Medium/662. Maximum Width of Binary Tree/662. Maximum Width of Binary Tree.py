# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque()
        q.append((root, 0))
        left_most_idx = right_most_idx = 0
        res = 0

        while q:
            size = len(q)
            left_most_idx = -1
            for i in range(size):
                node, idx = q.popleft()
                right_most_idx = idx
                if left_most_idx == -1: left_most_idx = idx
                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))
            res = max(res, right_most_idx - left_most_idx + 1)
        return res

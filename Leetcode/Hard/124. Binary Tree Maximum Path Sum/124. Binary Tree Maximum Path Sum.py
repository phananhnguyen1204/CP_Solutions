# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        use Post Order Traversal, since we don't know if our path contains root or not
        """
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left_max_sum = max(dfs(root.left), 0) # if negative, dont take this left subtree
            right_max_sum = max(dfs(root.right), 0)
            res = max(res, root.val + left_max_sum + right_max_sum)
            return max(left_max_sum, right_max_sum) + root.val
        dfs(root)
        return res
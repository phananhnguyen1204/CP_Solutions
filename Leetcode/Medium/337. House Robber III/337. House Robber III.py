# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root): # [maximum_amount of money if we rob root node, maximum_amount of money if we don't rob root node]
            if not root: return (0, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            # rob this root, can not rob their children
            rob = root.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return [rob, not_rob]
        
        return max(dfs(root))


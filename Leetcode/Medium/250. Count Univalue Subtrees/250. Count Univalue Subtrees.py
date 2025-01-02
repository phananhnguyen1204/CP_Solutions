# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        cnt = 0
        def dfs(root):
            nonlocal cnt

            if not root:
                return True
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                if root.left and root.left.val != root.val:
                    return False
                if root.right and root.right.val != root.val:
                    return False
                cnt += 1
                return True
            return False

        dfs(root)
        return cnt
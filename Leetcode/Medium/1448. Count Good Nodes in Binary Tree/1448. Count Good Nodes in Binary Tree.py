# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0

        def dfs(root, max_node):
            nonlocal cnt
            if not root: return
            max_node = max(max_node, root.val)
            if root.val >= max_node: cnt += 1
            dfs(root.left, max_node)
            dfs(root.right, max_node)

        dfs(root, root.val)
        return cnt
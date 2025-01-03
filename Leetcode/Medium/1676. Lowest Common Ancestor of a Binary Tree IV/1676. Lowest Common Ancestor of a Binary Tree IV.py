# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if not root: return None

        seen = set(nodes)

        def dfs(root):
            if not root:
                return root
            if root in seen:
                return root
            
            l = dfs(root.left)
            r = dfs(root.right)

            if l and r:
                return root
            return l if l else r
        return dfs(root)

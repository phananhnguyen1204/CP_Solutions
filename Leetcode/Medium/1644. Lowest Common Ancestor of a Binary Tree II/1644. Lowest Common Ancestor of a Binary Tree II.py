# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_found, q_found = False, False

        def LCA(root, p, q):
            nonlocal p_found
            nonlocal q_found

            if not root:
                return root

            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)
            
            if root == q or root == p:
                if root == q:
                    q_found = True
                else:
                    p_found = True
                return root

            if left and right:
                return root
            return left if left else right

        res = LCA(root, p, q)
        return res if p_found and q_found else None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_mapping = {v:i for i, v in enumerate(inorder)}

        def dfs(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop())
            idx = idx_mapping[root.val]
            root.right = dfs(idx + 1, r)
            root.left = dfs(l, idx - 1)

            return root

        return dfs(0, len(inorder) - 1)

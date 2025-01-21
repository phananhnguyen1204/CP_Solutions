# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        """
        find the target node

        """

        def dfs(root, target):
            if not root:
                return [None, None]
            if root.val == target:
                big = root.right
                root.right = None
                return [root, big]
            if root.val < target:
                small, big = dfs(root.right, target)
                root.right = small
                return [root, big]
            # root.val < target:
            small, big = dfs(root.left, target)
            root.left = big
            return [small, root]    
        return dfs(root, target)

                
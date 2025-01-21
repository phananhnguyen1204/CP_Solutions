# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(root, curr_sum):
            if not root: return
            path.append(root.val)
            curr_sum += root.val
            if not root.left and not root.right: #leaf node
                if curr_sum == targetSum:
                    res.append(path[:])
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            path.pop()
        dfs(root, 0)

        return res
                
        
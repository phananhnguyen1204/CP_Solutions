# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        res = 0
        # similar to find # of subarray that sum equal target
        def dfs(root, curr_sum):
            nonlocal res
            if not root: return
            curr_sum += root.val
            res += cnt[curr_sum - targetSum]
            cnt[curr_sum] += 1

            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            cnt[curr_sum] -= 1
        
        dfs(root, 0)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            max_val = float("-inf")
            for _ in range(size):
                cur = q.popleft()
                max_val = max(max_val, cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(max_val)
        
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()

        level = 0
        q.append((root, 0))
        while q:
            size = len(q)
            correct_idx = 0
            for i in range(size):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))
                if correct_idx != idx: return False
                correct_idx += 1

            # not the last level
            if q: 
                if size != 2 ** level: return False
            level += 1

        return True
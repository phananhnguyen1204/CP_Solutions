# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root: return []
        
        res = []
        subtrees = {}
        def dfs(node):
            if not node:
                return "null"
            key = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if key not in subtrees:
                subtrees[key] = [node]
            else:
                if len(subtrees[key]) == 1:
                    res.append(node)
                subtrees[key].append(node)
            return key
        
        dfs(root)
        return res
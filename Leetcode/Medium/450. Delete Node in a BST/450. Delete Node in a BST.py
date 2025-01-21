# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            min_val = root.val
            while root.left:
                min_val = root.val
                root = root.left
            return root.val

        def delete(root, key):
            if not root:
                return None
            if root.val == key:
                if not root.left and not root.right:
                    return None 
                if not root.left: return root.right
                if not root.right: return root.left
                root.val = findMin(root.right)
                root.right = delete(root.right, root.val)
                return root

            if root.val < key:
                root.right = delete(root.right, key)
            if root.val > key:
                root.left = delete(root.left, key)
            return root
            

        return delete(root, key)
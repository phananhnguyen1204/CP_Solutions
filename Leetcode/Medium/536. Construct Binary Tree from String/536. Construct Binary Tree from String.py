# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        """
        this problem can not have empty child
        if c is digit or sign: -> add to curr_root

        else:
            if c is (: 
                add parent to stack, reset curr_root to ""
            if c is ")":
                stack[-1] is the parent
                checking if stack[-1].left have been asigned or not
                else update right child
                set num = ""
        """

        if not s: return None
        stack = []
        curr_val = ""

        for c in s:
            if c.isdigit() or c == '-':
                curr_val += c
            elif c == '(':
                # 4(2)(3) -> case when ( is after 4
                if curr_val:
                    node = TreeNode(int(curr_val))
                    stack.append(node)
                    curr_val = ""
                # case when ( is before 3 -> do nothing
            else:
                # 4(2)(3) -> case when ) after 2
                if curr_val:
                    node = TreeNode(int(curr_val))
                    curr_val = ""
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                    # 4(2 (5) (3)) case when ) is the last element
                else:
                    node = stack.pop()
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
            
        return stack[-1] if stack else TreeNode(int(curr_val))
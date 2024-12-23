# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        res = 0

        def bfs():
            q = deque()
            q.append(root)
            while q:
                size = len(q)
                tmp = []
                for _ in range(size):
                    cur_node = q.popleft()
                    tmp.append(cur_node.val)
                    
                    if cur_node.left:
                        q.append(cur_node.left)
                    if cur_node.right:
                        q.append(cur_node.right)
                
                swap_array(tmp)

            return res

        def swap_array(nums):
            nonlocal res
            sorted_nums = sorted(nums)
            print(sorted_nums)
            mapping_index = {}

            for i, num in enumerate(nums):
                mapping_index[num] = i
            
            print(mapping_index)

            for i, num in enumerate(nums):
                if num != sorted_nums[i]:
                    correct_idx = mapping_index[sorted_nums[i]]
                    nums[i] = nums[correct_idx]
                    mapping_index[num] = correct_idx
                    print(correct_idx, num)
                    nums[correct_idx] = num
                    res += 1
            
        bfs()
        return res
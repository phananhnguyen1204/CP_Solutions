class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        1 0 1 0 1
        '''
        diff_map = {}
        one, zero = 0, 0
        res = 0
        for i, num in enumerate(nums):
            if num == 0: zero += 1
            else: one += 1
            diff = one - zero
            if diff not in diff_map:
                diff_map[diff] = i
            if one == zero:
                res = one + zero
            else:
                res = max(res, i - diff_map[diff])
        return res


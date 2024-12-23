class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] != 1:
                l = r + 1
            else:
                res = max(r - l + 1, res)
        
        return res
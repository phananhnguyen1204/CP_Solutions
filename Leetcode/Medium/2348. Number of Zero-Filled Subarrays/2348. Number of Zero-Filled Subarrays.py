class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        cnt_zero = 0 
        for i in range(n):
            if nums[i] == 0:
                cnt_zero += 1
            else:
                cnt_zero = 0
            res += cnt_zero
        return res
            
            
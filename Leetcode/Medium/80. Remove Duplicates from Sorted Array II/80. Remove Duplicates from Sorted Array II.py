class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        
        while r < len(nums):
            cnt = 1

            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                cnt += 1
                r += 1
            
            for _ in range(min(cnt, 2)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        1 3 2 3 4 6
        '''
        max_ele = max(nums)
        l = 0
        res = 0
        cnt = 0
        for r in range(len(nums)):
            if max_ele == nums[r]:
                cnt += 1
            while cnt == k:
                res += len(nums) - r
                if nums[l] == max_ele:
                    cnt -= 1
                l += 1
            
        return res

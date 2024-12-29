class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        for num, freq in freqs.items():
            if freq == 1:
                return num
    

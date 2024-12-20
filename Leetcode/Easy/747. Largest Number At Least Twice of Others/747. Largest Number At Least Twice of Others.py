class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums: return -1
        
        max_element = nums[0]
        index = 0
        for i, num in enumerate(nums):
            if max_element < num:
                index = i
            max_element = max(max_element, num)
        
        for num in nums:
            if num != max_element and num * 2 > max_element:
                return -1
        
        return index
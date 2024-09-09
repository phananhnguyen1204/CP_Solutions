class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)
        for num in nums:
            if num-1 not in seen:
                temp = num
                curr_len = 1
                while temp+1 in seen:
                    curr_len+=1
                    temp+=1
                res = max(curr_len,res)
        return res 
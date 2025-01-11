class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        last_index = {}

        """
        3 4 5 6 5 4
        """
        
        n = len(nums)
        max_score = 0
        start = -1

        prefix = [0] * n
        for i in range(n):
            prefix[i] = nums[i] if i == 0 else prefix[i - 1] + nums[i]
            if nums[i] in last_index:
                start = max(start, last_index[nums[i]])
            # if start == -1:
            #     max_score = max(max_score, prefix[i] - prefix[start] + nums[0])
            # else:
            if start != -1:
                max_score = max(max_score, prefix[i] - prefix[start])  
            else:
                max_score = max(max_score, prefix[i])
            last_index[nums[i]] = i

        return max_score
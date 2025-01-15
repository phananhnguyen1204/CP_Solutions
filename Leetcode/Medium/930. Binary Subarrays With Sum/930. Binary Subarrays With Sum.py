class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        num in nums are all 1, 0 -> can use sliding window (no need to use prefix)
        2 ways:
        +) sliding window at least
        +) prefix sum: finding another subarray has the same difference = sum - goal
        """
        # res = 0
        # n = len(nums)
        # l = total = 0
        # prefix = defaultdict(int)
        # prefix[0] = 1
        
        # for num in nums:
        #     total += num
        #     remain = total - goal
        #     res += prefix[remain]
        #     prefix[total] += 1
        
        # return res
        n = len(nums)
        def at_least(goal):
            l = 0
            res = 0
            total = 0
            
            for r in range(n):
                total += nums[r]
                while l <= r and total >= goal:
                    res += n - r
                    total -= nums[l]
                    l += 1
            return res

        return at_least(goal) - at_least(goal + 1)



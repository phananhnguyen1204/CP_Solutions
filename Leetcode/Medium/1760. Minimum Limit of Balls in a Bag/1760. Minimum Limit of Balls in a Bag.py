class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        def can_make_penalty(penalty):
            res = 0
            for num in nums:
                res += (num - 1) // penalty
            return res <= maxOperations

        while l <= r:
            mid = (l + r) // 2
            if can_make_penalty(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
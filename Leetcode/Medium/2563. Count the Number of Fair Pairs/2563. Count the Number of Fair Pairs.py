class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # cnt # sum pair < upper
        # cnt # sum pair < lower or (cnt # sum pair <= lower - 1)

        # sorting
        nums.sort()
        n = len(nums)

        def cnt_pair_at_most(k):
            cnt = 0
            l, r = 0, n - 1
            while l <= r:
                if (nums[l] + nums[r]) <= k:
                    cnt += r - l
                    l += 1
                else:
                    r -= 1
            return cnt
        return cnt_pair_at_most(upper) - cnt_pair_at_most(lower-1)
            
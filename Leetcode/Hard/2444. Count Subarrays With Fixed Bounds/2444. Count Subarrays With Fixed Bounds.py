class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        can not use sliding window -> since we expaned the window, we could increase the max and min
        -> need to find how many valid subarray ending at i index
            min max
        [3, 1, 5, 2, 7, 5]
        -> keep track of most recent max_element and min_element so far
        -> record bad_idx: the index that is out of bound (minK > nums[bad_idx] and nums[bad_idx] > maxK)
        if bad_idx > min(max_element_idx, min_element_idx) -> no the subarray is valid that ending at i index
        """

        res = 0
        min_idx = max_idx = bad_idx = -1
        n = len(nums)

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                bad_idx = i
            if nums[i] == maxK:
                max_idx = i
            if nums[i] == minK:
                min_idx = i
            res += max(0, min(min_idx, max_idx) - bad_idx)

        return res


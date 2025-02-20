class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 0: return nums[0]
        if k == 1:
            return -1 if n == 1 else nums[1]
        # k >= 2
        if n == 1:
            return -1 if( k % 2 == 1) else nums[0]
        # k >= 2 and n >= 2
        if k > n: return max(nums)
        if k == n: return max(nums[:k-1])
        # k < n
        return max(max(nums[:k-1]), nums[k])

        
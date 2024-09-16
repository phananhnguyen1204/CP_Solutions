class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n // 2
        res = [0] * n
        nums.sort()
        for k in range(n):
            if k % 2 == 1:
                res[k] = nums[i]
                i += 1
            else:
                res[k] = nums[j]
                j += 1
        return res
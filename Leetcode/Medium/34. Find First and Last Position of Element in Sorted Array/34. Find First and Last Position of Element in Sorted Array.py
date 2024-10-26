class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1] * 2
        n = len(nums)
        if n == 0 or nums[0] > target or nums[n-1] < target: return res

        l, r = 0, n - 1
        while(l <= r):
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        
        if nums[l] == target:
            res[0] = l
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[r] == target:
            res[1] = r
        return res
        
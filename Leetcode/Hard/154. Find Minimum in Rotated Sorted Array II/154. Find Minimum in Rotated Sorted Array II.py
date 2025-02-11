class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # 3 3 1
        # 3 3 3
        # 1 3 3

        while l < r:
            mid = (l + r) // 2
            print(mid)
            while l < r and nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]
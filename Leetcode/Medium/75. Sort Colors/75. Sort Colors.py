class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        [2,0,2,1,1,0]

        """
        l,n = 0,len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i],nums[l] = nums[l], nums[i]
                l+=1
        r = n-1
        for i in range(n-1,-1,-1):
            if nums[i]==2:
                nums[i],nums[r] = nums[r], nums[i]
                r-=1
        return nums
        
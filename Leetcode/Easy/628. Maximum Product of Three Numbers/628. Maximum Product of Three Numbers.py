class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        
        """

        max1 = max2 = max3 = float("-inf")
        min1 = min2 = float("inf")
        n = len(nums)
        for i in range(n):
            if nums[i] <= min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] <= min2:
                min2 = nums[i]

            if nums[i] >= max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif nums[i] >= max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] >= max3:
                max3 = nums[i]
        print(max1, max2, max3)
        return max(max1 * max2 * max3, max1 * min1 * min2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] > 0: break
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]: k -= 1
                elif total > 0: 
                    k -= 1
                else: j += 1
        return res
                    
           
        return res
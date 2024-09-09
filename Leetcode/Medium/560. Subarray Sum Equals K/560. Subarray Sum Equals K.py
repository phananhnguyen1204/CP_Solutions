class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {}
        '''

        '''
        cnt[0] = 1
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum +=num
            if curr_sum - k in cnt:
                res += cnt[curr_sum-k]
            cnt[curr_sum] = cnt.get(curr_sum,0) + 1
        return res
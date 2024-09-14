class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = {}
        '''
        {
            2: 4
            3: 3
            4: 2
        }
        '''
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        res = 0
        for val in cnt.values():
            if val == 1: return -1
            res += val // 3
            if val % 3 == 2 or val % 3 == 1:
                res += 1
        return res
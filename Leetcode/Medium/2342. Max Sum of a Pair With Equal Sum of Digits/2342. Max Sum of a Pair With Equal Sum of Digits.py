from heapq import heappush, heappop
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        def sum_digit(x):
            res = 0
            while x > 0:
                res += x % 10
                x //= 10
            return res
        # 1st approach:
        for num in nums:
            key = sum_digit(num)
            heappush(cnt[key], num)
            if len(cnt[key]) > 2:
                heappop(cnt[key])

        res = -1
        print(cnt)
        for _, values in cnt.items():
            if len(values) >= 2:
                res = max(heappop(values) + heappop(values), res)
        return res 

        # 2nd approach:
        # hashmap storing key -> digit
        # value: maximum value so far


        
            
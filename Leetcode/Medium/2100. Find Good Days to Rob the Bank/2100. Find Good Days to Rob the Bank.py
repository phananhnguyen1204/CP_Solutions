class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        """
        day: 0th index
        prefix[i]: store how many days before ith day it is non-increasing
        suffix[i]: store how many days after ith day it is non-decreasing
        every day: checking prefix[i] >= time and suffix[i] >= time
        """
        n = len(security)
        if time == 0: return [i for i in range(n)]
        res = []
        prefix = [0] * n
        suffix = [0] * n
        
        start = 0
        for i in range(1, n):
            if security[i] > security[i-1]:
                start = i
            else:
                prefix[i] = i - start

        end = n - 1
        for i in range(n-2, -1, -1):
            if security[i] > security[i + 1]:
                end = i
            else:
                suffix[i] = end - i

        for i in range(n):
            if i - time < 0 or i + time >= n:
                continue
            if prefix[i] >= time and suffix[i] >= time:
                res.append(i)
        return res


        


        
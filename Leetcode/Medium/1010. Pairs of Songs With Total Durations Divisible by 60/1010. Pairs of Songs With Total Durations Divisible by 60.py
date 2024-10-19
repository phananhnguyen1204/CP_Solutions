class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        cnt = {}
        for x in time:
            remainder = x % 60
            complement =( 60 - remainder) % 60
            if complement in cnt:
                res += cnt[complement]
            cnt[remainder] = cnt.get(remainder, 0) + 1
        
        return res
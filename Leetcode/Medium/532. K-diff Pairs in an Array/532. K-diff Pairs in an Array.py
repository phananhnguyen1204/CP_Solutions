class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # find if num + k exist in hashmap
        # pair of value not pair of index -> only care abt unique value in nums list
        # (1, 3) is the same as (3, 1)
        # num can be negative

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        res = 0
        for num, cnt in freq.items():
            # if k == 0
            # every element can amke a pair to other same element not including itselfs
            if k == 0 and cnt > 1:
                res += 1
            if k != 0 and num + k in freq:
                res += 1

        return res

        # this will work if k > 0
        # seen = set(nums)
        # res = 0
        # for num in seen:
        #     if num + k in seen:
        #         res += 1
        # return res
        


